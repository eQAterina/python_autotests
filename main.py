import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6f7f8a4f05222c57fa6b21ef0f7ab798'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}

# Тело запроса для создания покемона
body_creation = {
    "name": "generate",
    "photo_id": -1
}

# Создаем покемона
response = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_creation)
print("Создание покемона:", response.json())

# Получаем ID созданного покемона
pokemon_id = response.json()['id']
print("ID созданного покемона:", pokemon_id)

# Тело запроса для изменения покемона
body_change = {
    "pokemon_id": pokemon_id,  # Используем полученный ID
    "name": "Фитюлька",
    "photo_id": 2
}

# Изменяем покемона
response_change = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_change)
print("Изменение покемона:", response_change.json())

# Тело запроса "поймать покемона"
body_catch = {
    "pokemon_id": pokemon_id  # Используем полученный ID
}

# Запрос "поймать покемона"
response_catch = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_catch)
print("Ответ на запрос 'поймать покемона':", response_catch.json())



