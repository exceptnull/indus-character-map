def generate_html_divs():
    divs = []
    for codepoint in range(0xE000, 0xE3EA):  # PUA codepoints from U+E000 to U+E3E9
        hex_code = f"U+{codepoint:04X}"
        decimal_value = codepoint - 0xE000  # Decimal value starts from 0 for U+E000
        char = chr(codepoint)

        # Check if the character is renderable (may need a font check in practice, assuming blank otherwise)
        if char == "\uFFFD":
            # If the codepoint has a blank symbol, generate empty character div
            div_html = f'<div class="character-box" title="{hex_code}"> <small>{hex_code}<br>({decimal_value})</small></div>'
        else:
            # If the codepoint has a valid symbol, generate normal character div
            div_html = f'<div class="character-box" title="{hex_code}">&#x{codepoint:04X};<small>{hex_code}<br>({decimal_value})</small></div>'

        divs.append(div_html)

    return "\n".join(divs)

# Example of generating the divs as a string
if __name__ == "__main__":
    html_string = (
        "<!DOCTYPE html>\n"
        "<html lang=\"en\">\n"
        "  <head>\n"
        "    <meta charset=\"UTF-8\">\n"
        "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
        "    <title>Indus Valley Script Character Map</title>\n"
        "    <link rel=\"stylesheet\" href=\"style.css\">\n"
        "    <link href=\"https://fonts.googleapis.com/css2?family=Inconsolata:wght@400;700&display=swap\" rel=\"stylesheet\">\n"
        "  </head>\n"
        "  \n"
        "<body class=\"dark-theme\">\n"
        "  <header>\n"
        "    <h1>Indus Valley Script Character Map</h1>\n"
        "    <div class=\"theme-toggle\">\n"
        "      <label for=\"themeSwitch\">Light Theme</label>\n"
        "      <input type=\"checkbox\" id=\"themeSwitch\" />\n"
        "    </div>\n"
        "  </header>\n"
        "\n"
        "  <!-- Documentation Section -->\n"
        "  <section id=\"documentation\">\n"
        "    <h2>Documentation</h2>\n"
        "    <p>This font uses Private Use Area (PUA) encoding from U+E000 onwards to represent the characters of the Indus Valley script. Below is a character map with each glyph and its associated PUA code. Any rectangular boxes ▯ in the character map are to be treated as blanks i.e., these PUA codepoints don't accomodate any IVC glyphs.</p>\n"
        "  </section>\n"
        "\n"
        "  <!-- Character Map Section -->\n"
        "  <section id=\"character-map\">\n"
        "    <h2>Character Map</h2>\n"
        "    <div class=\"character-map\">\n"
        + generate_html_divs() +
        "    </div>\n"
        "  </section>\n"
        "\n"
        "  <!-- Usage Examples Section -->\n"
        "  <section id=\"usage-examples\">\n"
        "    <h2>Usage Examples</h2>\n"
        "    <p>To use this font on your website, include the following CSS in your stylesheet:</p>\n"
        "    <pre>\n"
        "@font-face {\n"
        "  font-family: 'IndusFont';\n"
        "  src: url('fonts/IndusFont.woff2') format('woff2'),\n"
        "       url('fonts/IndusFont.ttf') format('truetype');\n"
        "}\n"
        "    </pre>\n"
        "    <p>Apply it to any element by setting <code>font-family: 'IndusFont';</code>.</p>\n"
        "  </section>\n"
        "\n"
        "  <footer>\n"
        "    <p>\n"
        "      Font source: <a href=\"https://github.com/decipher-indus/font\" target=\"_blank\">GitHub - Indus Valley Script Font</a>\n"
        "    </p>\n"
        "    <p>\n"
        "      Main website: <a href=\"https://indusscript.net/\" target=\"_blank\">Indus Script Project</a>\n"
        "    </p>  \n"
        "  </footer>\n"
        "\n"
        "  <script src=\"script.js\"></script>\n"
        "</body>\n"
        "</html>"
    )
    
    # Print the HTML string
    print(html_string)
    
    # Write the HTML string to a file named 'index.html'
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_string)
