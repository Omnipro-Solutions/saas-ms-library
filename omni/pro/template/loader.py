try:
    from jinja2 import Template
except ImportError:
    # print("No se pudo importar la librería Jinja2. Por favor instálala con 'pip install Jinja2'")
    pass


def render_to_string(template_name: str, context: dict) -> str:
    # Crear una instancia de la plantilla
    template = Template(template_name)
    # Renderizar la plantilla con el contexto
    return template.render(context)
