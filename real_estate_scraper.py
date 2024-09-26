
from bs4 import BeautifulSoup
import csv
import requests

# Step 1: Load the HTML file
#with open('html_page1.html', 'r', encoding='utf-8') as file:
 #   html_content = file.read()

# Step 2: Parse the HTML content
url = "https://www.remax.ca/on/toronto-real-estate"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

pricelist = []
bedlist = []
bathlist = []
addresslist = []



#prices
prices = soup.findAll('h2', class_="listing-card_price__lEBmo")
for price in prices :
    price = price.text
    pricelist.append(price)
    #print(price)


#beds
beds = soup.findAll('span', attrs={'data-cy': 'property-beds'})
for bed in beds:
    bed = bed.text
    bedlist.append(bed)

    #print(bed)

#baths
baths = soup.findAll('span', attrs={'data-cy': 'property-baths'})
for bath in baths:
    bath = bath.text
    bathlist.append(bath)
    #print(bath)

#address
addresses = soup.findAll('div', attrs={'data-cy': 'property-address'})
for address in addresses:
    address = address.text
    addresslist.append(address)
    #print(address)

csv_filename = 'result.csv'

# Open the CSV file in write mode and specify newline='' to avoid extra blank lines
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header row
    csv_writer.writerow(['Price', 'Bed', 'Bath', 'Address'])

    # Write each row of data
    for price, bed, bath, address in zip(pricelist, bedlist, bathlist, addresslist):
        csv_writer.writerow([price, bed, bath, address])

