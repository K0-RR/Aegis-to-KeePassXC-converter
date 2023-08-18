#!/usr/bin/python3
import json

input("This script will extract data from the JSON file 'aegis.json' located in the working dir and save it to 'KeePassXC.csv'.\nPress any key to continue...\n")

try:
    with open("aegis.json", "r") as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    input("The JSON file 'aegis.json' was not found. Please make sure the file is in the same directory as the script.\n\nPress any key to exit...")
    exit()

entries = data["db"]["entries"]
entry_count = len(entries)

with open("KeePassXC.csv", "w") as csv_file:
    for entry in entries:
        group = entry.get("group", "Ungrouped")  # Default value: "Ungrouped"
        issuer = entry["issuer"]
        name = entry["name"]
        uuid = entry["uuid"]
        note = entry["note"]
        secret = entry["info"]["secret"]
        algo = entry["info"]["algo"]
        digits = entry["info"]["digits"]
        period = entry["info"]["period"]

        csv_file.write(f'"{group}","{issuer}","{name}","","","{note}\nUUID from Aegis: {uuid}","otpauth://totp/{issuer}:{name}?secret={secret}&period={period}&digits={digits}&issuer={issuer}"\n')

print(f"Done, total entries: {entry_count}.")
