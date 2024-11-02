## Project : Price Comparison Website - Django

[**Français**](README-fr.md)
<p align="center">
  <img src="media/pictures-readme/.png" width="150" height="175" />
  <img src="media/pictures-readme/.png" width="150" height="175" />
  <img src="media/pictures-readme/.png" width="150" height="175" />
</p>

### Table of contents :
1. Project description
2. Features
3. Technology Stack 
4. Web Scraping
5. Django application
6. Deployment
7. SEO considerations

## 1. Project description :
This project is a price comparison web application MVP (Minimum Viable Product) focused on the 
niche of smartwatches. It is primarily intended for users in Egypt. I aimed to create a 
comprehensive project, particularly in terms of backend development. The main goal was to practice
and explore Python and Django, allowing me to learn new libraries and tools while improving my 
skills as a developer. This project consists of two main parts:
* **Web Scraping**
* **Django Application**

## 2. Features :

* **Multilingual Support** : The application is available in both **English** and **Arabic**
* **Price comparison** : Users can click on the product image to display detailed product 
information (such as description, price, etc.) without leaving the page. The application features
a minimalist user interface, allowing users to view prices for multiple smartwatches 
simultaneously and facilitating easy comparisons.
* **Search Bar** : Users can search for specific products by color, brand, or other criteria.
* **Access the store** : Users can easily navigate to the original store of the scraped product 
with a dedicated button, enabling them to view more details and complete their purchase seamlessly.

* **Authentication** :
    * Website authentication
    * Google account integration
* **Favorites** :  Authenticated users can add specific products to their favorites and remove 
them as needed.
* **Product recommendations** : For each smartwatch, users can view the five closest products 
based on descriptions.
* **Feed/posts** : In this first version, the feed feature is designed to be simple. Authenticated
users can write posts to leave feedback, suggest features, or share anything related to their 
experience. These posts will be publicly visible, allowing other users to view and engage with the
content. This feature empowers users to provide their insights and opinions, facilitating iterative
improvements based on user suggestions.
* **Responsive Design** : The application features a responsive design, ensuring a seamless user 
experience across various devices, including desktops, tablets, and smartphones.

## 3. Technology Stack :

### Frontend technologies : 
* HTML
* CSS
* Javascript
### Backend technologies : 
* Programming Language : 
  * **Python**
* Web Framework :
  * **Django**
* Database :
  * **PostgreSQL**
* Caching (in-memory) :
  * **Redis**
* Testing (Unit tests) :
  * **Pytest** 
* Application Server :
  * **Gunicorn**
* Web Server / Reverse Proxy :
  * **Nginx** 
* DevOps tools :
  * **Gitlab CI/CD**
  * **Docker**
  * **Docker Compose**
* Cloud services :
   * **A.W.S** - Amazon Web Services : 
     - **EC2** : Elastic Compute Cloud
     - **SSM** Parameter : Systems Manager
     - **S3** : Simple Storage Service
     - **RDS** : Relational Database Service
     - **SES** : Simple Email Service
### Machine-Learning :

* **scikit-learn**: TfidfVectorizer, cosine_similarity

A bit of machine learning has been implemented in this project to compute vectors from product
descriptions, enabling the identification of the five closest products for each item. 
This is accomplished using `TfidfVectorizer`, which transforms text descriptions into numerical 
vectors based on term frequency-inverse document frequency (TF-IDF) scores. 
We then utilize `cosine_similarity` to measure the similarity between these vectors, 
allowing us to pinpoint the most similar products based on their descriptions.
Then, I have cached the IDs of the product recommendations for improved performance.

## 4. Web Scraping :
* **Scraper** :
In this first version, I have scraped products from four Egyptian websites:
  * Amazon Egypt
  * Jumia Egypt
  * 2B
  * EhabGroup

For each product, I collected the following information: image, price, description, currency, and
product URL. I used `asyncio` and `aiohttp` to fetch data asynchronously from each page, and 
BeautifulSoup to parse the content.

* **Data Normalization** : 
 I implemented helper functions using `Python` and `Pandas` to normalize the scraped data.

* **Data Storing** : Before creating Django instances and storing them in the database, I first 
**saved the products asynchronously in CSV files** (in both English and Arabic) using `aiofiles` 
while they were being fetched.

* **Unique Index Creation** : 
Since the products were stored in two CSV files for both languages but not in the same order 
(due to asynchronous processing), I created a unique index in each CSV file using `Pandas`. 
This step ensured a proper correspondence between the two files, allowing me to instantiate 
the models correctly in English and Arabic using `django-parler`.
## 5. Django Application :

## 6. Deployment :
## 7. SEO considerations :
* **Meta Tags**: Added relevant meta tags to improve search engine indexing and visibility.
* **Manual Translation**: Translated the website content myself to ensure accuracy and better 
alignment with the target audience, rather than relying on automated translation tools like 
Google Translate.
* **Optimized URLs**: Ensured that URLs are clean, descriptive, and contain relevant keywords.
* **Responsive Design**: Implemented responsive design to enhance user experience across devices.


---