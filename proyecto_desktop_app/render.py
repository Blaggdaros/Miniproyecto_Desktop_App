import json

import markdown2
import mistune
from pygments import highlight, lexers
from pygments.formatters import HtmlFormatter


def render_markdown(markdown_text):
    formatter = HtmlFormatter(style="colorful")

    sections = markdown_text.split("```")
    html_sections = []

    for section in sections:
        if section.startswith("{"):
            # Se encontró una sección de código JSON
            try:
                json_data = json.loads(section)
                # Renderizar como código JSON resaltado
                lexer = lexers.JsonLexer()
                html_section = highlight(
                    json.dumps(json_data, indent=4), lexer, formatter
                )
            except json.JSONDecodeError:
                # Si el JSON no es válido, renderizar como Markdown normal
                html_section = mistune.markdown(section)
        else:
            # No es una sección de código JSON, buscar el lexer según el lenguaje
            language = section.split("\n", 1)[0]
            try:
                lexer = lexers.get_lexer_by_name(language)
            except lexers.ClassNotFound:
                # Si no se encuentra el lexer, renderizar como Markdown normal
                html_section = mistune.markdown(section)
            else:
                # Renderizar como código resaltado del lenguaje correspondiente
                html_section = highlight(section, lexer, formatter)

        html_sections.append(html_section)

    # Combinar todas las secciones en un solo HTML
    html_with_highlight = "".join(html_sections)

    # Obtener el código CSS generado por Pygments
    pygments_css = formatter.get_style_defs(".highlight")

    # Agregar el código CSS al HTML
    html_with_css = f"<style>{pygments_css}</style>\n{html_with_highlight}"

    return html_with_css
