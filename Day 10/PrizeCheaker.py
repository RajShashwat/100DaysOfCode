import requests
from bs4 import BeautifulSoup
import smtplib


URL="https://www.amazon.in/Fitbit-FB507BKBK-Smartwatch-Tracking-Included/dp/B07TWFVDWT/ref=lp_19091095031_1_1?srs=19091095031&ie=UTF8&qid=1572603389&sr=8-1"


UA={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}

def email():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login('Sender Email id', 'Password')

    subject = 'PRIZE CHANGED!!!'
    body= 'Check the Amazon Link : https://www.amazon.in/Test-Exclusive-608/dp/B07HGBMJT6/ref=sr_1_1?keywords=oneplus+6t&qid=1571923245&smid=A35FCS7U51TK3C&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('Sender Email id', 'reciver email id',msg)
    print('HEY MAIL IS SENT!')


    server.quit()

def check_price():

    page = requests.get(URL, headers=UA)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    display_price = soup.find(id="priceblock_ourprice").get_text()
    price = float(display_price[2:4])*1000+float(display_price[5:8])

    if price<30000:
        email()

    print(price)
    print(title.strip())

check_price()
