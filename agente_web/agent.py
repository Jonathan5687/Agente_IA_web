import ollama
from skill_loader import load_all_skills
from project_writer import save_project_from_response

MODEL = "qwen2.5-coder:3b"

def build_system_prompt() -> str:
    skills = load_all_skills()

    return f"""
Eres un agente local especializado en generación de proyectos web.
Generas código HTML5, hojas de estilo CSS y scripts JavaScript.

REGLAS ABSOLUTAS — debes cumplirlas siempre sin excepción:
1. NUNCA hagas preguntas al usuario.
2. NUNCA pidas más información ni detalles adicionales.
3. Con la información que recibas, genera SIEMPRE un proyecto web completo de inmediato.
4. Si falta algún detalle, usa valores razonables por defecto.
5. Tu respuesta DEBE comenzar con <project name="..."> y terminar con </project>.
6. Cada archivo va dentro de su propia etiqueta <file name="ruta/archivo">.
7. No escribas NADA fuera de las etiquetas <project>...</project>.
8. No uses bloques de código markdown (no uses ```html ni ```css ni ```js).

Debes usar las siguientes skills cargadas desde archivos Markdown:

{skills}
"""


def ask_agent(user_prompt: str) -> str:
    system_prompt = build_system_prompt()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user",   "content": user_prompt}
    ]

    response = ollama.chat(model=MODEL, messages=messages)
    answer = response["message"]["content"]

    # Si no sigue el formato, reintenrar una vez más con un mensaje de corrección
    if "<project" not in answer:
        print("\n⚠  El modelo no usó el formato correcto. Reintentando...\n")
        messages.append({"role": "assistant", "content": answer})
        messages.append({
            "role": "user",
            "content": (
                "Tu respuesta no siguió el formato requerido. "
                "NO uses bloques ```html ni ```css ni ```js. "
                "Responde ÚNICAMENTE con esta estructura exacta:\n\n"
                "<project name=\"nombre-proyecto\">\n"
                "<file name=\"index.html\">\n"
                "...código HTML completo aquí...\n"
                "</file>\n"
                "<file name=\"styles/main.css\">\n"
                "...código CSS completo aquí...\n"
                "</file>\n"
                "<file name=\"scripts/main.js\">\n"
                "...código JS completo aquí...\n"
                "</file>\n"
                "</project>\n\n"
                "Sin texto adicional fuera de esas etiquetas. Genera el proyecto ahora."
            )
        })
        response = ollama.chat(model=MODEL, messages=messages)
        answer = response["message"]["content"]

    return answer


if __name__ == "__main__":
    print("Agente local Web con skills en Markdown")
    print("Escribe 'salir' para terminar.\n")

    while True:
        prompt = input("Solicitud: ")

        if prompt.lower() == "salir":
            break

        answer = ask_agent(prompt)
        print("\n--- RESPUESTA DEL AGENTE ---\n")
        print(answer)
        print("\n----------------------------------\n")

        try:
            project_dir = save_project_from_response(answer)
            print(f"\nProyecto generado en: {project_dir}\n")
        except ValueError as e:
            print(f"\n✗ No se pudo guardar el proyecto: {e}")
            print("Intenta reformular tu solicitud.\n")
