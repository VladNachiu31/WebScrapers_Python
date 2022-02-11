import requests
from bs4 import BeautifulSoup
import smtplib


def get_price(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find('span', {'itemprop': 'price'})['content']
    return price


def add_prices(p1, p2, p3):
    total = (float(p1) + float(p2) + float(p3))
    return total


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('yourgmail@gmail.com', 'Yourpassword')
    subject = 'Your Upgrade Price today'
    body = f'The total price to upgrade today is: {total_price}'
    message = f'Subject:{subject}\n\n{body}'
    server.sendmail('emailfrom@gmail.com', 'email_to@gmail.com', message)
    print('Email sent')
    server.quit()


cpu = get_price(
    'https://www.scan.co.uk/products/amd-ryzen-5-3600x-am4-zen-2-6-core-12-thread-38ghz-44ghz-turbo-32mb-l3-pcie-40-95w-cpu-pluswraith-sp')
motherboard = get_price(
    'https://www.scan.co.uk/products/msi-tomahawk-max-ii-amd-b450-am4-ddr4-pcie-30-sata-3-m2-2-way-crossfire-gbe-lan-atx')
ram = get_price(
    'https://www.scan.co.uk/products/16gb-2x8gb-corsair-ddr4-vengeance-lpx-black-pc4-25600-3200-non-ecc-unbuff-cas-16-135v-amd-ryzen-opti')

total_price = add_prices(cpu, motherboard, ram)

print(total_price)
