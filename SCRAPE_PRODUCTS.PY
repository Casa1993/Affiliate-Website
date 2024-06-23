import requests
from bs4 import BeautifulSoup

def get_products():
    url = 'https://example.com/products'  # Vervang dit door de URL van de website die je wilt scrapen
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    products = []
    
    for product in soup.select('.product'):  # Pas de selector aan op basis van de website structuur
        name = product.select_one('.product-name').text
        description = product.select_one('.product-description').text
        link = product.select_one('.product-link')['href']
        products.append({
            'name': name,
            'description': description,
            'link': link
        })
    
    return products

if __name__ == '__main__':
    products = get_products()
    print(products)
