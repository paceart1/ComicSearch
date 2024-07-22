import customtkinter as ctk

class LoadingMessenger(ctk.CTkFrame):
    def __init__(self, parent, message="Loading..."):
        super().__init__(parent, corner_radius=0, fg_color="transparent")
        self.message = message
        self.message_lbl = ctk.CTkLabel(self, text=self.message, font=("Arial", 36, 'bold'))
        self.message_lbl.grid(row=0, column=0, padx=(100, 100), pady=(80, 80), sticky="nsew")

