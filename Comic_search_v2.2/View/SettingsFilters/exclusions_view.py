import customtkinter as ctk


class ExclusionsView(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        #self.hid_scroll()

        for i in range(50):
            self.lbl_test = ctk.CTkLabel(self, text=i, corner_radius=4, width=40, height=40)
            self.lbl_test.grid(row=i, column=0, padx=(5, 0), pady=5, sticky="nsew")

        self.test()

    def test(self):
        print(self._scrollbar.cget("height"))

    def show_scroll(self):
        self._scrollbar.grid()

    def hid_scroll(self):
        self._scrollbar.grid_remove()