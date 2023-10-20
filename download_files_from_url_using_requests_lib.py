import requests


url = "https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD"

query_parameters = {"downloadformat" : "csv"}

response = requests.get(url,params = query_parameters)

print(response.url,"\n", response.ok,"\n", response.status_code)

with open("gdp_by_country_via_requests.zip","wb") as file:
    file.write(response.content)