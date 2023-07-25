import json

input_json_file_path = "main_test.json"
input_mod_file_path = "main_test_mod.json"


# Reading data from a JSON-file
def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


if __name__ == "__main__":

    # Reading data from files
    input_data = read_json(input_json_file_path)
    modified_data = read_json(input_mod_file_path)

    # Function to find missing blocks
    def find_missing_blocks(input_data, modified_data, current_key=""):
        if isinstance(input_data, dict):
            for key, value in input_data.items():
                new_key = key if not current_key else f"{current_key}.{key}"
                if key not in modified_data:
                    print(f"Block:   {new_key}   missing from   >>>>>   '{input_mod_file_path}'")
                else:
                    find_missing_blocks(value, modified_data[key], new_key)
        elif isinstance(input_data, list):
            for i, item in enumerate(input_data):
                new_key = current_key if not current_key else f"{current_key}[{i}]"
                find_missing_blocks(item, modified_data[i], new_key)

    # Comparison and output of missing blocks
    find_missing_blocks(input_data, modified_data)
