from View.root import Root
from View.Results import results_view
from View.SettingsFilters import settings_filters_view

import customtkinter as ctk


class MainHeading(ctk.CTkFrame):
    def __init__(self, parent, heading):
        super().__init__(parent, corner_radius=0)

        # create grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.lbl_title = ctk.CTkLabel(self, text=heading, text_color="black", font=("Arial", 30, 'bold'))
        self.lbl_title.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="nsw")

        #self.textbox.grid(row=0, column=0, columnspan=2, padx=5, pady=(20, 0), sticky="nsew")

class View:
    def __init__(self):
        self.root_window = Root()
        # create root grid system
        #self.root_window.grid_rowconfigure((1,2,3,4,5,6,7,8,9), weight=1, uniform="Silent_Creme")
        self.root_window.grid_rowconfigure(1, weight=1)
        self.root_window.grid_columnconfigure(0, weight=1)

        head = MainHeading(parent=self.root_window, heading="Cool Comics")
        head.grid(row=0, column=0, padx=2, pady=(5,0), sticky="nsew")

        self.base_container = ctk.CTkTabview(self.root_window, fg_color="transparent", anchor=ctk.NE)
        self.base_container.grid(row=1, column=0, padx=5, pady=(2,5), sticky="nsew")
        #self.base_container.rowconfigure((0,1,2), weight=1)

        #head = MainHeading(parent=self.base_container, heading="Cool Comics")
        #head.grid(row=1, column=0, padx=2, pady=(5, 0), sticky="new")

        # init tabs
        self.comics_tab = self.base_container.add("Comics")
        self.cards_tab = self.base_container.add("Cards")

        # Configure Tabs
        self.comics_tab.configure(fg_color="transparent")
        self.comics_tab.columnconfigure((0,1,2), weight=1)
        self.comics_tab.rowconfigure(0, weight=1)

        self.cards_tab.configure(fg_color="transparent")
        self.cards_tab.columnconfigure((0, 1, 2), weight=1)
        self.cards_tab.rowconfigure(0, weight=1)

        self.base_container._segmented_button.configure(font=("Arial",20,'bold'))
        #self.base_container._segmented_button.lift()
        #self.base_container._segmented_button.grid(row=0, column=0, sticky="n")

        # Add Comics View to Tab
        self.comic_results_view = results_view.ResultsView(self.comics_tab, "Comic Search Results:")
        self.comic_results_view.grid(row=0, columnspan=2, column=0, padx=(0,2), pady=0, sticky="nsew")

        self.comic_filters_view = settings_filters_view.FiltersView(self.comics_tab, "Comic Settings and Filters:")
        #self.comic_filters_view.grid(row=0, column=2,  padx=(2,0), pady=0, sticky="nsew")

        # Add Cards View to Tab
        self.card_results_view = results_view.ResultsView(self.cards_tab, "Card Search Results:")
        self.card_results_view.grid(row=0, columnspan=2, column=0, padx=(0, 2), pady=0, sticky="nsew")

        self.card_filters_view = settings_filters_view.FiltersView(self.cards_tab, "Card Settings and Filters")
        #self.card_filters_view.grid(row=0, column=2, padx=(2, 0), pady=0, sticky="nsew")

        self._filter_control = ctk.CTkLabel(self.base_container,fg_color="light grey",
                                            cursor="hand2", text=">", font=("Arial",30,'bold'))
        self._filter_control.bind("<Button-1>", lambda e: self.change_filter_view_state())
        self._filter_control.grid(row=3, column=1, ipadx=5, ipady=5, sticky="")

        self._filter_view_state = True
        self.show_filters()

        #self.show_filters()


    def change_filter_view_state(self):
        if self._filter_view_state:
            self.hide_filters()
        else:
            self.show_filters()

    def show_filters(self):
        self.root_window.geometry(f"{1000}x{540}+{200}+{100}")

        self.card_results_view.grid(row=0, columnspan=2, column=0, padx=(0, 2), pady=0, sticky="nsew")
        self.comic_results_view.grid(row=0, columnspan=2, column=0, padx=(0, 2), pady=0, sticky="nsew")
        self.card_filters_view.grid(row=0, column=2, padx=(2, 0), pady=0, sticky="nsew")
        self.comic_filters_view.grid(row=0, column=2, padx=(2, 0), pady=0, sticky="nsew")

        self._filter_control.configure(text="<")
        self.root_window.update()
        self.card_filters_view.show()
        self.comic_filters_view.show()
        self._filter_view_state = True


    def hide_filters(self):
        self.card_filters_view.hide()
        self.comic_filters_view.hide()
        self.card_filters_view.grid_remove()
        self.comic_filters_view.grid_remove()
        self.root_window.geometry(f"{650}x{540}+{200}+{100}")
        self.card_results_view.grid(row=0, columnspan=3, column=0, padx=(0, 2), pady=0, sticky="nsew")
        self.comic_results_view.grid(row=0, columnspan=3, column=0, padx=(0, 2), pady=0, sticky="nsew")
        self._filter_view_state = False
        self._filter_control.configure(text=">")

    def start_mainloop(self):
        self.root_window.mainloop()

if __name__ == "__main__":
    v = View()
    v.start_mainloop()