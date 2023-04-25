class MainPage():
    app = None
    def __init__(self, app) -> None:

        self.app = app

    def init(self, messageCallback, taskCallback, accessCallback):
        with self.app.frame("MainView"):
            self.app.addButtons(["Messages", "Tasks", "Access"], [messageCallback, taskCallback, accessCallback])