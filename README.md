# AlphaFold Use Case Explorer

An interactive web explainer showcasing real-world applications of AlphaFold in digital biology — from drug discovery to environmental science.

![AlphaFold Use Case Explorer](https://img.shields.io/badge/AlphaFold-Use%20Case%20Explorer-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![No Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)

## Features

### Interactive Timeline
Explore the evolution of AlphaFold from its inception in 2018 to the groundbreaking AlphaFold 3 in 2024, featuring:
- AlphaFold 1 (2018) - CASP13 victory
- AlphaFold 2 (2020) - Solving the protein folding problem
- AlphaFold Database (2021) - Democratizing protein structures
- AlphaFold 3 (2024) - Expanding to DNA, RNA, and small molecules

### Real-World Use Cases
Deep-dive into five major applications with expandable cards:

1. **Drug Discovery** - Accelerating pharmaceutical development
2. **Protein Engineering** - Designing novel proteins for biotechnology
3. **Disease Research** - Understanding and treating genetic diseases
4. **Agriculture** - Engineering resilient and nutritious crops
5. **Environmental Science** - Tackling pollution and climate change

Each use case includes:
- Detailed applications and examples
- Key metrics and impact data
- Real-world success stories

### How AlphaFold Works
A simplified 5-step explanation of the technology:
- Input processing and sequence alignment
- Deep learning neural networks
- Structure prediction and refinement
- Confidence scoring and validation
- Impact on scientific research

### Modern Web Experience
- **Dark Mode Toggle** - Seamless theme switching with localStorage persistence
- **Smooth Animations** - Intersection Observer for scroll-triggered animations
- **Responsive Design** - Optimized for desktop, tablet, and mobile
- **Zero Dependencies** - Pure HTML, CSS, and JavaScript
- **Keyboard Accessible** - Full navigation support for accessibility

## Technical Stack

- **HTML5** - Semantic markup
- **CSS3** - Custom properties, Grid, Flexbox, animations
- **Vanilla JavaScript** - No frameworks or libraries
- **GitHub Pages** - Automated deployment via GitHub Actions

## Project Structure

```
alphafold-use-case-explorer/
├── index.html              # Main HTML file
├── style.css               # Styles with dark mode theming
├── script.js               # Interactive functionality
├── LICENSE                 # MIT License
├── .gitignore              # Git ignore rules
├── requirements-test.txt   # Python testing dependencies
├── .github/
│   └── workflows/
│       └── pages.yml       # GitHub Pages deployment
└── tests/
    └── test_structure.py   # Automated tests
```

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/serenakeyitan/alphafold-use-case-explorer.git
cd alphafold-use-case-explorer
```

2. Open `index.html` in your browser:
```bash
# On macOS
open index.html

# On Linux
xdg-open index.html

# On Windows
start index.html
```

Or use a simple HTTP server:
```bash
# Python 3
python -m http.server 8000

# Node.js
npx http-server
```

Then visit `http://localhost:8000`

## Testing

The project includes automated tests for HTML structure, CSS validity, and JavaScript functionality.

### Run Tests Locally

1. Install dependencies:
```bash
pip install -r requirements-test.txt
```

2. Run tests:
```bash
pytest -v tests/
```

### CI/CD Pipeline

Every push and pull request triggers:
- HTML structure validation
- CSS parsing and theming checks
- JavaScript file verification
- Automated deployment to GitHub Pages (on main branch)

## Deployment

The site is automatically deployed to GitHub Pages on every push to the `main` branch.

Live site: `https://serenakeyitan.github.io/alphafold-use-case-explorer/`

## Credits

- **AlphaFold** - [DeepMind](https://www.deepmind.com/research/highlighted-research/alphafold)
- **AlphaFold Database** - [EMBL-EBI](https://alphafold.ebi.ac.uk/)
- **Inspiration** - [@demishassabis](https://twitter.com/demishassabis)

## License

MIT License - see [LICENSE](LICENSE) file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

This project was created to showcase the transformative impact of AlphaFold on biology and medicine. Special thanks to the DeepMind team and the broader scientific community for their groundbreaking work in computational biology.

---

Built with ❤️ for the digital biology community
