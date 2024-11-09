// Toggle theme
document.getElementById('themeSwitch').addEventListener('change', function() {
    document.body.classList.toggle('light-theme');
    document.body.classList.toggle('dark-theme');
  });
  
  // Copy character to clipboard on click
  document.querySelectorAll('.character-box').forEach(box => {
    box.addEventListener('click', function() {
      const character = box.textContent.trim();
      navigator.clipboard.writeText(character).then(() => {
        // Show a brief confirmation message
        box.classList.add('copied');
        setTimeout(() => box.classList.remove('copied'), 800);
      }).catch(err => console.error('Failed to copy text: ', err));
    });
  });
  