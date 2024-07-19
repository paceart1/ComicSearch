import time

from View.Results.results_view import ResultsView
from Model.result_item import ResultItem

class ResultsPresenter:
    def __init__(self, result_view, model, show_empty=True, include_buy_now=True):
        self.include_buy_now = include_buy_now
        self.show_empty = show_empty
        self.view = result_view
        self.model = model
        self._bind_behaviors()
        self.remaining_hours = 48 #TODO: Hard Coded!

    def _bind_behaviors(self):
        self.view.heading.refresh_button.configure(command=self.update_results)


    def update_results(self, print_message=True):
        self.view.results.clear()
        #self.view.loading_message.grid(row=2, column=0, sticky="s")
        self.view.results.update() #reprint gui

        searches = self.model.get_all_search_data()
        message ="Loading"
        print(message, end="")
        for s in searches:

            if print_message:
                #message += "."
                print(".", end="")


            path = self.model.get_search_path(s.id, self.remaining_hours)

            #print(f"{s}\n   https://www.ebay.com/sch/i.html?{path}")
            results = self.model.get_search_results(path)

            # TODO: This is temp filtering
            count = 0
            while count < len(results):

                #Blocklist filter
                if results[count]['item_id'] in s.item_block_list:
                    results.pop(count)
                    continue

                # Time remaining filter (both blocks)
                if self.include_buy_now is True:
                    if results[count]['rem_time'] is None:
                        count += 1
                        continue

                if results[count]['rem_time'] is None:
                    results.pop(count)
                elif "d" in results[count]['rem_time']:
                    results.pop(count)
                else:
                    count += 1

            # TODO: End temp filtering

            # Filter out empty topics
            if self.show_empty is False and len(results) == 0:
                continue

            self.view.results.add_topic(s.id, f"{s.id}-{s.name}", s.number)
            for r in results:
                #image = r['img_src'] #ToDO : Create method of getting and saving image
                self.view.results.add_item_to_topic(s.id,
                                                    desc=r['title'],
                                                    price=r['price'],
                                                    shipping=r['shipping'],
                                                    time=r['rem_time'],
                                                    link=r['link'],
                                                    img=None)

            self.view.results.update()

        if print_message:
            print("\ncomplete!\n")





