class Controller:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

    def save(self, title):
        self.model.title = title
        self.model.title_search()