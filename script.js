// Dark Mode Toggle
const darkModeToggle = document.getElementById('dark-mode-toggle');
const html = document.documentElement;

// Check for saved theme preference or default to light mode
const currentTheme = localStorage.getItem('theme') || 'light';
html.setAttribute('data-theme', currentTheme);

darkModeToggle.addEventListener('click', () => {
    const currentTheme = html.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';

    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
});

// Smooth Scroll for Navigation Links
const navLinks = document.querySelectorAll('.nav-link');

navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = link.getAttribute('href');
        const targetSection = document.querySelector(targetId);

        if (targetSection) {
            const navHeight = document.querySelector('.navbar').offsetHeight;
            const targetPosition = targetSection.offsetTop - navHeight;

            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// Card Expand/Collapse Functionality
const useCaseCards = document.querySelectorAll('.use-case-card');

useCaseCards.forEach(card => {
    const expandButton = card.querySelector('.expand-button');

    expandButton.addEventListener('click', (e) => {
        e.stopPropagation();

        // Close all other cards
        useCaseCards.forEach(otherCard => {
            if (otherCard !== card && otherCard.classList.contains('expanded')) {
                otherCard.classList.remove('expanded');
            }
        });

        // Toggle current card
        card.classList.toggle('expanded');
    });

    // Also allow clicking the card itself to expand (except when clicking links)
    card.addEventListener('click', (e) => {
        if (e.target.tagName !== 'A' && !e.target.closest('.expand-button')) {
            // Close all other cards
            useCaseCards.forEach(otherCard => {
                if (otherCard !== card && otherCard.classList.contains('expanded')) {
                    otherCard.classList.remove('expanded');
                }
            });

            // Toggle current card
            card.classList.toggle('expanded');
        }
    });
});

// Intersection Observer for Scroll Animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            // Optional: Stop observing after animation triggers
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe all elements with fade-in-up class
const animatedElements = document.querySelectorAll('.fade-in-up');
animatedElements.forEach(element => {
    observer.observe(element);
});

// Smooth CTA Button Scroll
const ctaButton = document.querySelector('.cta-button');

if (ctaButton) {
    ctaButton.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = ctaButton.getAttribute('href');
        const targetSection = document.querySelector(targetId);

        if (targetSection) {
            const navHeight = document.querySelector('.navbar').offsetHeight;
            const targetPosition = targetSection.offsetTop - navHeight;

            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
}

// Add active state to nav links based on scroll position
const sections = document.querySelectorAll('section[id]');

function highlightNavOnScroll() {
    const scrollPosition = window.scrollY + 100;

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;
        const sectionId = section.getAttribute('id');

        if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${sectionId}`) {
                    link.classList.add('active');
                }
            });
        }
    });
}

window.addEventListener('scroll', highlightNavOnScroll);

// Close expanded cards when clicking outside
document.addEventListener('click', (e) => {
    if (!e.target.closest('.use-case-card')) {
        useCaseCards.forEach(card => {
            card.classList.remove('expanded');
        });
    }
});

// Close expanded cards on Escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        useCaseCards.forEach(card => {
            card.classList.remove('expanded');
        });
    }
});

// Add keyboard navigation for cards
useCaseCards.forEach((card, index) => {
    card.setAttribute('tabindex', '0');

    card.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();

            // Close all other cards
            useCaseCards.forEach(otherCard => {
                if (otherCard !== card && otherCard.classList.contains('expanded')) {
                    otherCard.classList.remove('expanded');
                }
            });

            // Toggle current card
            card.classList.toggle('expanded');
        }

        // Arrow key navigation
        if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
            e.preventDefault();
            const nextCard = useCaseCards[index + 1] || useCaseCards[0];
            nextCard.focus();
        }

        if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
            e.preventDefault();
            const prevCard = useCaseCards[index - 1] || useCaseCards[useCaseCards.length - 1];
            prevCard.focus();
        }
    });
});

// Performance optimization: Debounce scroll events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

const debouncedScrollHandler = debounce(highlightNavOnScroll, 100);
window.addEventListener('scroll', debouncedScrollHandler);

// Add animation to metrics when they come into view
const metricElements = document.querySelectorAll('.metric-value');

const metricObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            // Add a subtle animation to the metric
            entry.target.style.animation = 'fadeIn 0.6s ease-out forwards';
            metricObserver.unobserve(entry.target);
        }
    });
}, observerOptions);

metricElements.forEach(element => {
    metricObserver.observe(element);
});

// Console message
console.log('%cAlphaFold Use Case Explorer', 'font-size: 24px; font-weight: bold; background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;');
console.log('%cExploring the frontiers of digital biology', 'font-size: 14px; color: #718096;');
console.log('%cSource: https://github.com/serenakeyitan/alphafold-use-case-explorer', 'font-size: 12px; color: #3b82f6;');
