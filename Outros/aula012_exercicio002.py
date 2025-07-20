import requests

try:
    r = requests.get("https://www.pudim.com.br")
except:
    print("O Site está indisponível no momento!")
else:
    if r.status_code == 200:
        print("O Site está acessivel!")