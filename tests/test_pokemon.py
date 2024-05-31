import requests
import pytest

URL = 'https://pokemonbattle.ru/v2'
TRAINER_ID = '2658'
TOKEN = 'f58d02f05aa4c3c258529cbc70aa8771'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINERNAME = 'qwerb'

def test_trainers_status_code():
    """Проверяем, что ответ GET запроса на /pokemons (для конкретного тренера) приходит с кодом состояния 200."""
    response = requests.get(f'{URL}/pokemons', headers=HEADER, params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200


def test_trainers_contains_trainer_name():
    """Проверяем, содержится ли в ответе имя тренера."""
    response = requests.get(f'{URL}/pokemons', params={'trainer_id': TRAINER_ID}, headers=HEADER)
    trainers_list = response.json()  # ответ - это список тренеров в формате JSON
    # Поиск тренера по имени в списке всех тренеров
    assert any(trainer['name'] == TRAINERNAME for trainer in trainers_list)