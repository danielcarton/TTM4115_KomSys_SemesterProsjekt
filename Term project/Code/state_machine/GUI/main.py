from appJar import gui
from MainPage import MainPage

class TimerGUI():
    def __init__(self):
        self.app = gui()
        self.app.setSize(500, 800)
        self.setup()
  

    def setup(self):
        def on_button_pressed(btn):
            if btn == "Login":
                self.app.selectFrame("Pages",num=1)
            elif btn == "Quit":
                quit()
            elif btn == "Confirm":
                self.app.selectFrame("Pages",num=2)

        self.app.startFrameStack("Pages", start=0)

        self.app.startFrame()
        self.app.button("Login", on_button_pressed)
        self.app.button("Quit", on_button_pressed)
        self.app.stopFrame()

        self.app.startFrame()
        self.app.entry("name")
        self.app.button("Confirm", on_button_pressed)
        self.app.stopFrame()

        mainPage = MainPage()
        mainPage.AddMainPage(self.app)



        self.app.stopFrameStack()

timer_gui = TimerGUI()

timer_gui.app.go()