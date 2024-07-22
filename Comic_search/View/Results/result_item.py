import customtkinter as ctk
import webbrowser
from PIL import Image


class ResultItem(ctk.CTkFrame):
    def __init__(self, parent, description, price, shipping, time, link, img=None):
        super().__init__(parent, corner_radius=10, cursor= "hand2")

        #self.grid(row=0, column=1, rowspan=1, columnspan=1, padx=(5,5), pady=5, sticky="nse")
        #self.columnconfigure(0, weight=1)
        #self.columnconfigure(1, weight=5)

        self.lbl_image = ctk.CTkLabel(self, text="", fg_color="black", corner_radius=4, width=40, height=40)
        self.lbl_image.grid(row=0, column=0, rowspan=3, padx=(5,0), pady=5, sticky="nsw")

        self.lbl_title = ctk.CTkLabel(self, text=description, fg_color="transparent", wraplength=450,
                                      justify="left",text_color="black", font=("Arial",12, 'bold'))
        self.lbl_title.grid(row=0, column=1, padx=10, pady=(5, 0), sticky="nw")

        #TODO: Refactor how details are placed.  Cuts off when min state.  Make individual labels
        self.lbl_details = ctk.CTkLabel(self, text=f"Price: {price}\tShipping: {shipping}\t\tTime Remaining: {time}",
                                      fg_color="transparent",
                                      text_color="black", font=("Arial", 12, 'bold'))
        self.lbl_details.grid(row=1, column=1, padx=10, pady=(0, 0), sticky="new")

        self.bind("<Button-1>", lambda e: self.open_link(link))
        self.lbl_title.bind("<Button-1>", lambda e: self.open_link(link))
        self.lbl_details.bind("<Button-1>", lambda e: self.open_link(link))
        self.lbl_image.bind("<Button-1>", lambda e: self.open_link(link))

    #TODO: Move Binding and behavior to presenter !!!
    def open_link(self, url):
        lead = "https://"
        if lead not in url:
            url = lead + url
        print(f"Attempting to connect: {url}")
        webbrowser.open_new(url)


if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry(f"{600}x{400}+{200}+{100}")
    root.title("TEST WINDOW")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    test_frame = ctk.CTkFrame(root, fg_color="light blue")
    test_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    test_frame.columnconfigure(0, weight=1, uniform="Silent_Creme")

    r = ResultItem(test_frame, "Hulk 181", 6500, 12.99, "1d 3h 24m")
    r.grid(row=0, column=0, padx=2, pady=2, sticky="new")

    root.mainloop()