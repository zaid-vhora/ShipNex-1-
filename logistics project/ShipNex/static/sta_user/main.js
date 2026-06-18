/**
 * Shipnex - Main JavaScript
 * Common functionality across all pages
 */

document.addEventListener('DOMContentLoaded', function() {
  // ============================================
  // HEADER SCROLL EFFECT
  // ============================================
  const header = document.getElementById('header');
  let lastScroll = 0;

  if (header) {
    window.addEventListener('scroll', () => {
      const currentScroll = window.scrollY;

      if (currentScroll > 50) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }

      lastScroll = currentScroll;
    });
  }

  // ============================================
  // MOBILE MENU TOGGLE
  // ============================================
  const mobileMenuToggle = document.getElementById('mobileMenuToggle');
  const mobileMenu = document.getElementById('mobileMenu');

  if (mobileMenuToggle && mobileMenu) {
    mobileMenuToggle.addEventListener('click', () => {
      mobileMenuToggle.classList.toggle('active');
      mobileMenu.classList.toggle('active');
      document.body.classList.toggle('menu-open');
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
      if (!mobileMenu.contains(e.target) && !mobileMenuToggle.contains(e.target)) {
        mobileMenuToggle.classList.remove('active');
        mobileMenu.classList.remove('active');
        document.body.classList.remove('menu-open');
      }
    });

    // Close menu when clicking on a link
    const mobileLinks = mobileMenu.querySelectorAll('.mobile-menu-link');
    mobileLinks.forEach(link => {
      link.addEventListener('click', () => {
        mobileMenuToggle.classList.remove('active');
        mobileMenu.classList.remove('active');
        document.body.classList.remove('menu-open');
      });
    });
  }

  // ============================================
  // SMOOTH SCROLL FOR ANCHOR LINKS
  // ============================================
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href !== '#') {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      }
    });
  });

  // ============================================
  // ANIMATION ON SCROLL
  // ============================================
  const animateOnScroll = () => {
    const elements = document.querySelectorAll('.service-card, .feature-item, .testimonial-card, .about-image, .about-content');

    elements.forEach(element => {
      const elementTop = element.getBoundingClientRect().top;
      const elementBottom = element.getBoundingClientRect().bottom;
      const windowHeight = window.innerHeight;

      if (elementTop < windowHeight - 100 && elementBottom > 0) {
        element.classList.add('animate-visible');
      }
    });
  };

  window.addEventListener('scroll', animateOnScroll);
  animateOnScroll(); // Initial check

  // ============================================
  // FORM VALIDATION HELPERS
  // ============================================
  const forms = document.querySelectorAll('form');

  forms.forEach(form => {
    const inputs = form.querySelectorAll('input, textarea, select');

    inputs.forEach(input => {
      // Add blur validation
      input.addEventListener('blur', function() {
        if (this.required && !this.value.trim()) {
          this.classList.add('error');
        } else {
          this.classList.remove('error');
        }
      });

      // Remove error on focus
      input.addEventListener('focus', function() {
        this.classList.remove('error');
      });
    });
  });

  // ============================================
  // TRACKING FORM (if on tracking page)
  // ============================================
  const trackingForm = document.getElementById('trackingForm');
  const trackingResult = document.getElementById('trackingResult');

  if (trackingForm && trackingResult) {
    trackingForm.addEventListener('submit', function(e) {
      e.preventDefault();
      const trackingNum = document.getElementById('trackingNumber').value;

      if (trackingNum) {
        trackingResult.classList.add('show');
        trackingResult.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  }

  // ============================================
  // CONTACT FORM (if on contact page)
  // ============================================
  const contactForm = document.getElementById('contactForm');

  if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
      e.preventDefault();

      // Simple form validation
      const firstName = document.getElementById('firstName')?.value;
      const lastName = document.getElementById('lastName')?.value;
      const email = document.getElementById('email')?.value;
      const phone = document.getElementById('phone')?.value;
      const message = document.getElementById('message')?.value;

      if (!firstName || !lastName || !email || !phone || !message) {
        alert('Please fill in all required fields.');
        return;
      }

      // Email validation
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        alert('Please enter a valid email address.');
        return;
      }

      alert('Thank you for your message! We will get back to you within 24 hours.');
      this.reset();
    });
  }

  // ============================================
  // TESTIMONIAL CARDS ANIMATION
  // ============================================
  const testimonialCards = document.querySelectorAll('.testimonial-card');

  if (testimonialCards.length > 0) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
          setTimeout(() => {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
          }, index * 150);
        }
      });
    }, { threshold: 0.2 });

    testimonialCards.forEach(card => {
      card.style.opacity = '0';
      card.style.transform = 'translateY(30px)';
      card.style.transition = 'all 0.6s ease';
      observer.observe(card);
    });
  }

  // ============================================
  // BUTTON RIPPLE EFFECT
  // ============================================
  const buttons = document.querySelectorAll('.btn');

  buttons.forEach(button => {
    button.addEventListener('click', function(e) {
      const ripple = document.createElement('span');
      ripple.classList.add('ripple');

      const rect = this.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      ripple.style.left = `${x}px`;
      ripple.style.top = `${y}px`;

      this.appendChild(ripple);

      setTimeout(() => {
        ripple.remove();
      }, 600);
    });
  });

  // ============================================
  // PARTICLES EFFECT FOR HERO
  // ============================================
  const heroSection = document.querySelector('.hero');
  const heroParticles = document.querySelector('.hero-particles');

  if (heroSection && heroParticles) {
    // Create particles
    for (let i = 0; i < 20; i++) {
      const particle = document.createElement('div');
      particle.classList.add('hero-particle');
      particle.style.left = `${Math.random() * 100}%`;
      particle.style.animationDelay = `${Math.random() * 20}s`;
      particle.style.animationDuration = `${15 + Math.random() * 10}s`;
      heroParticles.appendChild(particle);
    }
  }

  // ============================================
  // YEAR UPDATE IN FOOTER
  // ============================================
  const yearElement = document.querySelector('.footer-bottom p');
  if (yearElement) {
    const currentYear = new Date().getFullYear();
    yearElement.innerHTML = yearElement.innerHTML.replace(/2024/, currentYear);
  }

  // ============================================
  // KEYBOARD NAVIGATION
  // ============================================
  document.addEventListener('keydown', (e) => {
    // ESC key closes mobile menu
    if (e.key === 'Escape') {
      if (mobileMenuToggle && mobileMenu) {
        mobileMenuToggle.classList.remove('active');
        mobileMenu.classList.remove('active');
        document.body.classList.remove('menu-open');
      }
    }
  });

  // ============================================
  // PRELOADER (optional)
  // ============================================
  window.addEventListener('load', () => {
    document.body.classList.add('loaded');
  });
});

