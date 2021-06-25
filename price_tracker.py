import requests
from bs4 import BeautifulSoup
import smtplib
import time


def check_price():
    URL = "URL"

    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    title = title.strip()
    con_price_1 = price[2]
    con_price_2 = price[4:7]
    con_price = int(con_price_1 + con_price_2)

    print(title)
    print(con_price)

    if(con_price >= 7990):
        mail()


def mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('GMAIL-ID', 'API')

    subject = 'PRICE DOWN'
    link = 'URL'

    msg = f"SUBJECT : {subject}\n\nLINK BELOW\n\n{link}"

    server.sendmail('FROMmail', 'TOgmail', msg)
    print('MAIL_SENT')
    server.quit()


while(True):
    check_price()
    time.sleep(60)

#MADE BY THIRISHUL ASOKAN
