class MainPage():
    app = None
    def __init__(self, app) -> None:
        self.app = app

    def init(self):
        with self.app.frame("MainView"):
            self.app.addButtons(["Messages", "Tasks", "Access"], None)