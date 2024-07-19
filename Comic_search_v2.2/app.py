from Model.main import Model
from View.main import View
from Presenter.main import Presenter

class main:
    view = View()
    model = Model()
    presenter = Presenter(view, model)
    presenter.start()


if __name__ == "__main__":
    main()
