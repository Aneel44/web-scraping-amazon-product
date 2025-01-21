# This app scrap data from amazon website

# requests
# beautifulsoup4
# pandas
# lxml

from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

url = 'https://www.amazon.in/Apple-Headphones-Cancellation-Transparency-Personalised/dp/B0DGJ7S59D/ref=sr_1_4?crid=RBARZ970AYJI&dib=eyJ2IjoiMSJ9.y08pMqaeTlUXGU64oyMGlx8v2Sx78yzGgsFfSLyufaCZhsU6s-KsHLVTWzO21l030BNAPdSwF1uvk-xP2xiYHOrOsuJoyUXTbtnLlKohg0PDfeDV2ow3KJTID02CZHFHe8BElHxz0Qx9AFS7cgOtkIB0SiGqovUlX53vpFMVfDlFCxKDYYyYS0xwojJ1zvN8J-uZuRvzI8Bf-RrBv58giQ5qGy-67sptz4v75mHE4Wo.tSxthxJx5H1i4-8rVzEb4sSrmXDaiOyiNDov_Gs8y5U&dib_tag=se&keywords=apple%2Bairpods%2Bpro%2Bmax&nsdOptOutParam=true&qid=1736429886&sprefix=%2Caps%2C209&sr=8-4&th=1'
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # print(response.status_code)
    html_content = response.text
else:
    print('Error', response.status_code)
    
soup = BeautifulSoup(html_content, 'lxml')
# print(soup.prettify())
# product title
product_title = soup.find("span", id='productTitle').get_text().strip()
# product price
product_price = soup.find("span", class_="a-price-whole").get_text().strip()
# product rating
product_rating = soup.find("span", id="acrPopover").get_text().strip()
# product bullet points
product_bp = soup.find("ul", class_="a-unordered-list a-vertical a-spacing-mini").get_text().strip()
# product description
product_description = soup.find("div", id="productDescription").get_text().strip()
# product reviews
reviews = soup.find("ul", id="cm-cr-dp-review-list").get_text().strip()
# product techincal details
techincal_details = soup.find("div", class_="a-section a-spacing-small a-spacing-top-small").get_text().strip()
# print data
print(techincal_details)

# saving the data
with open('amazon_airpods.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Product Title', 'Product Price', 'Product Rating', 'Product Bullet Points', 'Product Description', 'Reviews', 'Techincal Details'])
    writer.writerow([product_title, product_price, product_rating, product_bp, product_description, reviews, techincal_details])
print('File saved')