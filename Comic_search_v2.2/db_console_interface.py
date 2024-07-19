import os
from Data.data_access import Data

class InterfaceFunctions:
    db = {"comics":Data.Comics, "cards":Data.Cards}

    @classmethod
    def _show_search_data(cls, data, header=""):
        if header: print(header)
        print(f"\t{data['id']}-{data['name']} {data['number']} | Minimum Price: ${data['minprice']} "
              f"\tMaximum Price: ${data['maxprice']}")
        print(f"\tGrading companies: {data['grading_co']} | Grades: {data['grades']}")
        print(f"\tAdditional Keywords: {data['keywords']}")
        print(f"\tItem specific exclusions: {data['exclusions']}")

    @classmethod
    def yes_no_loop(cls, message) -> bool:
        while True:
            print(message)
            choice = input("\tEnter yes or no >> ").lower()
            if choice == "yes" or choice == "y":
                return True
            elif choice == "no" or choice == "n":
                return False
            else:
                print("Invalid.")

    @classmethod
    def exit_application(cls, cat):
        print("Exiting application...")
        exit()

    @classmethod
    def show_exclusions(cls, cat):
        data = cls.db[cat].get_exclusion_data()
        print(f"{cat.upper()} EXCLUSIONS:")
        for d in data:
            print(f"\t{d}")

    @classmethod
    def show_searches(cls, cat:str):
        data = cls.db[cat].get_all_search_data()
        for d in data:
            cls._show_search_data(d, "\n")
            #print(f"{d['id']} - {d['name']} #{d['number']}")
            #print(f"Grading: {d['grading_co']} {d['grades']}  |  Max Price: {d['maxprice']}")
            #print(f"Keywords: {d['keywords']}")
            #print(f"Exclusions: {d['exclusions']}\n")

    @classmethod
    def add_search(cls, cat:str):
        print("\nADDING NEW SEARCH TOPIC:")
        print("Enter the data for the new topic or enter quit at any time to return.  ")

        name = ""
        while not name:
            name = input("\n\tEnter the name or title >> ").strip().lower()
            if name == "quit": return
        while True:
            number = input("\n\tEnter the number or issue >> ").strip()
            if number == "quit": return
            try:
                number = int(number)
                break
            except ValueError:
                print("\tInvalid")

        keywords = []
        grading_co = []
        grades = []
        max_price = 999999
        min_price = 0
        exclusions = []

        while cls.yes_no_loop("\n\tDoes your search have additional keywords?"):
            keyword = input("\tEnter keyword >> ").strip().lower()
            if keyword == "quit": return
            keywords.append(keyword)
        while cls.yes_no_loop("\n\tDoes your search have additional exclusions?"):
            exclusion = input("\tEnter exclusion >> ").strip().lower()
            if exclusion == "quit": return
            exclusions.append(exclusion)
        if cls.yes_no_loop("Is your search professionally graded?"):
            co_output = None
            while cls.yes_no_loop(f"\n\tDo you want to add a grading company? (Current grading companies: {co_output})"):
                co = input("\tEnter company such as PSA or CGC >> ").strip().upper()
                if co == "quit": return
                grading_co.append(co)
                co_output = ", ".join(grading_co)
            grades_output = None
            while cls.yes_no_loop(f"\n\tDo you want to add a numeric grade? (Current grades: {grades_output})"):
                grade = input("\tEnter a grade such as 9.8 >> ").strip()
                if grade == "quit": return
                try:
                    float(grade)
                    grades.append(grade)
                    grades_output = ", ".join(grades)
                except ValueError:
                    print("Entry failed not valid")

        while cls.yes_no_loop(f"\n\tDo you want to set a minimum price?  The default is ${min_price}"):
            min_p = input("\tEnter a minimum price.  Do not include symbols other than a decimal >>")
            if min_p == "quit": return
            try:
                min_p = float(min_p)
                if cls.yes_no_loop(f"\tIs ${min_p} correct as the minimum price?"):
                    min_price = min_p
                    break
            except ValueError:
                print("\tinvalid")

        while cls.yes_no_loop(f"\n\tDo you want to set a maximum price?  The default is ${max_price}"):
            max_p = input("\tEnter a maximum price.  Do not include symbols other than a decimal >>")
            if max_p == "quit": return
            try:
                max_p = float(max_p)
                if cls.yes_no_loop(f"\tIs ${max_p} correct as the maximum price?"):
                    max_price = max_p
                    break
            except ValueError:
                print("\tinvalid")

        print(f"\n\nNew {cat.upper()} search topic to be added:")

        print(f"\n\t{name} #{number} {','.join(grading_co)} {','.join(grades)}")
        print(f"\tMinimum Price ${min_price}  |  Maximum Price ${max_price}")
        print(f"\tAdditional Keywords: {','.join(keywords)}")
        print(f"\tAdditional Exclusions: {','.join(exclusions)}")
        if cls.yes_no_loop("\n\tDoes the following information look correct?"):
            if cls.db[cat].add_search(name, number, grading_co, grades, min_price, max_price, keywords, exclusions):
                print("\n\tSearch Added.")
            else:
                print("\n\tUnable to add search to database")
        else:
            print("\n\tSearch not added.")
        print("\tReturning to the menu...")

    @classmethod
    def edit_search(cls, cat:str):
        print("\nEDIT SEARCH TOPIC:")
        #TODO: implement fully and delete warning
        print("CAUTION : NOT FULLY IMPLEMENTED. Updated will not be saved")
        while True:
            print("\n\tEnter the id of the search to edit. Hint: id starts with 3 letters and 6 numbers ")
            print("\t(Type list to view current topics or type quit at any time to return to the menu)")
            id = input("\n\t >> ").lower()
            if id == "quit": return
            if id == "list":
                cls.show_searches(cat)
                continue

            # Begin editing process here
            # Show current data
            data = cls.db[cat].get_search_data(id)
            if not data:
                print("id does not exist.")
                continue
            print(f"Editing category {cat} - id {id}")
            cls._show_search_data(data, "\tDATA")

            while cls.yes_no_loop("Edit Name/Title?"):
                new_name=input("Enter the new name or title >> ")

            while cls.yes_no_loop("Edit Number?"):
                new_number = input("Enter the new issue or number >> ")

            while cls.yes_no_loop("Edit minimum price?"):
                new_minprice = input("Enter the new minimum price >> ")

            while cls.yes_no_loop("Edit maximum price?"):
                new_max_price=input("Enter the new maximum price. >> ")

            while cls.yes_no_loop("Edit Grading Companies?"):
                print(f"Existing companies : {','.join(data['grading_co'])}")
                co = input("Enter a new company to add or an existing company to remove >> ").lower()
                #TODO: Implement add or remove

            while cls.yes_no_loop("Edit Grades?"):
                print(f"Existing Grades : {','.join(data['grades'])}")
                grade = input("Enter a new grade to add or an existing grade to remove >> ").lower()
                # TODO: Implement add or remove

            while cls.yes_no_loop("Edit Keywords?"):
                print(f"Keywords Grades : {','.join(data['keywords'])}")
                grade = input("Enter a new keyword to add or an existing keyword to remove >> ").lower()
                # TODO: Implement add or remove

            while cls.yes_no_loop("Edit Exclusions?"):
                print(f"Exclusions Grades : {','.join(data['exclusions'])}")
                grade = input("Enter a new exclusion to add or an exclusion to remove >> " ).lower()
                # TODO: Implement add or remove




    @classmethod
    def add_exclusion(cls, cat:str):
        print(f"Adding a new exclusion to {cat}")
        term = input("Enter a new term to exclude from searches or quit to return to the menu>> ").lower()
        if term == "quit":return
        result = cls.db[cat].add_exclusion(term)

        if result:
            print(f"{term} added to {cat}")
        else:
            print("term NOT added!")


