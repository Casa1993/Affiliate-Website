import json
from scrape_products import get_products

def select_best_products(products):
    # Eenvoudig regelsysteem, later vervangen door meer geavanceerde AI
    selected_products = []
    for product in products:
        if 'criteria' in product['description']:  # Voeg je selectiecriteria hier toe
            selected_products.append(product)
    return selected_products

def update_app_js(products):
    js_code = f"""
document.addEventListener('DOMContentLoaded', () => {{
    const products = {json.dumps(products)};
    const productList = document.getElementById('product-list');
    products.forEach(product => {{
        const productDiv = document.createElement('div');
        productDiv.className = 'product';
        productDiv.innerHTML = `
            <h3>\${{product['name']}}</h3>
            <p>\${{product['description']}}</p>
            <a href="\${{product['link']}}" target="_blank">Buy Now</a>
        `;
        productList.appendChild(productDiv);
    }});
}});
    """
    with open('app.js', 'w') as file:
        file.write(js_code)

if __name__ == '__main__':
    products = get_products()
    selected_products = select_best_products(products)
    update_app_js(selected_products)
