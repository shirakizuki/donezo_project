// Mobile menu toggle
document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    document.getElementById('mobile-menu-button').addEventListener('click', function() {
        document.getElementById('mobile-menu').classList.toggle('hidden');
    });

    // Close mobile menu when a link is clicked
    document.querySelectorAll('#mobile-menu a').forEach(link => {
        link.addEventListener('click', function() {
            document.getElementById('mobile-menu').classList.add('hidden');
        });
    });

    // Smooth scrolling for all anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Navbar scroll behavior
    const navbar = document.querySelector('nav');
    const heroSection = document.getElementById('home');
    const heroHeight = heroSection.offsetHeight;

    window.addEventListener('scroll', function() {
        if (window.scrollY > heroHeight) {
            navbar.classList.add('bg-white', 'shadow-md');
            navbar.classList.remove('bg-transparent');
            // Change text color for all nav links
            document.querySelectorAll('nav a').forEach(link => {
                if (!link.classList.contains('bg-orange-400')) { // Don't change the login button
                    link.classList.add('text-gray-900');
                    link.classList.remove('text-white');
                }
            });
        } else {
            navbar.classList.remove('bg-white', 'shadow-md');
            navbar.classList.add('bg-transparent');
            // Change text color back for all nav links
            document.querySelectorAll('nav a').forEach(link => {
                if (!link.classList.contains('bg-orange-400')) { // Don't change the login button
                    link.classList.remove('text-gray-900');
                    link.classList.add('text-white');
                }
            });
        }
    });

    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-link');

    function updateActiveLink() {
        let currentSection = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (window.scrollY >= (sectionTop - sectionHeight/3)) {
                currentSection = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('text-orange-400');
            link.classList.add('text-black');
            if (link.getAttribute('href') === `#${currentSection}`) {
                link.classList.remove('text-white');
                link.classList.add('text-orange-400');
            }
        });
    }

    // Update on scroll
    window.addEventListener('scroll', updateActiveLink);
    
    // Update on page load
    updateActiveLink();

    // Testimonial carousel logic
    (function() {
        const cards = document.querySelectorAll('.testimonial-card');
        const users = document.querySelectorAll('.testimonial-user');
        const prevBtn = document.getElementById('testimonial-prev');
        const nextBtn = document.getElementById('testimonial-next');
        let current = 0;

        function showCard(idx) {
            cards.forEach((card, i) => {
                if (i === idx) {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });
            users.forEach((user, i) => {
                if (i === idx) {
                    user.classList.remove('opacity-50');
                    user.classList.add('opacity-100');
                    user.querySelector('.testimonial-underline').classList.remove('border-orange-200');
                    user.querySelector('.testimonial-underline').classList.add('border-orange-400');
                } else {
                    user.classList.remove('opacity-100');
                    user.classList.add('opacity-50');
                    user.querySelector('.testimonial-underline').classList.remove('border-orange-400');
                    user.querySelector('.testimonial-underline').classList.add('border-orange-200');
                }
            });
        }

        prevBtn && prevBtn.addEventListener('click', function() {
            current = (current - 1 + cards.length) % cards.length;
            showCard(current);
        });
        nextBtn && nextBtn.addEventListener('click', function() {
            current = (current + 1) % cards.length;
            showCard(current);
        });

        // Initialize
        showCard(current);
    })();
}); 