class OptionsManager:
    def __init__(self):
        self._ui_functions = {}

    def get_count(self):
        return len(self._ui_functions)

    def add(self, key:str, func):
        if type(key) != str:
            raise Exception("Key must be a string") #TODO: change to argument exception
        if key in self._ui_functions:
            print(f"Key: {key} already exists")
            return
            #raise Exception("")
        self._ui_functions[key] = func

    def get_function(self, key):
        if key.isdecimal():
            key_int = int(key)
            if key_int < 0 or key_int >= self.get_count():
                return None
            return list(self._ui_functions.values())[key_int]

        if key not in self._ui_functions:
            return None

        return self._ui_functions[key]

    def get_keys(self):
        return list(self._ui_functions.keys())


class ConsoleInterface:
    def __init__(self):
        self.options = OptionsManager()
        self.options.add("quit", InterfaceFunctions.exit_application)
        self.options.add("show exclusions", InterfaceFunctions.show_exclusions)
        self.options.add("add exclusions", InterfaceFunctions.add_exclusion)
        self.options.add("show searches", InterfaceFunctions.show_searches)
        self.options.add("add search", InterfaceFunctions.add_search)
        self.options.add("edit search", InterfaceFunctions.edit_search)

    def _clear_console(self):
        clear = lambda: os.system('cls')  # on Windows System
        #clear = lambda: os.system('clear')  # on Linux System
        clear()

    def show_options(self):
        print("\nEnter the term of your choice or 'cat' to change categories.")
        keys = self.options.get_keys()
        for ii in range(self.options.get_count()):
            print(f"\t{ii}. {keys[ii]}")

    def _run_inner_options(self, cat):
        while True:
            self.show_options()
            choice = input(">> ").lower()
            if choice == "cat": return
            f = self.options.get_function(choice)
            if f is not None:
                f(cat)
            else:
                print("Invalid")


    def run(self):
        while True:
            print("Database Console App:\n")
            print("Select a category or enter quit to exit")
            cat = input("\tEnter comics or cards >>").lower()
            if cat == "quit":
                break
            if cat not in InterfaceFunctions.db.keys():
                print("invalid")
                continue
            self._clear_console()
            self._run_inner_options(cat)



if __name__ == "__main__":
    ui = ConsoleInterface()
    ui.run()
