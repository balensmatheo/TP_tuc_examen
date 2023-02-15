import unittest
from app.utils.pokeapi import battle_pokemon,get_pokemon_name,get_pokemon_stats,get_pokemon_data

class TestBattlePokemon(unittest.TestCase):
    """
        Test module pokeapi
    """

    def test_battle_pokemon(self):
        """
            Test do battle between 2 pokemons
        """
        # Define test inputs
        first_api_id = 247
        second_api_id = 124

        # Test battle_pokemon function
        result = battle_pokemon(first_api_id, second_api_id)

        # Assertions
        self.assertIn('draw', result['winner'])

    def test_get_pokemon_name(self):
        """
            Test to get a pokemon name from the API pokeapi
        """
        # Define test inputs
        api_id = 25

        # Test get_pokemon_name function
        result = get_pokemon_name(api_id)

        # Assertions
        self.assertEqual(result, "pikachu")

    def test_get_pokemon_stats(self):
        """
            Test to get pokemon stats from the API pokeapi
        """
        # Define test inputs
        api_id = 25

        # Test get_pokemon_stats function
        result = get_pokemon_stats(api_id)

        # Assertions
        self.assertEqual(len(result), 6)
        self.assertEqual(result[0]["stat"]["name"], "hp")
        self.assertEqual(result[1]["stat"]["name"], "attack")
        self.assertEqual(result[2]["stat"]["name"], "defense")
        self.assertEqual(result[3]["stat"]["name"], "special-attack")
        self.assertEqual(result[4]["stat"]["name"], "special-defense")
        self.assertEqual(result[5]["stat"]["name"], "speed")

    def test_get_pokemon_data(self):
        # Define test inputs
        api_id = 25

        # Test get_pokemon_data function
        result = get_pokemon_data(api_id)

        # Assertions
        self.assertIsInstance(result, dict)
        self.assertEqual(result["name"], "pikachu")
        self.assertEqual(result["id"], api_id)
