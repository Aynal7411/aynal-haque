/**
 * HOMEPAGE SPECIFIC INTERACTIONS
 */

document.addEventListener('DOMContentLoaded', function () {
  
  // ============================================================
  // CODE ANIMATION IN HERO
  // ============================================================
  
  const codeLines = document.querySelectorAll('.code-line');
  
  function animateCodeLines() {
    codeLines.forEach((line, index) => {
      line.style.opacity = '0';
      line.style.animation = `slideInLeft 0.3s ease-out ${index * 0.1}s forwards`;
    });
  }
  
  // Animate code when page loads
  if (codeLines.length > 0) {
    animateCodeLines();
  }
  
  // ============================================================
  // HERO EYEBROW PULSE
  // ============================================================
  
  const statusIndicator = document.querySelector('.status-indicator');
  if (statusIndicator) {
    // Status indicator already has CSS animation
    // This is just for reference
  }
  
  // ============================================================
  // EXPERTISE CARDS HOVER EFFECT
  // ============================================================
  
  const expertiseCards = document.querySelectorAll('.expertise-card');
  
  expertiseCards.forEach(card => {
    card.addEventListener('mouseenter', function () {
      // Get the icon element
      const icon = this.querySelector('.expertise-icon');
      if (icon) {
        icon.style.animation = 'bounce 0.6s ease-in-out';
      }
    });
    
    card.addEventListener('animationend', function (e) {
      if (e.animationName === 'bounce') {
        e.target.style.animation = '';
      }
    });
  });
  
  // ============================================================
  // SERVICE CARDS NUMBER COUNTER
  // ============================================================
  
  const serviceCards = document.querySelectorAll('.service-card');
  let serviceCounterAnimated = false;
  
  const serviceObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !serviceCounterAnimated) {
        serviceCounterAnimated = true;
        serviceCards.forEach((card, index) => {
          const numberEl = card.querySelector('.service-number');
          if (numberEl) {
            numberEl.style.animation = `pulse 0.6s ease-out ${index * 0.1}s forwards`;
          }
        });
      }
    });
  }, { threshold: 0.1 });
  
  const servicesSection = document.getElementById('services');
  if (servicesSection) {
    serviceObserver.observe(servicesSection);
  }
  
  // ============================================================
  // PROCESS TIMELINE ANIMATION
  // ============================================================
  
  const processSteps = document.querySelectorAll('.process-step');
  let processAnimated = false;
  
  const processObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !processAnimated) {
        processAnimated = true;
        processSteps.forEach((step, index) => {
          step.style.animation = `slideInUp 0.5s ease-out ${index * 0.15}s forwards`;
          step.style.opacity = '0';
        });
      }
    });
  }, { threshold: 0.2 });
  
  const processSection = document.getElementById('process');
  if (processSection) {
    processObserver.observe(processSection);
  }
  
  // ============================================================
  // JSON SYNTAX HIGHLIGHTING IN PLAYGROUND
  // ============================================================
  
  const jsonLines = document.querySelectorAll('.json-line');
  
  jsonLines.forEach(line => {
    // Already styled in CSS, but we can add animation
    line.style.animation = `slideInLeft 0.4s ease-out backwards`;
  });
  
  // ============================================================
  // TECH STRIP ANIMATION
  // ============================================================
  
  const techCores = document.querySelectorAll('.tech-core');
  
  techCores.forEach((tech, index) => {
    tech.style.animation = `fadeIn 0.5s ease-out ${index * 0.1}s forwards`;
    tech.style.opacity = '0';
  });
  
  // ============================================================
  // ABOUT VALUES GRID STAGGER
  // ============================================================
  
  const valueItems = document.querySelectorAll('.value-item');
  let valueAnimated = false;
  
  const aboutObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !valueAnimated) {
        valueAnimated = true;
        valueItems.forEach((item, index) => {
          item.style.animation = `fadeInScale 0.5s ease-out ${index * 0.12}s forwards`;
          item.style.opacity = '0';
        });
      }
    });
  }, { threshold: 0.1 });
  
  const aboutSection = document.getElementById('about');
  if (aboutSection) {
    aboutObserver.observe(aboutSection);
  }
  
  // ============================================================
  // ACTIVE SECTION IN NAVBAR
  // ============================================================
  
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');
  
  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const activeId = entry.target.id;
        
        navLinks.forEach(link => {
          link.classList.remove('active');
          
          if (link.getAttribute('href') === `#${activeId}`) {
            link.classList.add('active');
          }
        });
      }
    });
  }, {
    threshold: 0.3
  });
  
  sections.forEach(section => {
    sectionObserver.observe(section);
  });
  
  // ============================================================
  // ADD ANIMATIONS TO KEYFRAMES
  // ============================================================
  
  // Create and inject animations if not in CSS
  if (!document.querySelector('style[data-animations]')) {
    const style = document.createElement('style');
    style.setAttribute('data-animations', 'true');
    style.textContent = `
      @keyframes slideInLeft {
        from {
          opacity: 0;
          transform: translateX(-20px);
        }
        to {
          opacity: 1;
          transform: translateX(0);
        }
      }
      
      @keyframes slideInUp {
        from {
          opacity: 0;
          transform: translateY(20px);
        }
        to {
          opacity: 1;
          transform: translateY(0);
        }
      }
      
      @keyframes fadeIn {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }
      
      @keyframes fadeInScale {
        from {
          opacity: 0;
          transform: scale(0.95);
        }
        to {
          opacity: 1;
          transform: scale(1);
        }
      }
      
      @keyframes fadeInUp {
        from {
          opacity: 0;
          transform: translateY(10px);
        }
        to {
          opacity: 1;
          transform: translateY(0);
        }
      }
      
      @keyframes bounce {
        0%, 100% {
          transform: translateY(0);
        }
        50% {
          transform: translateY(-10px);
        }
      }
      
      @keyframes pulse {
        0%, 100% {
          opacity: 1;
        }
        50% {
          opacity: 0.7;
        }
      }
    `;
    document.head.appendChild(style);
  }
  
  // ============================================================
  // HERO TITLE ANIMATION
  // ============================================================
  
  const heroTitle = document.querySelector('.hero h1');
  if (heroTitle) {
    heroTitle.style.animation = 'slideInUp 0.8s ease-out';
  }
  
  const heroDescription = document.querySelector('.hero-description');
  if (heroDescription) {
    heroDescription.style.animation = 'slideInUp 0.8s ease-out 0.2s forwards';
    heroDescription.style.opacity = '0';
  }
  
  const heroCTA = document.querySelector('.hero-cta');
  if (heroCTA) {
    heroCTA.style.animation = 'slideInUp 0.8s ease-out 0.4s forwards';
    heroCTA.style.opacity = '0';
  }
  
  const heroVisual = document.querySelector('.hero-visual');
  if (heroVisual) {
    heroVisual.style.animation = 'slideInUp 0.8s ease-out 0.6s forwards';
    heroVisual.style.opacity = '0';
  }
});
