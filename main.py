import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.macys.com/shop/product/lauren-ralph-lauren-mens-ultraflex-gray-plaid-sport-coat?ID=11734310&CategoryID=9559"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(name="div", class_="price").get_text()
sale_price = soup.find(name="span", class_="c-red bold on-sale").get_text()
print(sale_price)

separate_letters = sale_price.split(" ")
remove_letters = separate_letters[25]


print(remove_letters)

sale_price_without_currency = remove_letters.split("$")[1]
sale_price_as_float = float(sale_price_without_currency)
print(sale_price_as_float)

if sale_price_as_float <= 100.00:
    my_email = "python.project37@gmail.com"
    password = "Thisisstupid125%"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
        to_addrs="nostro37@gmail.com",
        msg=f"Subject:Your item is on sale\n\n${sale_price_as_float}")


