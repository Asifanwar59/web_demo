document.addEventListener('DOMContentLoaded', function() {
    // Scroll Reveal Animation with Intersection Observer
    const animatedElements = document.querySelectorAll('.animate-on-scroll');

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target); // Stop observing once visible
            }
        });
    }, {
        threshold: 0.2 // Trigger when 20% of the element is visible
    });

    animatedElements.forEach(element => {
        observer.observe(element);
    });
});
