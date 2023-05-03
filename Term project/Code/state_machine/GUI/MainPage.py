class MainPage():
    app = None
    def __init__(self, app) -> None:

        self.app = app
        self.stm_component = None

    def init(self, messageCallback, taskCallback, accessCallback):
        with self.app.frame("MainView"):
            self.app.addButtons(["Messages", "Tasks"], [messageCallback, taskCallback])
            self.app.addButtons(["Cancel", "Ask for help"], [lambda: self.cancel, lambda: accessCallback(True)])

    def cancel():
        self.stm.send('cancel')
        #Needs further implementation

  

