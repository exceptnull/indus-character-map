[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Indus Valley Script Character Map

This project is a web-based character map for the Indus Valley Script, designed to make characters easily accessible and provide users with the ability to copy individual characters to their clipboard. The project includes both dark and light theme options, styled similarly to Slack, and is mobile-friendly.

## Live Demo

View the live demo here: [Indus Valley Script Character Map](https://exceptnull.github.io/indus-character-map/)

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Features

- **Character Map**: Displays characters in the Private Use Area (PUA) Unicode range, used for representing Indus Valley Script symbols.
- **Copy to Clipboard**: Click any character to copy it directly to your clipboard.
- **Dark/Light Theme Toggle**: Switch between themes using a toggle in the top header.
- **Responsive Design**: Optimized for both desktop and mobile views.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/exceptnull/indus-character-map.git
   cd indus-character-map
   ```

2. **Files**:
   - `index.html`: The main HTML file.
   - `style.css`: Contains the styling for both dark and light themes.
   - `script.js`: JavaScript for theme toggle and copy functionality.
   - `fonts/IndusFont.woff2` and `fonts/IndusFont.ttf`: Custom fonts for the Indus Valley Script characters.
   - `html-gen.py`: Autogenerates `index.html`

3. **Fonts**:
   - The font files are from the [Indus Valley Script Font Repository](https://github.com/decipher-indus/font).

4. **Open the Project**:
   - Open `index.html` in a browser to view the character map locally.

## Usage

- **Toggle Themes**: Click the checkbox at the top-right to switch between dark and light themes.
- **Copy Characters**: Click any character box to copy the character to your clipboard. A green highlight will briefly show when copied.
- **Responsive**: The character map layout adjusts based on screen size, making it easy to use on mobile devices.

## Customization

To further customize:

- **Change Fonts**: Update the font by replacing `IndusFont.woff2` and `IndusFont.ttf` in the `fonts` folder.
- **Modify Styles**: Adjust colors, font sizes, and other styles in `style.css`.
- **Add New Features**: Modify `script.js` for additional interactivity.

## Contributing

Contributions are welcome! Feel free to submit issues, feature requests, or pull requests.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Acknowledgments

- **Indus Script Project**: [https://indusscript.net/](https://indusscript.net/) - Main repository for the Indus Valley Script Project.
- **Font Source**: [GitHub - Indus Valley Script Font](https://github.com/decipher-indus/font).

## License

This project is licensed under the MIT License.
