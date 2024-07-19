import customtkinter as ctk
from View.SettingsFilters.settings_view import SettingsView
from View.SettingsFilters.search_filters_view import SearchFiltersView
from View.SettingsFilters.exclusions_view import ExclusionsView


# Main parent view manager for settings and filters sub-views

class FiltersHeading(ctk.CTkFrame):
    def __init__(self, parent, heading="Heading"):
        super().__init__(parent, corner_radius=2)

        # create grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.lbl_title = ctk.CTkLabel(self, text=heading, text_color="black", font=("Arial",18, 'bold'))
        self.lbl_title.grid(row=0, column=0, padx=10, pady=(5, 5), sticky="nsw")


class FiltersManager(ctk.CTkFrame):
    def __init__(self, parent, color="transparent"):
        super().__init__(parent, corner_radius=2, fg_color=color)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.sections = {"settings": SettingsView(self), "searches": SearchFiltersView(self), "exceptions": ExclusionsView(self)}
        self.options = list(self.sections.keys())

        self.current_selection = self.options[0]
        self.optionbox_var = ctk.StringVar(value=self.current_selection)
        self.optionbox = ctk.CTkOptionMenu(master=self,
                                                values=self.options,
                                                variable=self.optionbox_var,
                                                command= lambda e: self.show_section())

        self.optionbox.grid(row=0, column=0, columnspan=1, pady=(5, 7), padx=2, sticky="w")
        self.show_section()

    def show_section(self):
        choice = self.optionbox_var.get()
        if choice not in self.options:
            raise NameError(f"{choice} is not a valid option.")
        self.sections[self.current_selection].grid_remove()
        section = self.sections[choice]
        section.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
        self.current_selection = choice




class FiltersView(ctk.CTkFrame):
    def __init__(self, parent, heading="title", color="transparent"):

        super().__init__(parent, corner_radius=0, fg_color=color)

        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1, uniform="Silent_Creme")

        self.heading = FiltersHeading(self, heading)
        #self.heading.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")

        self.filters = FiltersManager(self, color)
        #self.filters.grid(row=1, column=0, rowspan=10, padx=2, pady=2, sticky="nsew")

        #manager
        #searches = SearchResultsContainer(self)
        #searches.grid(row=1, column=0, rowspan=10, padx=2, pady=2, sticky="nsew")

    def show(self):
        self.heading.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")
        self.filters.grid(row=1, column=0, rowspan=10, padx=2, pady=2, sticky="nsew")

    def hide(self):
        self.heading.grid_remove()
        self.filters.grid_remove()

