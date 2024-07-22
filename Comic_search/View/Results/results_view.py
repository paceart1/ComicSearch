import customtkinter as ctk
from View.Results.topic import Topic
from View.Messengers.loading_messenger import LoadingMessenger


class ResultsHeading(ctk.CTkFrame):
    def __init__(self, parent, heading="Result:", radius=2):
        super().__init__(parent, corner_radius=radius)

        # create grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0,1,2,3), weight=1)

        self.lbl_title = ctk.CTkLabel(self, text=heading, text_color="black", font=("Arial",18, 'bold'))
        self.lbl_title.grid(row=0, column=0, padx=10, pady=(5, 5), sticky="nsw")

        self.refresh_button = ctk.CTkButton(self, text=u'\u27F3',width=30, height=30, font=("Arial",30,'bold'))
        self.refresh_button.grid(row=0, column=3, sticky="ne")

    def set(self, new_title):
        self.lbl_title.configure(text=new_title)


class ResultsManager(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=2, fg_color="light blue")
        self._scrollbar.configure(width=20)
        self.columnconfigure(0, weight=1, uniform="Silent_Creme")
        self.topics = {}

    def add_topic(self, topic_id, description, number):
        self.topics[topic_id] = Topic(self, topic_id, f"{description} #{number}") #TODO: TEMP
        self.topics[topic_id].grid(row=self.topics_count(), column=0, padx=2, pady=8, sticky="new")


    def add_item_to_topic(self, topic_id, desc, price, shipping, time, link, img=None):
        if topic_id not in self.topics.keys():
            print(f"{topic_id} does not exist in topics")
            return

        self.topics[topic_id].add_item(desc, price, shipping, time, link, img)

    def clear(self):
        for child in self.winfo_children():
            child.destroy()
        self.topics = {}

    def topics_count(self):
        return len(self.topics)


class ResultsView(ctk.CTkFrame):
    def __init__(self, parent, heading="title", color="transparent"):
        super().__init__(parent, corner_radius=2, fg_color=color)
        self.columnconfigure(0, weight=1, uniform="Silent_Creme")
        self.rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1, uniform="Silent_Creme")

        self.heading = ResultsHeading(self, heading)
        self.heading.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")

        self.results = ResultsManager(self)
        self.results.grid(row=1, column=0, rowspan=10, padx=2, pady=2, sticky="nsew")



if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry(f"{600}x{400}+{200}+{100}")
    root.title("TEST WINDOW")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    test_frame = ctk.CTkFrame(root, fg_color="light blue")
    test_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    test_frame.columnconfigure(0, weight=1, uniform="Silent_Creme")

    view = ResultsView(test_frame, "black")
    view.grid(row=1, column=0, rowspan=4, columnspan=4, padx=5, pady=5, sticky="nsew")
    view.heading.set("Search Results")
    view.results.add_topic("1001", "The Incredible Hulk", "181")
    view.results.add_topic("1004", "The Amazing Spider-man", "300")

    view.results.add_item_to_topic("1001",
                                   "Hulk 181 VF CGC 8.0",
                                   4700,
                                   14.99,
                                   "1d 4h 29m",
                                   "www.ebay.com")

    #r = ResultItem(test_frame, "Hulk 181", 6500, 12.99, "1d 3h 24m")
    #r.grid(row=0, column=0, padx=2, pady=2, sticky="new")

    root.mainloop()