// ============================================
// UTILITY FUNCTIONS
// ============================================

// Debounce function for scroll events
function debounce(func, wait = 20, immediate = true) {
  let timeout;
  return function() {
    const context = this, args = arguments;
    const later = function() {
      timeout = null;
      if (!immediate) func.apply(context, args);
    };
    const callNow = immediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
    if (callNow) func.apply(context, args);
  };
}

// Throttle function for resize events
function throttle(func, limit) {
  let inThrottle;
  return function() {
    const args = arguments;
    const context = this;
    if (!inThrottle) {
      func.apply(context, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}

// Add CSS for ripple effect dynamically
const style = document.createElement('style');
style.textContent = `
  .btn {
    position: relative;
    overflow: hidden;
  }

  .ripple {
    position: absolute;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.4);
    transform: scale(0);
    animation: ripple-animation 0.6s linear;
    pointer-events: none;
    width: 10px;
    height: 10px;
    margin-left: -5px;
    margin-top: -5px;
  }

  @keyframes ripple-animation {
    to {
      transform: scale(20);
      opacity: 0;
    }
  }

  .form-input.error,
  .form-textarea.error,
  .form-select.error {
    border-color: #eb1535 !important;
    box-shadow: 0 0 0 4px rgba(235, 21, 53, 0.1) !important;
  }

  .animate-visible {
    opacity: 1 !important;
    transform: translateY(0) !important;
  }

  body.menu-open {
    overflow: hidden;
  }

  body.loaded .preloader {
    opacity: 0;
    pointer-events: none;
  }
`;
document.head.appendChild(style);
