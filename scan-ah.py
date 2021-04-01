import blizz_api
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_mapper import map_item

engine = create_engine("", echo=True, future=True)

api = blizz_api.BlizzApi()

item = api.find_item(name="Elementium Dragonling",inventory_type="Trinket")
model_item = map_item(item['results'][0])
with Session(engine) as session:
    session.add(model_item)
    session.commit()