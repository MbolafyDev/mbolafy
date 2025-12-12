// dynamisation du progress bar
document.querySelectorAll('.progress-circle').forEach(circle => {
    const progress = circle.getAttribute('data-progress');
    circle.style.setProperty('--progress', progress);
});