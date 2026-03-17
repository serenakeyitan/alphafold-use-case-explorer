"""
Tests for AlphaFold Use Case Explorer structure and content
"""
import os
from pathlib import Path
from bs4 import BeautifulSoup
import cssutils
import logging

# Suppress cssutils logging
cssutils.log.setLevel(logging.CRITICAL)

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent


def test_required_files_exist():
    """Test that all required files are present"""
    required_files = [
        'index.html',
        'style.css',
        'script.js',
        'LICENSE',
        '.gitignore',
        'requirements-test.txt'
    ]

    for file in required_files:
        file_path = PROJECT_ROOT / file
        assert file_path.exists(), f"Required file {file} not found"


def test_html_structure():
    """Test HTML structure and required sections"""
    with open(PROJECT_ROOT / 'index.html', 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Check DOCTYPE
    assert soup.contents[0].strip().lower().startswith('<!doctype html'), "Missing or incorrect DOCTYPE"

    # Check meta tags
    assert soup.find('meta', {'charset': True}), "Missing charset meta tag"
    assert soup.find('meta', {'name': 'viewport'}), "Missing viewport meta tag"
    assert soup.find('meta', {'name': 'description'}), "Missing description meta tag"

    # Check title
    title = soup.find('title')
    assert title, "Missing title tag"
    assert 'AlphaFold' in title.string, "Title doesn't mention AlphaFold"

    # Check stylesheets
    assert soup.find('link', {'rel': 'stylesheet', 'href': 'style.css'}), "Missing style.css link"

    # Check script
    assert soup.find('script', {'src': 'script.js'}), "Missing script.js link"

    # Check navigation
    nav = soup.find('nav', class_='navbar')
    assert nav, "Missing navigation bar"

    # Check main sections
    assert soup.find('section', id='hero'), "Missing hero section"
    assert soup.find('section', id='timeline'), "Missing timeline section"
    assert soup.find('section', id='use-cases'), "Missing use cases section"
    assert soup.find('section', id='how-it-works'), "Missing how-it-works section"

    # Check footer
    assert soup.find('footer'), "Missing footer"


def test_dark_mode_toggle():
    """Test that dark mode toggle exists"""
    with open(PROJECT_ROOT / 'index.html', 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    dark_mode_toggle = soup.find(id='dark-mode-toggle')
    assert dark_mode_toggle, "Missing dark mode toggle button"


def test_timeline_items():
    """Test that timeline has all required years"""
    with open(PROJECT_ROOT / 'index.html', 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    timeline_section = soup.find('section', id='timeline')
    assert timeline_section, "Missing timeline section"

    timeline_items = timeline_section.find_all('div', class_='timeline-item')
    assert len(timeline_items) >= 4, f"Expected at least 4 timeline items, found {len(timeline_items)}"

    # Check for key years
    timeline_text = timeline_section.get_text()
    assert '2018' in timeline_text, "Timeline missing 2018 (AlphaFold 1)"
    assert '2020' in timeline_text, "Timeline missing 2020 (AlphaFold 2)"
    assert '2021' in timeline_text, "Timeline missing 2021 (AlphaFold Database)"
    assert '2024' in timeline_text, "Timeline missing 2024 (AlphaFold 3)"


def test_use_case_cards():
    """Test that use case cards are present"""
    with open(PROJECT_ROOT / 'index.html', 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    use_cases_section = soup.find('section', id='use-cases')
    assert use_cases_section, "Missing use cases section"

    cards = use_cases_section.find_all('div', class_='use-case-card')
    assert len(cards) >= 5, f"Expected at least 5 use case cards, found {len(cards)}"

    # Check that each card has required elements
    for card in cards:
        assert card.find('h3', class_='card-title'), "Card missing title"
        assert card.find('button', class_='expand-button'), "Card missing expand button"
        assert card.find('div', class_='card-expanded-content'), "Card missing expanded content"


def test_css_valid():
    """Test that CSS file is valid and parseable"""
    css_path = PROJECT_ROOT / 'style.css'
    assert css_path.exists(), "CSS file not found"

    # Parse CSS
    sheet = cssutils.parseFile(str(css_path))
    assert len(sheet.cssRules) > 0, "CSS file appears to be empty"


def test_css_custom_properties():
    """Test that CSS custom properties for theming exist"""
    with open(PROJECT_ROOT / 'style.css', 'r') as f:
        css_content = f.read()

    # Check for :root variables
    assert ':root' in css_content, "Missing :root selector for CSS custom properties"

    # Check for key theme variables
    theme_vars = [
        '--bg-primary',
        '--bg-secondary',
        '--text-primary',
        '--text-secondary',
        '--accent-primary'
    ]

    for var in theme_vars:
        assert var in css_content, f"Missing CSS custom property: {var}"

    # Check for dark theme
    assert '[data-theme="dark"]' in css_content or 'data-theme' in css_content, "Missing dark theme CSS"


def test_css_responsive():
    """Test that CSS has responsive breakpoints"""
    with open(PROJECT_ROOT / 'style.css', 'r') as f:
        css_content = f.read()

    # Check for media queries
    assert '@media' in css_content, "No media queries found in CSS"
    assert 'max-width' in css_content or 'min-width' in css_content, "No responsive breakpoints found"


def test_javascript_file():
    """Test that JavaScript file exists and has required functionality"""
    js_path = PROJECT_ROOT / 'script.js'
    assert js_path.exists(), "JavaScript file not found"

    with open(js_path, 'r') as f:
        js_content = f.read()

    # Check for key functionality
    assert 'dark-mode-toggle' in js_content or 'darkModeToggle' in js_content, "Missing dark mode toggle logic"
    assert 'localStorage' in js_content, "Missing localStorage for theme persistence"
    assert 'IntersectionObserver' in js_content or 'scroll' in js_content, "Missing scroll animation logic"


def test_navigation_links():
    """Test that navigation links point to correct sections"""
    with open(PROJECT_ROOT / 'index.html', 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    nav_links = soup.find_all('a', class_='nav-link')
    assert len(nav_links) > 0, "No navigation links found"

    for link in nav_links:
        href = link.get('href', '')
        if href.startswith('#'):
            section_id = href[1:]
            section = soup.find(id=section_id)
            assert section, f"Navigation link points to non-existent section: {section_id}"


def test_footer_content():
    """Test that footer has required content"""
    with open(PROJECT_ROOT / 'index.html', 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    footer = soup.find('footer')
    assert footer, "Missing footer"

    footer_text = footer.get_text()
    assert 'DeepMind' in footer_text or 'demishassabis' in str(footer), "Footer missing DeepMind/Demis Hassabis credit"
    assert 'MIT' in footer_text or 'License' in footer_text, "Footer missing license information"


def test_accessibility_basics():
    """Test basic accessibility features"""
    with open(PROJECT_ROOT / 'index.html', 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Check that buttons have aria-labels or text content
    buttons = soup.find_all('button')
    for button in buttons:
        has_aria_label = button.get('aria-label')
        has_text = button.get_text(strip=True)
        assert has_aria_label or has_text, f"Button missing aria-label or text content: {button}"

    # Check that links have meaningful text
    links = soup.find_all('a')
    for link in links:
        link_text = link.get_text(strip=True)
        # Skip empty links (they might be icon-only with aria-labels)
        if link_text:
            assert len(link_text) > 1, f"Link has non-meaningful text: {link_text}"


def test_no_broken_internal_links():
    """Test that internal links don't point to non-existent elements"""
    with open(PROJECT_ROOT / 'index.html', 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    all_links = soup.find_all('a', href=True)
    for link in all_links:
        href = link['href']
        if href.startswith('#'):
            target_id = href[1:]
            target = soup.find(id=target_id)
            assert target, f"Broken internal link: {href} - no element with id='{target_id}'"


def test_how_it_works_section():
    """Test that 'How It Works' section has steps"""
    with open(PROJECT_ROOT / 'index.html', 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    how_it_works = soup.find('section', id='how-it-works')
    assert how_it_works, "Missing 'How It Works' section"

    steps = how_it_works.find_all('div', class_='step')
    assert len(steps) >= 3, f"Expected at least 3 steps in 'How It Works', found {len(steps)}"
