import json
import simplejson

class Cleaner:
    def __init__(self):
        self.search_data_path = "Data/Data_Files/Data/search_data.json"
        self.exclusion_data_path = "Data/Data_Files/Data/search_term_exclusions.json"

        self._temp_search_data_path = "Data/Data_Files/Data/temp_search_data.json"
        self._temp_exclusion_data_path = "Data/Data_Files/Data/exclusions_search_data.json"

    def _write_to_temp(self, data, path):
        with open(path, "w") as tempFile:
            # magic happens here to make it pretty-printed
            #TODO is using loads instead of dumps
            tempFile.write(
                simplejson.dumps(simplejson.loads(data), indent=4, sort_keys=True)
            )

    def clean_ids(self):
        file = open(self.search_data_path, "r")
        data = json.load(file)
        file.close()
        comic_data = data["topic search data"]["comics"]
        card_data = data["topic search data"]["cards"]

    def run_cleanup(self):
        pass



if __name__ == "__main__":
    cleaner = Cleaner()