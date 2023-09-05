import json
import os


json_file = r'C:\Users\khaza\Desktop\Udemy\Python_3_Deep_Dive\my_codes\customers.json'

with open(json_file, 'r') as json_convert:
    data = json.load(json_convert)
#empty list
converted_file = []

for entry in data:
    converted_entry = {
        "PutRequest": {
            "Item": {
                "id": {"S": (entry["id"])},
                "company": {"S": entry["company"]},
                "last_name": {"S": entry["last_name"]},
                "first_name": {"S": entry["first_name"]},
                "phone": {"S": entry["phone"]},
                "address": {"S": entry["address"]},
                "city_and_state": {"S": entry["city_and_state"]},
                "postal_code": {"S": entry["postal_code"]},
                "country": {"S": entry["country"]}
            }
        }
    }
    converted_file.append(converted_entry)

output_file_path = r'C:\Users\khaza\Desktop\Udemy\Python_3_Deep_Dive\my_codes\converted_output.json'


os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
with open(output_file_path, 'w') as output_file:
    json.dump(converted_file, output_file, indent=4)
