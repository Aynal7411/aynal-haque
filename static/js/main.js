/**
 * AYNAL'S SOLUTIONS - Main JavaScript
 * Navigation, interactions, and enhancements
 */

// ============================================================
// NAVBAR SCROLL DETECTION
// ============================================================

const navbar = document.getElementById('navbar');
const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
const navbarMenu = document.getElementById('navbar-menu');

// Detect scroll and update navbar style
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

// Mobile menu toggle
if (mobileMenuToggle) {
  mobileMenuToggle.addEventListener('click', () => {
    navbarMenu.classList.toggle('active');
  });
}

// Close mobile menu when a link is clicked
const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
  link.addEventListener('click', () => {
    navbarMenu.classList.remove('active');
  });
});

// ============================================================
// SMOOTH SCROLL TO SECTIONS
// ============================================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const href = this.getAttribute('href');
    
    // Skip if href is just "#"
    if (href === '#') return;
    
    e.preventDefault();
    
    const target = document.querySelector(href);
    if (target) {
      const headerOffset = 80; // navbar height
      const elementPosition = target.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
      
      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      });
    }
  });
});

// ============================================================
// API PLAYGROUND INTERACTION
// ============================================================

const tryButton = document.querySelector('.playground-action .btn-primary');
const copyButton = document.querySelector('.playground-action .btn-secondary');

if (tryButton) {
  tryButton.addEventListener('click', () => {
    // Show a simple success message
    const originalText = tryButton.textContent;
    tryButton.textContent = '✓ Request Sent!';
    tryButton.style.pointerEvents = 'none';
    
    setTimeout(() => {
      tryButton.textContent = originalText;
      tryButton.style.pointerEvents = 'auto';
    }, 2000);
  });
}

if (copyButton) {
  copyButton.addEventListener('click', () => {
    const curlCommand = 'curl -X GET "https://api.aynalsolutions.com/api/v1/solutions/" \\\n' +
      '  -H "Authorization: Bearer eyJhbGc..."';
    
    navigator.clipboard.writeText(curlCommand).then(() => {
      const originalText = copyButton.textContent;
      copyButton.textContent = '✓ Copied!';
      
      setTimeout(() => {
        copyButton.textContent = originalText;
      }, 2000);
    });
  });
}

// ============================================================
// FORM HANDLING
// ============================================================

const contactForm = document.querySelector('.contact-form form');

if (contactForm) {
  contactForm.addEventListener('submit', function (e) {
    e.preventDefault();
    
    // Simple form validation
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const projectType = document.getElementById('project-type').value;
    const budget = document.getElementById('budget').value;
    const description = document.getElementById('description').value.trim();
    
    if (!name || !email || !projectType || !budget || !description) {
      alert('Please fill in all fields.');
      return;
    }
    
    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      alert('Please enter a valid email address.');
      return;
    }
    
    // Show success message
    const submitButton = this.querySelector('button[type="submit"]');
    const originalText = submitButton.textContent;
    
    submitButton.disabled = true;
    submitButton.textContent = 'Sending...';
    
    // Simulate form submission
    setTimeout(() => {
      submitButton.textContent = '✓ Message Sent!';
      
      // Reset form after 2 seconds
      setTimeout(() => {
        contactForm.reset();
        submitButton.textContent = originalText;
        submitButton.disabled = false;
      }, 2000);
    }, 1000);
  });
}

// ============================================================
// INTERSECTION OBSERVER FOR ANIMATIONS
// ============================================================

// Animate elements as they come into view
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver(function (entries) {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.animation = 'fadeInUp 0.6s ease-out forwards';
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

// Observe cards and sections
document.querySelectorAll('.expertise-card, .service-card, .project-card, .value-item').forEach(el => {
  el.style.opacity = '0';
  observer.observe(el);
});

// ============================================================
// KEYBOARD NAVIGATION
// ============================================================

// Ensure all interactive elements are keyboard accessible
document.addEventListener('keydown', (e) => {
  // Escape key closes mobile menu
  if (e.key === 'Escape' && navbarMenu.classList.contains('active')) {
    navbarMenu.classList.remove('active');
  }
});

// ============================================================
// ACCESSIBILITY ENHANCEMENTS
// ============================================================

// Ensure focus management
navLinks.forEach(link => {
  link.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      link.click();
    }
  });
});

// ============================================================
// LAZY LOAD IMAGES (if used)
// ============================================================

if ('IntersectionObserver' in window) {
  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        if (img.dataset.src) {
          img.src = img.dataset.src;
          img.removeAttribute('data-src');
          imageObserver.unobserve(img);
        }
      }
    });
  });

  document.querySelectorAll('img[data-src]').forEach(img => {
    imageObserver.observe(img);
  });
}

// ============================================================
// PREFERS REDUCED MOTION SUPPORT
// ============================================================

const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (prefersReducedMotion) {
  // Disable smooth scroll for users who prefer reduced motion
  document.documentElement.style.scrollBehavior = 'auto';
}

// ============================================================
// ANALYTICS & TRACKING (Optional - Add your tracking code here)
// ============================================================

// Track page views
console.log('Aynal\'s Solutions website loaded successfully');

// Track button clicks
document.querySelectorAll('.btn').forEach(btn => {
  btn.addEventListener('click', function () {
    // Add your analytics tracking here
    const buttonText = this.textContent.trim();
    console.log('Button clicked:', buttonText);
  });
});
