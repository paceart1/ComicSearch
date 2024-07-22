import customtkinter as ctk
from View import assets

class Root(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("")
        #self.iconbitmap("assets/spiderman.ico")
        self.geometry(f"{1000}x{540}+{200}+{100}")
        self.minsize(300, 200)


if __name__ == "__main__":
    root = Root()
    root.mainloop()
