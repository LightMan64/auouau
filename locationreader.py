import json
with open(r"C:\Users\Izaak Rochester\Desktop\my creations\stardewfish\Locations.json", "r", encoding="utf-8") as file:
    data = json.load(file)
for item in data.keys():
    if len(data[item]["Fish"]) > 0:
        print(item)
        for fish in data[item]["Fish"]:
            if("Id" in fish):
                print(fish["Id"])
            else:
                print("Fish has no id")