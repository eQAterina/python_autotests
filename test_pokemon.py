import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6f7f8a4f05222c57fa6b21ef0f7ab798'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}
TRAINER_ID = '23119'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200

def test_trainer_id():
    response_trainer = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response_trainer.json()["data"][0]["trainer_name"] == 'KaterW'
