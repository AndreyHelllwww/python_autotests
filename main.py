import requests
import json

URL = 'https://pokemonbattle.ru/v2'
TOKEN = 'f58d02f05aa4c3c258529cbc70aa8771'
HEADER = {'Content-Type': 'application/json'}

# Создание покемона
data_create = {
    "trainer_token": TOKEN,
    "name": "generate",
    "photo": "generate"
}
response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=data_create)
print("Создание покемона:", response_create.text)

# Получение id из прошлого ответа
pokemon_id = response_create.json()['id'] 

# Смена имени покемона
data_rename = {
   "pokemon_id": pokemon_id,
   "trainer_token": TOKEN,
   "name": "НовоеИмя"  
}
response_rename = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=data_rename)  
print("Смена имени покемона:", response_rename.text)

# Поймать покемона в покебол
data_catch = {
 "trainer_id": "2658",
 "pokemon_id": pokemon_id,
 "trainer_token": TOKEN
}
response_catch = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=data_catch)  
print("Поймать покемона в покебол:", response_catch.text)