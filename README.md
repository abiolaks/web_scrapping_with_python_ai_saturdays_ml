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


# 2. IMDB Movies Dataset Documentation

## Overview
This dataset was scraped from [IMDB](https://www.imdb.com/) and contains information about movies, including their titles, genres, ratings, summaries, and more.  
It can be used for various **Machine Learning (ML)** and **Data Analysis** tasks, such as:
- Recommendation systems
- Sentiment analysis
- Popularity prediction
- Genre classification
- Trend analysis

---

## Data Fields
| Column Name       | Description                                                                                  | Example                                                                 |
|-------------------|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `title`           | Name of the movie                                                                            | *The Shawshank Redemption*                                             |
| `year`            | Release year of the movie                                                                    | `1994`                                                                  |
| `genre`           | Movie genres, separated by commas                                                            | *Drama, Crime*                                                          |
| `rating`          | IMDb user rating (0.0 to 10.0)                                                                | `9.3`                                                                   |
| `votes`           | Number of user votes                                                                         | `2,700,000`                                                             |
| `summary`         | Short plot summary or description of the movie                                               | *Two imprisoned men bond over a number of years...*                     |
| `duration`        | Length of the movie                                                                          | `142 min`                                                               |
| `director`        | Name(s) of the movie director(s)                                                             | *Frank Darabont*                                                        |
| `stars`           | Main cast of the movie                                                                       | *Tim Robbins, Morgan Freeman, Bob Gunton*                               |
| `gross_income`    | Gross box office earnings (if available)                                                     | `$28,341,469`                                                           |
| `metascore`       | Metacritic score of the movie (if available)                                                 | `80`                                                                    |

---

## Data Source
- **Website**: [IMDB](https://www.imdb.com/)
- **Scraping Method**: BeautifulSoup (Python)
- **License**: For educational and research purposes only.  
  Data must be used in compliance with IMDb’s terms of service.

---

## Possible Use Cases
1. **Movie Recommendation System** – Suggest movies based on user ratings, genres, and preferences.
2. **Popularity Prediction** – Predict a movie’s success using ratings, votes, and box office data.
3. **Sentiment Analysis** – Analyze movie summaries or reviews for sentiment trends.
4. **Genre Classification** – Train models to automatically assign genres to new movies.
5. **Trend Analysis** – Study changes in genres, ratings, and themes over time.

---

## Example Row
| title                      | year | genre         | rating | votes     | summary                                      | duration | director       | stars                                    | gross_income  | metascore |
|----------------------------|------|---------------|--------|-----------|----------------------------------------------|----------|----------------|-------------------------------------------|---------------|-----------|
| The Shawshank Redemption   | 1994 | Drama, Crime  | 9.3    | 2700000   | Two imprisoned men bond over a number of... | 142 min  | Frank Darabont | Tim Robbins, Morgan Freeman, Bob Gunton   | $28,341,469   | 80        |

---

## Notes
- Missing data fields (e.g., `gross_income` or `metascore`) are represented as `NaN` or left blank.
- Currency for gross income is in USD.
- Genre values are comma-separated strings for multi-genre films.

---

# 3 Nigeria Cities Weather Dataset (OpenWeatherMap API)

##  Overview
This dataset contains real-time weather information for **major cities in Nigeria**, collected using the **[OpenWeatherMap API](https://openweathermap.org/api)**.  
It can be used for **machine learning**, **data analysis**, and **weather pattern studies** across different regions in Nigeria.

---

##  Data Collection Method
- **Source:** OpenWeatherMap Free API
- **Access Method:** REST API (JSON)
- **Update Frequency:** Real-time (data pulled at the time of request)
- **Data Scope:** Major cities in Nigeria (e.g., Lagos, Abuja, Port Harcourt, Kano, Ibadan, Enugu, etc.)

---

##  Dataset Fields
| Column Name         | Data Type | Description |
|---------------------|-----------|-------------|
| `city`              | string    | Name of the Nigerian city |
| `temperature`       | float     | Current temperature in Celsius |
| `feels_like`        | float     | Perceived temperature in Celsius |
| `temp_min`          | float     | Minimum temperature at the time |
| `temp_max`          | float     | Maximum temperature at the time |
| `humidity`          | integer   | Humidity percentage |
| `pressure`          | integer   | Atmospheric pressure (hPa) |
| `weather_main`      | string    | Main weather condition (e.g., Clouds, Rain, Clear) |
| `weather_description` | string | More detailed weather description |
| `wind_speed`        | float     | Wind speed in meters/second |
| `wind_deg`          | integer   | Wind direction in degrees |
| `visibility`        | integer   | Visibility in meters |
| `sunrise`           | datetime  | Sunrise time (UTC) |
| `sunset`            | datetime  | Sunset time (UTC) |
| `timestamp`         | datetime  | Time of data retrieval (UTC) |

---

## How the Data Was Collected
The data was retrieved using the **OpenWeatherMap Current Weather API** for a list of Nigerian cities.  
Each API call returns JSON weather data, which was parsed and stored in a structured CSV format.

**Example API Call:**
```bash
https://api.openweathermap.org/data/2.5/weather?q=Lagos,NG&appid=YOUR_API_KEY&units=metric
```

## Possible Use Cases
* Climate pattern analysis in Nigeria

* Predictive weather modeling using ML

* City-wise environmental studies

* Agricultural planning and decision-making

* Public health analysis related to weather trends


# License
* Data sourced from OpenWeatherMap API.

* API usage is subject to OpenWeatherMap Terms of Service.

* Free tier provides limited requests per minute/hour.



