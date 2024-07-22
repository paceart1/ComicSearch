import customtkinter as ctk

class SearchFiltersView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)


        self.lbl_test = ctk.CTkLabel(self, text="Search TESTING123", fg_color="red", corner_radius=4, width=40, height=40)
        self.lbl_test.grid(row=0, column=0, rowspan=3, padx=(5, 0), pady=5, sticky="nsw")