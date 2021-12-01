class Controller:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

    def save(self, title, date):
        self.model.title = title
        self.model.date = date

        if self.model.title == None:
            date_input = self.model.date_search()
            self.view.receiving(date_input)  

        elif self.model.date == None:
            title_input = self.model.title_search()
            self.view.receiving(title_input)


    # def send_back(self, movies):
    #     self.model.
    #     self.view.