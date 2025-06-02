 // Core Functionality Preserved
 const form = document.getElementById('script-form');
 const submitBtn = document.getElementById('submit-btn');
 const loadingSpinner = document.getElementById('loading-spinner');
 const responseContainer = document.getElementById('response-container');

 // Auto-resize with cyberpunk effect
 function autoResize(textarea) {
     textarea.style.height = 'auto';
     textarea.style.height = textarea.scrollHeight + 'px';
     
     // Update character counter
     const counter = textarea.parentElement.querySelector('div');
     counter.textContent = `[CHAR: ${textarea.value.length}/500]`;
 }
 // Enhanced form submission
 form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Cyberpunk activation effect
    submitBtn.style.filter = 'hue-rotate(180deg)';
    loadingSpinner.classList.remove('hidden');
    responseContainer.classList.add('hidden');

    // Add CRT screen effect
    document.body.style.filter = 'contrast(110%) brightness(90%)';
    
    // Show loading text
    updateLoadingText();

    await new Promise(resolve => setTimeout(resolve, 1500));
    
    // Submit form normally
    form.submit();
 });

 function updateLoadingText() {
    const loadingText = document.getElementById('loading-text');
    let progress = 0;
    const interval = setInterval(() => {
        progress += 1;
        loadingText.textContent = `LOADING: ${progress}%`;
        if (progress >= 100) {
           clearInterval(interval);
        }
    }, 800); // Adjust the interval speed as needed
 }

 // Cyber copy feedback
 function copyToClipboard() {
     const text = document.querySelector('.glow-text').innerText;
     navigator.clipboard.writeText(text).then(() => {
         confetti({
             particleCount: 30,
             spread: 60,
             origin: { y: 0.5 },
             colors: ['#0ff', '#0f0']
         });
     });
 }

 // Initialize character counter
 document.querySelectorAll('textarea').forEach(autoResize);
