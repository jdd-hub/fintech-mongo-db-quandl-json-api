import json


class Json:

    # Save the JSON stream to the specified path and location.
    def dump_to_file(file_name, json_dict, path=None):

        # If the path is specified updated full path to with path.
        if path:
            full_path = path + file_name + ".json"
        else:
            full_path = file_name.replace(" ", "_") + ".json"

        # Open the JSON file for writing.
        with open(full_path, "w") as file:
            # Dump the JSON dictionary in the specified in indented format for human read ability.
            json.dump(json_dict, file, indent=2)

            # Return the name of the new file.
            return file.name