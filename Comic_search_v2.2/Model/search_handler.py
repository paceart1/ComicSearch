import requests
#from bs4 import BeautifulSoup
import datetime as dt

class SearchHandler:
    def __init__(self):
        pass

    def connect_search(self, address, path, VERBOSE=False):
        full_path = address + path

        if VERBOSE:
            print("Connecting to Ebay...")
            print(f"Searching Path : {full_path}\n")

        response = requests.get(full_path)

        if VERBOSE:
            print(f"CONNECTION Result: {response}")

        if response.status_code == 200:
            return response.text
        raise Exception(f"Error in Ebay Search request - Response: {response}")

        '''
        try:
            response = requests.get(full_path)
            if VERBOSE:
                print(f"CONNECTION Result: {response}" )
            html_text = BeautifulSoup(response.text, "html.parser")
            if VERBOSE:
                print("Request Complete.")
            return html_text
            
        except Exception as ex:
            print("Failure in Connect.py\nUnable to connect to Ebay.")
            print(ex, "-------------------------\n")
            return None
        '''


if __name__ == "__main__":
    print("** Testing search_handler.py **")
    address = "https://www.ebay.com/sch/i.html?"
    p = "_nkw=amazing+spider-man+%23121+cgc+9.0"

    sm = SearchHandler()
    result = sm.connect_search(address, p, True)
    print(result)

