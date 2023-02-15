from locust import HttpUser, between, task
import random

class PokemonUser(HttpUser):
    wait_time = between(1, 5)
    #
    @task
    def fight_pokemon(self):
        id_pokemon_1 = random.randint(1, 1008)
        id_pokemon_2 = random.randint(1, 1008)
        response = self.client.get(f'/pokemons/fight/{id_pokemon_1}/{id_pokemon_2}')
        if response.status_code == 200:
            print(f"{id_pokemon_1} vs {id_pokemon_2}: {response.text}")
        else:
            print(f"Error: {response.status_code}")