from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends
from app import actions, schemas
from app.utils.utils import get_db
from app.utils.pokeapi import battle_pokemon

router = APIRouter()


@router.get("/", response_model=List[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Return all pokemons
        Default limit is 100
    """
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    return pokemons

@router.get("/fight/{id_pokemon_1}/{id_pokemon_2}")
def get_pokemons_fight(
    id_pokemon_1: int, id_pokemon_2: int, database: Session = Depends(get_db)
):
    return battle_pokemon(id_pokemon_1, id_pokemon_2)
