from Model.search_handler import SearchHandler
from Model.search_result_Parser import Parser
from Data.data_access import Data
from Model.search_topic import SearchTopic


class base_Model:
    def __init__(self, database, base_path, search_handler, parser):
        self.search_handler = search_handler
        self.parser = parser
        self.base_path = base_path
        self.database = database

    def get_search_results(self, path):
        raw = self.search_handler.connect_search(self.base_path, path)
        parsed_data = self.parser.parse_data(raw)
        #TODO: Use defined data type?
        return parsed_data

    def get_search_data(self, id):
        raise NotImplementedError()

    def get_all_search_data(self):
        # No id returns all
        searches = self.database.get_all_search_data()
        data = []
        for s in searches:
            d = SearchTopic(s['id'], s['name'], s['number'], s['era'], s['keywords'], s['grades'],
                             s['exclusions'], s['minprice'], s['maxprice'], s['item_block_list'])
            data.append(d)
        return data

    def get_exclusions(self):
        return self.database.get_exclusion_data()

    def get_search_path(self, id, rem_time=24):
        return self.database.get_search_path(id, rem_time)


class Model:
    def __init__(self):
        self.search_handler = SearchHandler()
        self.parser = Parser()
        self.base_path = "https://www.ebay.com/sch/i.html?"

        # database, base_path, search_handler, parser
        self.Comics = base_Model(Data.Comics, self.base_path, self.search_handler, self.parser)
        self.Cards = base_Model(Data.Cards, self.base_path, self.search_handler, self.parser)

'''
class Model:
    def __init__(self):
        self.search_handler = SearchHandler()
        self.parser = Parser()
        self.base_path = "https://www.ebay.com/sch/i.html?"

    def get_search_results(self, path):
        raw = self.search_handler.connect_search(self.base_path, path)
        parsed_data = self.parser.parse_data(raw)
        #TODO: Use defined data type?
        return parsed_data

    def get_search_data(self, id):
        raise NotImplementedError()

    def get_all_search_data(self):
        # No id returns all
        searches = Data.Comics.get_all_search_data()
        data = []
        for s in searches:
            d = SearchTopic(s['id'], s['name'], s['number'], s['era'], s['keywords'], s['grades'],
                             s['exclusions'], s['minprice'], s['maxprice'])
            data.append(d)
        return data

    def get_exclusions(self):
        return Data.Comics.get_exclusion_data()

    def get_search_path(self, id):
        return Data.Comics.get_search_path(id)
'''