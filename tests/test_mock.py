from fastapi.testclient import TestClient
from app.routers.pokemons import router

client = TestClient(router)

def test_get_pokemons_fight(mock_battle_pokemon):
    mock_battle_pokemon.return_value = "Charizard wins!"
    response = client.get("/fight/6/9")
    assert response.status_code == 200
    assert response.json() == "Charizard wins!"

