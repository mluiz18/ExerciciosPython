import requests

API_KEY = "AAAAAAAAAAAAAAAAAAAAABvo1wEAAAAAIjYIyiYOx7KpNRyP7oHZtfv%2BcJE%3DFj7TkTmef00TNcnsr3icSoCyPzdMO3MYJM16D9HVrtegD7Zc5b"
BASE_URL = "https://api.twitter.com/2/tweets/search/recent"
query = str(input("Digite sua marca: "))
headers = {"Authorization": f"Bearer {API_KEY}"}
params = {"query": query}
response = requests.get(BASE_URL, headers=headers, params=params)

if response.status_code == 200:
    tweets = response.json().get("data", [])
    if tweets:
        for tweet in tweets:
            print(f"{tweet['text']}\n")
    else:
        print("Nenhum tweet encontrado para essa marca.")
else:
    print(f"Erro ao buscar tweets: {response.status_code} - {response.text}")
