import glob
import json
import os
import pandas as pd

# 1. Define the folder containing your JSON files
json_folder = "./json_files"  # Change this to your folder path
output_excel = "merged_output.xlsx"

# 2. Find all JSON files in the directory
json_files = glob.glob(os.path.join(json_folder, "*.json"))

# 3. Read and combine all JSON data into a single list
all_data = []
data_list = []
for file_path in json_files:
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)

            # If the JSON file contains a single object, wrap it in a list
            if isinstance(data, dict):
                all_data.append(data)
            # If the JSON file is already a list of objects, extend the main list
            elif isinstance(data, list):
                all_data.extend(data)

        except json.JSONDecodeError:
            print(f"Skipping invalid JSON file: {file_path}")

for item in all_data:
    data_list.append(item["address"].split(", ") + ["Церкви", item["name"]])
# 4. Convert the combined data into a Pandas DataFrame
df = pd.DataFrame(data_list)

# 5. Export the DataFrame to an Excel spreadsheet
df.to_excel(output_excel, index=False)

print(f"Successfully merged {len(json_files)} JSON files into '{output_excel}'!")
      
