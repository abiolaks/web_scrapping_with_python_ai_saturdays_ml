# web_scrapping_with_python_ai_saturdays_ml
# List of Data project for Ml Use Case

## 1. Scraping Books

## Books to Scrape Dataset Documentation

### Overview
This dataset was collected from the [Books to Scrape](https://books.toscrape.com/) website, an open practice site for web scraping.  
It contains information about all books listed on the site (50 pages in total), including pricing, availability, ratings, and detailed metadata.  
This dataset is suitable for various Machine Learning (ML) and Data Analysis tasks such as price prediction, rating classification, and category-based recommendation systems.

---

### Dataset Details

- **Source:** [Books to Scrape](https://books.toscrape.com/)
- **Pages Scraped:** 50 (all available pages)
- **Number of Records:** 1,000 books
- **Scraping Method:** Python `requests` + `BeautifulSoup`
- **File Format:** CSV (`books_dataset.csv`)

---

###  Columns & Descriptions

| Column Name       | Description |
|-------------------|-------------|
| `title`           | The title of the book |
| `price`           | Price of the book in GBP (£) |
| `availability`    | Stock availability status (e.g., "In stock (22 available)") |
| `rating`          | Star rating of the book (1 to 5 stars) |
| `category`        | The genre/category the book belongs to |
| `product_description` | A short description or synopsis of the book |
| `upc`             | Unique Product Code for the book |
| `stock_count`     | Number of copies available in stock |

---

### Potential ML Use Cases

1. **Price Prediction** – Predict book prices based on category, rating, and other features.  
2. **Rating Classification** – Classify books into star ratings using metadata.  
3. **Recommendation System** – Suggest books to users based on categories and descriptions.  
4. **Category Prediction** – Predict the category of a book using its title and description.  

---

### 🛠 Tools Used

- **Python Libraries:**  
  - `requests` – for sending HTTP requests to fetch page HTML  
  - `BeautifulSoup` – for parsing HTML and extracting data  
  - `csv` / `pandas` – for saving the dataset into CSV format  

---

###  License & Disclaimer
This dataset was scraped from an **open practice website** created for educational purposes.  
It does not violate any terms of service and is intended solely for **learning and non-commercial use**.

2.
