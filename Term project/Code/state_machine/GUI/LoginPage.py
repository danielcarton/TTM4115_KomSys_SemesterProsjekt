
class LoginPage():
    app = None
    def __init__(self, app) -> None:
        self.app = app
        pass

    def init(self, callback):
        self.app.startFrame("Login")
        self.app.addLabelOptionBox("Role", ['TA', 'Team 1', 'Team 2'], 0, 0, 2)
        self.app.addLabel("Name", "Name", 1, 0)
        self.app.entry("nameinput", "", 1, 1)
        self.app.addButton("Confirm", lambda: self.on_button_click(callback=callback), 2, 0, 2)
        self.app.stopFrame()

    def on_button_click(self, callback):
        #Do something with the driver
        name = self.app.getEntry("nameinput")
        role = self.app.getOptionBox("Role")
        callback(name, role)
