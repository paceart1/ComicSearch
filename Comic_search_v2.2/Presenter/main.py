from Presenter.results_presenter import ResultsPresenter


class Presenter:
    def __init__(self, Main_View, Model):
        print("Starting application")
        self.model = Model
        self.view = Main_View

        self.comic_results_presenter = ResultsPresenter(self.view.comic_results_view, self.model.Comics,
                                                        show_empty=False,  include_buy_now=True)
        self.card_results_presenter = ResultsPresenter(self.view.card_results_view, self.model.Cards,
                                                       show_empty=False,  include_buy_now=True)
        print("Initializing Comic Search Data:")
        self.comic_results_presenter.update_results(print_message=True)
        print("Initializing Card Search Data:")
        self.card_results_presenter.update_results(print_message=True)


    def start(self):
        self.view.start_mainloop()

