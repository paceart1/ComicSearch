import json
from Data import search_path_builder as SPB


class base_DataAccess:
    def __init__(self, topic):
        self.search_data_path = "Data/Data_Files/Data/search_data.json"
        self.exclusion_data_path = "Data/Data_Files/Data/search_term_exclusions.json"
        self.topic = topic

    def exclusion_exists(self, term):
        data = self.get_exclusion_data()
        if term.upper() in data:
            return True
        return False


    def get_all_search_data(self):
        file = open(self.search_data_path, "r")
        data = json.load(file)
        file.close()
        search_data = data["topic search data"][self.topic]
        return search_data

    def get_all_search_paths(self):
        search_data = self.get_all_search_data()
        exclusions = self.get_exclusion_data()
        search_paths = []
        for sd in search_data:
            try:
                search_paths.append(SPB.gen_search_path(sd, exclusions))
            except Exception as ex:
                print(ex)
                print(f"Failure generating path : {sd}")
        return search_paths

    def get_search_data(self, id):
        file = open(self.search_data_path, "r")
        data = json.load(file)
        file.close()
        search_data = data["topic search data"][self.topic]
        for s in search_data:
            if s['id'] == id:
                return s
        return None

    def add_search(self, name:str, number:int, grading_co:list, grades:list, minprice:float,
                   maxprice:float, keywords:list, exclusions:list, era:list=[]):

        file = open(self.search_data_path, "r")
        data = json.load(file)
        file.close()
        search_data = data["topic search data"][self.topic]

        #TODO: Add validation

        #Gen ID
        last_id = search_data[-1]["id"]
        newid = last_id[:3] + str(int(last_id[3:]) + 1)

        for d in search_data:
            if d['id'] == newid:
                return False

        new_topic = {"id":newid, "name": name, "number": number, "era": era,
                "keywords": keywords, "grading_co": grading_co, "grades": grades,
                "exclusions": exclusions, "minprice": minprice, "maxprice": maxprice,
                "item_block_list": []
            }

        search_data.append(new_topic)

        with open(self.search_data_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True

    # EXCLUSIONS
    def get_exclusion_data(self):
        file = open(self.exclusion_data_path, "r")
        data = json.load(file)
        file.close()
        exclusion_data = data["general exclusions"][self.topic]["terms"]
        return exclusion_data

    def add_exclusion(self, term):
        term = term.upper().strip()
        exists = self.exclusion_exists(term)
        if exists:
            print(f"Term {term} already exists")
            return False

        if " " in term: # TODO: Temp warning
            print("* Multiple word entries may not work correctly! *")

        file = open(self.exclusion_data_path, "r+")
        data = json.load(file)
        file.close()

        data["general exclusions"][self.topic]["terms"].append(term)

        with open(self.exclusion_data_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True

    # PATHS

    def get_search_path(self, id, rem_hours=24):
        exclusions = self.get_exclusion_data()
        search_data = self.get_search_data(id)
        path = SPB.gen_search_path(search_data, exclusions, rem_hours)
        return path


class Data:
    Comics = base_DataAccess("comics")
    Cards = base_DataAccess("cards")


if __name__ == "__main__":
    data = Data()
    data.Comics.search_data_path = "Data_Files/Data/search_data.json"
    sd = data.Comics.get_all_search_data()
    for s in sd:
        print(s)




