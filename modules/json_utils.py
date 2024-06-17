import json


# read json
def read_json(name=""):
    filename = f'{name}.json'
    # Try to open and read the file
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # Use json.load() to read data from a file
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except json.JSONDecodeError:
        print("Error: The file does not contain valid JSON.")
    except IOError as e:
        print("I/O error:", e)
    except Exception as e:
        print("Unexpected error:", e)


# save json
def save_json(data, name):
    # Specify the file name to be written
    filename = f'{name}.json'

    # Open a file for writing
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            # Use json.dump() to convert the dict to JSON format and write it to a file
            json.dump(data, f, indent=4)
        print("Data has been written to", filename)
    except IOError as e:
        print("I/O error:", e)
    except Exception as e:
        print("Unexpected error:", e)
