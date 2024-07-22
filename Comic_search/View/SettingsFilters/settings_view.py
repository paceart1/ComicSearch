import customtkinter as ctk

class Setting(ctk.CTkFrame):
    def __init__(self, parent, text, widget):
        super().__init__(parent)
        self.label = ctk.CTkLabel(self, text=text)
        self.label.grid(row=0, column=0, padx=(5, 0), pady=5, sticky="nw")
        self.widget = widget(self, text="", command=None,
                                    onvalue="on", offvalue="off")
        self.widget.grid(row=0, column=1, padx=(50, 0), pady=5, sticky="ne")


class SettingsView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        #self.rowconfigure(1, weight=1)
        #self._scrollbar.configure(width=20)

        self.settings = []
        for ii in range(5):
            w = ctk.CTkSwitch
            s = Setting(self, f"Setting {ii}", w)
            s.grid(row=ii, column=0, rowspan=1, padx=(5, 0), pady=5, sticky="nsw")
            self.settings.append(s)

        #self.lbl_test = ctk.CTkLabel(self, text="settings TESTING123", fg_color="yellow", corner_radius=4, width=40, height=40)
        #self.lbl_test.grid(row=0, column=0, rowspan=1, padx=(5, 0), pady=5, sticky="nsw")

