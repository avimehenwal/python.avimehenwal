import pprint

CSV_DATA = [
  "Selfie Stick,98,29",
  "iPhone Case,90,15",
  "Fire TV Stick,48,49",
  "Wyze Cam,48,25",
  "Water Filter,56,49",
  "Blue Light Blocking Glasses,90,16",
  "Ice Maker,47,119",
  "Video Doorbell,47,199",
  "AA Batteries,64,12",
  "Disinfecting Wipes,37,12",
  "Baseball Cards,73,16",
  "Winter Gloves,32,112",
  "Microphone,44,22",
  "Pet Kennel,5,24",
  "Jenga Classic Game,100,7",
  "Ink Cartridges,88,45",
  "Instant Pot,98,59",
  "Hoze Nozzle,74,26",
  "Gift Card,45,25",
  "Keyboard,82,19"
]

structured_data = []
for item in CSV_DATA:
    data = {}
    [Title, Popularity, Price] = item.split(',')
    data['TITLE'] = Title
    data['POPULARITY'] = int(Popularity)
    data['PRICE'] = int(Price)
    structured_data.append(data)

sort_by_price = sorted(structured_data, key=lambda d: d['PRICE'],  reverse=True)
sort_by_price_popularity = sorted(sort_by_price, key=lambda d: d['POPULARITY'],  reverse=True)

pprint.pprint([item['TITLE'] for item in sort_by_price_popularity])
