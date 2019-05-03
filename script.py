import requests

re = requests.get("https://coreyms.com")

print(re.status_code)
