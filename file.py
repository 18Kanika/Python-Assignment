import requests
from bs4 import BeautifulSoup

# Set the number of pages to scrape
num_pages = 20

# Define the base URL for the Amazon search
base_url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2F&ref=sr_pg_{}"

# Initialize lists to store scraped data
product_data = []

# Loop through each page
for page in range(1, num_pages + 1):
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all product containers
    product_containers = soup.find_all("div", class_="s-result-item")

    # Extract product information
    for container in product_containers:
        product_info = {}
        
        # Extract product URL
        product_link = container.find("a", class_="a-link-normal")
        if product_link:
            product_info["url"] = "https://www.amazon.in" + product_link.get("href")
        
        # Extract product name
        product_name = container.find("span", class_="a-text-normal")
        if product_name:
            product_info["name"] = product_name.get_text()
        
        # Extract product price
        product_price = container.find("span", class_="a-offscreen")
        if product_price:
            product_info["price"] = product_price.get_text()
        
        # Extract product rating
        product_rating = container.find("span", class_="a-icon-alt")
        if product_rating:
            product_info["rating"] = product_rating.get_text()
        
        # Extract number of reviews
        num_reviews = container.find("span", {"aria-label": "ratings"})
        if num_reviews:
            product_info["num_reviews"] = num_reviews.get_text()
        
        product_data.append(product_info)

for product in product_data:
    print(product)