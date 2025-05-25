document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.btn');

    buttons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const productName = btn.closest('.card-body').querySelector('.card-title').textContent;
            alert(`Has agregado "${productName}" al carrito.`);
        });
    });
});