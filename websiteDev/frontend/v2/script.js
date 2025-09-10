document.addEventListener('DOMContentLoaded', () => {
    const cube = document.querySelector('.cube');
    let isDragging = false;
    let startX, startY;
    let rotationX = -20;
    let rotationY = 20;

    // Optional: Stop the CSS animation on mouse down to take over with JS
    cube.addEventListener('mousedown', (e) => {
        isDragging = true;
        startX = e.clientX;
        startY = e.clientY;
        cube.style.animationPlayState = 'paused';
    });

    // Handle mouse movement for rotation
    document.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        const deltaX = (e.clientX - startX) * 0.5;
        const deltaY = (e.clientY - startY) * 0.5;
        rotationY += deltaX;
        rotationX -= deltaY;

        cube.style.transform = `rotateX(${rotationX}deg) rotateY(${rotationY}deg)`;
        startX = e.clientX;
        startY = e.clientY;
    });

    // Release drag
    document.addEventListener('mouseup', () => {
        isDragging = false;
    });
});
