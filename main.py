import requests
from bs4 import BeautifulSoup

url = "https://dolarhoy.com"

# Fetch the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Extract the values using the provided CSS selectors
dolar_oficial_compra = soup.select_one("div.is-7:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)").text.strip()
dolar_oficial_venta = soup.select_one("div.is-7:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)").text.strip()
dolar_blue_compra = soup.select_one(".is-5 > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)").text.strip()
dolar_blue_venta = soup.select_one(".is-5 > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)").text.strip()
dolar_mep_compra = soup.select_one("div.is-7:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)").text.strip()
dolar_mep_venta = soup.select_one("div.is-7:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)").text.strip()
dolar_ccl_compra = soup.select_one("div.is-7:nth-child(2) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)").text.strip()
dolar_ccl_venta = soup.select_one("div.is-7:nth-child(2) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)").text.strip()
dolar_crypto_compra = soup.select_one("div.is-7:nth-child(2) > div:nth-child(5) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)").text.strip()
dolar_crypto_venta = soup.select_one("div.is-7:nth-child(2) > div:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)").text.strip()
dolar_tarjeta = soup.select_one("div.tile:nth-child(6) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)").text.strip()

# Print the extracted values
print()
print("Dolar Oficial Compra:", dolar_oficial_compra)
print("Dolar Oficial Venta:", dolar_oficial_venta)
print("\nFinancieros:")
print("Dolar CCL Compra:", dolar_ccl_compra)
print("Dolar CCL Venta:", dolar_ccl_venta)
print("Dolar MEP Compra", dolar_mep_compra)
print("Dolar MEP Venta", dolar_mep_venta)
print()
print("Dolar Tarjeta", dolar_tarjeta)
print("Dolar Crypto Compra", dolar_crypto_compra)
print("Dolar Crypto Venta", dolar_crypto_venta)
print("Dolar Blue Compra:", dolar_blue_compra)
print("Dolar Blue Venta:", dolar_blue_venta)
print(f"\n\n* Valores obtenidos de {url}")

