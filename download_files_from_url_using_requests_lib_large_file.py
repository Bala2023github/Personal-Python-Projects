import requests


url = "https://api.worldbank.org/data/download/WDI_CSV.zip"

response = requests.get(url,stream=True)

print(response.url,"\n", response.ok,"\n", response.status_code)

with open("gdp_by_country_via_requests.zip",mode="wb") as file:
    for chunk in response.iter_content(chunk_size=10*1024):
    # file.write(response.content)
        file.write(chunk)