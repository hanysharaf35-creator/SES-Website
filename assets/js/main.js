// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Navbar scroll effect
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.boxShadow = '0 5px 20px rgba(0,0,0,0.4)';
    } else {
        navbar.style.boxShadow = '0 2px 10px rgba(0,0,0,0.3)';
    }
});

// Language switcher (placeholder for future implementation)
document.addEventListener('DOMContentLoaded', function() {
    const langSwitcher = document.querySelector('.lang-switcher');
    if (langSwitcher) {
        langSwitcher.addEventListener('click', function() {
            // Will be implemented with backend
            alert('Arabic version coming soon!');
        });
    }
    
    // Mobile Burger Menu
    const burger = document.querySelector('.burger-menu');
    const navMenu = document.querySelector('.nav-menu');
    
    if (burger && navMenu) {
        burger.addEventListener('click', function() {
            burger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
        
        // Close menu when clicking on a link
        const navLinks = document.querySelectorAll('.nav-menu a');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                burger.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            const isClickInsideNav = navMenu.contains(event.target);
            const isClickOnBurger = burger.contains(event.target);
            
            if (!isClickInsideNav && !isClickOnBurger && navMenu.classList.contains('active')) {
                burger.classList.remove('active');
                navMenu.classList.remove('active');
            }
        });
    }
});
