# Agente Web — Generador de proyectos HTML/CSS/JS

Agente local basado en LLM que genera proyectos web completos con HTML5, hojas de estilo CSS y scripts JavaScript, organizados en carpetas y listos para abrir en el navegador.

## Requisitos

- Python 3.10+
- [Ollama](https://ollama.com/) instalado y corriendo localmente
- Modelo descargado: `ollama pull qwen2.5-coder:7b`

## Instalación

```bash
pip install ollama
```

## Uso

```bash
python agent.py
```

Luego escribe tu solicitud, por ejemplo:
- `Crea una landing page para una cafetería con menú y formulario de contacto`
- `Genera una página de portafolio personal con sección de proyectos`
- `Haz una calculadora interactiva con HTML, CSS y JS`

El proyecto generado se guarda automáticamente en `workspace/<nombre-proyecto>/`.

## Estructura del proyecto generado

```
workspace/
└── nombre-proyecto/
    ├── index.html
    ├── styles/
    │   └── main.css
    └── scripts/
        └── main.js
```

## Skills disponibles

| Skill | Descripción |
|---|---|
| `estructura_salida.md` | Formato XML obligatorio de la respuesta |
| `crear_html.md` | Generación de HTML5 semántico |
| `crear_estilos.md` | Hojas de estilo CSS organizadas y responsive |
| `crear_scripts.md` | Scripts JS con ES6+ para interacción |
| `estructura_proyecto.md` | Organización de carpetas del proyecto web |
| `revisar_codigo_web.md` | Revisión y corrección de código web |

## Agregar nuevas skills

Crear un archivo `.md` en la carpeta `skills/` con el nombre y las instrucciones. El agente la cargará automáticamente en el próximo inicio.
