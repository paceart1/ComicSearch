import customtkinter as ctk
from View.Results.result_item import ResultItem


class TopicHeading(ctk.CTkFrame):
    def __init__(self, parent, heading):
        super().__init__(parent, corner_radius=0)
        self.columnconfigure((0,1), weight=1)
        self.lbl_title = ctk.CTkLabel(self, text=heading, text_color="black", font=("Arial", 14, 'bold'))
        self.lbl_title.grid(row=0, column=0, padx=10, pady=(2, 2), sticky="nw")

        #self.lbl_collapse = ctk.CTkLabel(self, cursor= "hand2", text=" v ", text_color="dark grey", font=("Arial", 24, 'bold'))
        #self.lbl_collapse.grid(row=0, column=1, padx=10, pady=(2, 2), sticky="ne")

    def set_heading(self, heading):
            self.lbl_title.configure(text=heading)


class Topic(ctk.CTkFrame):
    def __init__(self, parent, topic_id, name):
        super().__init__(parent, corner_radius=0, fg_color="transparent")
        self.columnconfigure(0, weight=1, uniform="Silent_Creme")

        self.heading = TopicHeading(self, name)
        self.heading.grid(row=0, column=0, padx=0, pady=2, sticky="new")
        self.id = topic_id
        self.items = []
        self.items_hidden_state = False

        self.heading.bind("<Button-1>", lambda e: self.on_hide_click())

    def add_item(self, desc, price, shipping, time, link, img=None):
        r = ResultItem(self, desc, price, shipping, time, link, img)
        self.items.append(r)
        r.grid(row=self.item_count(), column=0, padx=(20, 0), pady=1, sticky="new")

    def on_hide_click(self):
        if self.items_hidden_state is True:
            self.items_hidden_state = False
            self.show_items()
            return
        self.items_hidden_state = True
        self.hide_items()

    def hide_items(self):
        print("Hiding items")
        for ii in range(len(self.items)):
            self.items[ii].grid_remove()

    def show_items(self):
        for ii in range(len(self.items)):
            row_placement = ii + 1
            self.items[ii].grid(row=row_placement, column=0, padx=(20, 0), pady=1, sticky="new")



    def item_count(self):
        return len(self.items)


if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry(f"{600}x{400}+{200}+{100}")
    root.title("TEST WINDOW")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    test_frame = ctk.CTkFrame(root, fg_color="light blue")
    test_frame.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")
    test_frame.columnconfigure(0, weight=1, uniform="Silent_Creme")

    topics = {}
    topics["1001"] = Topic(test_frame, "1001", "Test Search Name 1")
    topics["1001"].grid(row=0, column=0, padx=2, pady=2, sticky="new")
    topics["1002"] = Topic(test_frame, "1002", "Test Search Name 2")
    topics["1002"].grid(row=1, column=0, padx=2, pady=2, sticky="new")

    topics["1002"].add_item("Hulk 181", 6500.99, 12.99, "12h 46m", None)
    topics["1002"].add_item("Hulk 180", 612.99, "Free", "4h 12m", None)



    root.mainloop()




