from model import ObservedItem


def map_item(json) -> ObservedItem:
    data = json['data']
    return ObservedItem(
        wow_id= data['id']
        , name=__locale(data['name'])
        , item_class=__locale(data['item_class']['name'])
        , item_subclass=__locale(data['item_subclass']['name'])
        , item_type=__locale(data['inventory_type']['name'])
        , quality=__locale(data['quality']['name'])
        , ilvl=data['level']
    )


def __locale(data):
    return data['en_US']
