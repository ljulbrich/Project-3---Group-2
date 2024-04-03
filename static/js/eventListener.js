const inputElement = document.getElementById("long-term-price-ticker");
inputElement.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        const inputQuery = document.getElementById('long-term-price-ticker').value;
        if (inputQuery) {
            window.location.href = `/long-term-price/${inputQuery}`;
        }
    }
});
