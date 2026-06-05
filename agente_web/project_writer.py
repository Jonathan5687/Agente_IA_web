import re
from pathlib import Path

WORKSPACE_DIR = Path("workspace")


def strip_code_fences(text: str) -> str:
    """Elimina bloques de markdown tipo ```html ... ``` que el modelo agrega."""
    text = re.sub(r'```[a-zA-Z]*\n?', '', text)
    text = re.sub(r'```', '', text)
    return text.strip()


def extract_project_name(response_text: str) -> str:
    # <project name="nombre">
    match = re.search(r'<project\s+name="([^"]+)">', response_text)
    if match:
        return match.group(1).strip()

    # si no: <project> sin atributo name → usar nombre genérico
    if re.search(r'<project\s*>', response_text):
        return "proyecto-web"

    raise ValueError("No se encontró etiqueta <project>")


def extract_files(response_text: str):
    # etiquetas <file name="...">
    pattern = r'<file\s+name="([^"]+)">\s*(.*?)\s*</file>'
    files = re.findall(pattern, response_text, re.DOTALL)

    if files:
        return files

    # En caso que el modelo metió todo en <project> sin <file> → guardar como index.html
    project_content = re.search(
        r'<project[^>]*>\s*(.*?)\s*</project>',
        response_text,
        re.DOTALL
    )
    if project_content:
        content = project_content.group(1).strip()
        if content:
            print("⚠  El modelo no usó etiquetas <file>. Guardando todo como index.html.")
            return [("index.html", content)]

    raise ValueError("No se encontró contenido válido para guardar.")


def save_project_from_response(response_text: str) -> Path:
    clean_text = strip_code_fences(response_text)

    project_name = extract_project_name(clean_text)
    files = extract_files(clean_text)

    project_dir = WORKSPACE_DIR / project_name
    project_dir.mkdir(parents=True, exist_ok=True)

    for filename, content in files:
        file_path = project_dir / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content.strip(), encoding="utf-8")
        print(f"✓ Archivo creado: {file_path}")

    print(f"\nProyecto creado en: {project_dir}")
    return project_dir
