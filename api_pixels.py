import requests
import csv
from time import sleep

items = [
    'itm_egg',
    'itm_seltsamEgg',
    'itm_eggsplosive',
    'itm_honey',
    'itm_beeswax',
    'itm_queenbee',
    'itm_Iron_Ore',
    'itm_clay',
    'itm_Marble',
    'itm_void',
    'itm_silkfiber',
    'itm_silkslugslime',
    'itm_silkslugspider',
    'itm_wood',
    'itm_hard_wood',
    'itm_tree_sap',
    'itm_popberryFruit',
    'itm_butterberry',
    'itm_grainbow',
    'itm_scarrotFruit',
    'itm_grumpkinFruit',
    'itm_cloverFruit',
    'itm_hotato',
    'itm_wintermintFruit',
    'itm_tenta',
    'itm_muckchuck',
    'itm_clover4LeafFruit',
    'itm_popberryPie',
    'itm_popberryLoaf',
    'itm_pancakes',
    'itm_plain_omelet',
    'itm_scarrotPie',
    'itm_scarrotLoaf',
    'itm_grumpFruit',
    'itm_grumpkinPie',
    'itm_grumpkinLoaf',
    'itm_Iron_Bar',
    'itm_brick',
    'itm_Glue',
    'itm_Bomb_Shell',
    'itm_flour',
    'itm_4_leaf_cloveregano',
    'itm_Shrapnel',
    'itm_constructionPowder',
    'itm_hay',
    'itm_popberrywine',
    'itm_grumpkinwine',
    'itm_scarrotwine',
    'itm_grainbow_grainshine',
    'itm_wintermint_whiskey',
    'itm_tentacactus_tequila',
    'itm_muckchuck_mead',
    'itm_butterberry_butterbrew',
    'itm_Fireplace',
    'itm_hot_sauce',
    'itm_coffeepod',
    'itm_limestone_paving_stones',
    'itm_silkcloth',
    'itm_cunstruction_cone',
    'itm_plaster',
    'itm_silkrope',
    'itm_silkcloth',
    'itm_plank',
    'itm_storageChest6Slot',
    'itm_milk',
    'itm_turd',
    'itm_hotato_hotka',
    'itm_woodenbeam'


]

# Create csv file or clear existinf csv file data
field_names = ["product", "price"]
with open("pixels_api.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    print("creating / rewriting csv file")

# For each item on the list, get the api data and write it on csv at immediately.
for item_id in items:
    print(f"requesting ..{item_id}")
    url2 = f"https://pixels-server.pixels.xyz/v1/marketplace/item/{item_id}?pid=65cf188f507c9890f600014c&v=1708071055158.2617"

    try:
        response = requests.get(url2)
        response2 = response.json()

    except requests.exceptions.JSONDecodeError:
        print(f"Error {response.status_code} occurred")

        break

    else:
        item_price = response2["listings"][0]["price"]

        with open("pixels_api.csv","a", newline="") as csvfile:
            print(f"writing {item_id}\n\n")
            item_data = [{"product": item_id, "price": item_price}]
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writerows(item_data)



print("closing program in..",end="")
for i in range(3):

    print(f"{3-i}..",end="")
    sleep(1)
print("")