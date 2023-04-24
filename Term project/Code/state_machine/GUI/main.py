from appJar import gui
from LoginPage import LoginPage
from MainPage import MainPage
from Button import Button

class TimerGUI():
    def __init__(self):
        self.app = gui()
        self.app.setSize("fullscreen")
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
        button = Button(self.app, "Login", 200, 200, on_button_pressed)
        self.app.button("Quit", on_button_pressed)
        self.app.stopFrame()

        loginPage = LoginPage(self.app)
        loginPage.setup()

        mainPage = MainPage(self.app, ['General', 'TA', 'Group 1'])
        mainPage.AddMainPage()



        self.app.stopFrameStack()

timer_gui = TimerGUI()

timer_gui.app.go()