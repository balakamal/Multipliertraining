import requests
url = input("Enter the url you want to take source code:")
x = requests.get(url)

print(x.text)
