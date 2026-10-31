import json
import os

# CONFIGURACIÓN DE ESTILOS PERSONALIZADOS
# Aquí puedes poner el color de borde y de fondo que te dé la gana (ej. amarillo: "#FFD700")
BORDER_COLOR = "#FFD700"  # Cambia esto al color que quieras (ej: Amarillo)
BG_COLOR = "#030B12"  # Color de fondo de la celda

def generate_table(apps, cols=4):
    rows = []
    for i in range(0, len(apps), cols):
        chunk = apps[i:i + cols]
        cells = []
        for app in chunk:
            # Usamos atributos HTML seguros que GitHub no descarta tan fácilmente
            cells.append(f'''<td align="center" bgcolor="{BG_COLOR}" style="border: 2px solid {BORDER_COLOR}; background-color: {BG_COLOR}; padding: 2px;">
<a href="{app['url']}">
<img src="{app['img']}" width="80" alt="{app['name']}">
</a>
</td>''')
        while len(cells) < cols:
            cells.append('<td align="center">&nbsp;</td>')
        rows.append("<tr>\n" + "\n".join(cells) + "\n</tr>")
    return "\n".join(rows)

def build_showcase():
    with open("apps.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    dark_html = generate_table(data.get("dark_tools", []))
    general_html = generate_table(data.get("general_apps", []))

    return f'''<table width="100%" align="center" cellspacing="5" cellpadding="0">
<tr>
<td width="50%" valign="top" align="center">
<h2>😈 Dark Tools 😈</h2>
<b>Root &nbsp;·&nbsp; Pentesting &nbsp;·&nbsp; Android</b>
<br><br>
<table align="center" cellspacing="4" cellpadding="0">
{dark_html}
</table>
</td>
<td width="50%" valign="top" align="center">
<h2>📱 General Apps 📱</h2>
<b>Utilities &nbsp;·&nbsp; Accessibility &nbsp;·&nbsp; Science</b>
<br><br>
<table align="center" cellspacing="4" cellpadding="0">
{general_html}
</table>
</td>
</tr>
</table>'''

def main():
    if not os.path.exists("README.md"):
        print("❌ README.md no encontrado.")
        return

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    start_tag = "<!-- APP_SHOWCASE_START -->"
    end_tag = "<!-- APP_SHOWCASE_END -->"

    if start_tag not in content or end_tag not in content:
        print("❌ Faltan las etiquetas de marcado en el README.md")
        return

    start_idx = content.find(start_tag) + len(start_tag)
    end_idx = content.find(end_tag)

    new_content = content[:start_idx] + "\n\n" + build_showcase() + "\n\n" + content[end_idx:]

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

    print("🚀 README.md actualizado con tus bordes y colores personalizados!")

if __name__ == "__main__":
    main()
