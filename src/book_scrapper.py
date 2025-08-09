import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

from ftfy import fix_text
import unicodedata




BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
BASE_SITE = "http://books.toscrape.com/catalogue/"

books = []

for page in range(1, 51):  # Loop through all 50 pages
    print(f"Scraping page {page}...")
    url = BASE_URL.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for book in soup.find_all("article", class_="product_pod"):
        # Basic info from listing page
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        rating = book.p["class"][1]  
        
        # Book detail page link
        book_url = BASE_SITE + book.h3.a["href"].replace('../../../', '')
        book_resp = requests.get(book_url)
        book_soup = BeautifulSoup(book_resp.text, 'html.parser')

        # Category
        category = book_soup.find("ul", class_="breadcrumb").find_all("li")[2].text.strip()

        # Product description
        desc_tag = book_soup.find("div", id="product_description")
        description = desc_tag.find_next_sibling("p").text.strip() if desc_tag else ""

        # Table info (UPC, stock)
        table_rows = book_soup.find("table", class_="table table-striped").find_all("tr")
        upc = table_rows[0].find("td").text.strip()
        stock_text = table_rows[5].find("td").text.strip()
        
        # Extract stock number (e.g., "In stock (22 available)")
        stock_count = ''.join([c for c in stock_text if c.isdigit()])

        # Availability (from list page, cleaned)
        availability = book.find("p", class_="instock availability").text.strip()

        books.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Stock Count": stock_count,
            "Rating": rating,
            "Category": category,
            "UPC": upc,
            "Description": description
        })

        time.sleep(0.2)  # short delay for detail page requests

    time.sleep(1)  # delay for page requests

# Save to CSV
df = pd.DataFrame(books)
df.to_csv("../scraped_data/books_detailed_dataset.csv", index=False, encoding="utf-8")
print("Scraping complete! Data saved to books_detailed_dataset.csv")

# preprocessing da
# Cleaning the description column value text data and the price column
df["PriceGBP"] = (
    df["Price"]
      .astype(str)
      .str.replace("\xa0", " ", regex=False)                  # kill NBSP
      .str.encode("latin1", "ignore").str.decode("utf-8", "ignore")  # Â£ -> £
      .str.replace(",", "", regex=False)                      # remove thousand sep if any
      .str.replace(r"[^\d.\-]", "", regex=True)               # drop £ and any other symbols
      .replace("", pd.NA)
      .astype(float)
)

def basic_clean(s):
    if not isinstance(s, str):
        return ""
    s = fix_text(s)                         # fix encoding issues
    s = unicodedata.normalize("NFKC", s)    # normalize unicode (quotes, spaces, etc.)
    s = s.replace("\xa0", " ")              # convert non-breaking spaces to normal spaces
    s = re.sub(r"\s+", " ", s).strip()      # collapse multiple spaces
    return s

df["Description_clean"] = df["Description"].apply(basic_clean)