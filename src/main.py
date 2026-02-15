import requests

print("Hello world !!!")
response = requests.get("https://api.github.com")
print(response.status_code)