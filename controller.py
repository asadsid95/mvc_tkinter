class Controller:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

    def save(self, title, date):
        self.model.title = title
        self.model.date = date

        if self.model.title == None:
            movies_result_date = self.model.date_search()
            self.view.receiving(movies_result_date)  

        elif self.model.date == None:
            movies_result_title = self.model.title_search()
            self.view.receiving(movies_result_title)


    # def send_back(self, movies):
    #     self.model.
    #     self.view.