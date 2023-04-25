
class LoginPage():
    app = None
    def __init__(self, app) -> None:
        self.app = app
        pass

    def init(self, callback):
        self.app.startFrame("Login")
        self.app.addLabelOptionBox("Role", ['TA', 'Group 1', 'Group 2'], 0, 0, 2)
        self.app.addLabel("Name", "Name", 1, 0)
        self.app.entry("name", "", 1, 1)
        self.app.addButton("Confirm", callback, 2, 0, 2)
        self.app.stopFrame()

    def on_button_click(self):
        #Do something with the driver
        name = self.app.getLabel("Name")
        role = self.app.getOptionBox("Role")
        self.app.selectFrame("Pages",num=2)