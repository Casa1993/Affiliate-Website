document.addEventListener('DOMContentLoaded', () => {
    const products = [
        { name: 'Product 1', description: 'Description 1', link: 'https://affiliate-link1.com' },
        { name: 'Product 2', description: 'Description 2', link: 'https://affiliate-link2.com' },
        { name: 'Product 3', description: 'Description 3', link: 'https://affiliate-link3.com' }
    ];

    const productList = document.getElementById('product-list');
    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.className = 'product';
        productDiv.innerHTML = `
            <h3>${product.name}</h3>
            <p>${product.description}</p>
            <a href="${product.link}" target="_blank">Buy Now</a>
        `;
        productList.appendChild(productDiv);
    });
});
