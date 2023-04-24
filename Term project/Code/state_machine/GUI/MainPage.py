from appJar import gui


class MainPage():

    channels = []
    app = None

    def __init__(self, app, channels):
        self.channels = channels
        self.app = app
        pass

    def AddMainPage(self):
        with self.app.frame():
            index = 0
            for i in self.channels:
                self.app.addLabel(i, i, index, 0)
                index += 1
                self.app.addHorizontalSeparator(row=index, column=0, colspan=1, colour="gray")
                index += 1
            
            self.app.addVerticalSeparator(row=0, column=1, colspan=1, rowspan=index, colour="gray")

            self.app.addButton("Tasks", None, row=0, column=2, colspan=1)
            self.app.addNamedButton("Quit", "QuitFromMainView", None, row=0, column=3, colspan=1)

            with self.app.scrollPane("ScrollPane", row=1, column=2, colspan=2, rowspan=index-2, sticky="NEW", stretch="COLUMN"):
                for x in range(10):
                    with self.app.labelFrame("message{number}".format(number=x), stretch="COLUMN", sticky="NEW", colspan=2, column=0, row=x):
                        self.app.setSticky("NEW")
                        self.app.setStretch("COLUMN")
                        self.app.addLabel("l{number}".format(number=x), "Sender", column=0, row= 0)
                        self.app.addMessage("l{number}".format(number=x), "heiadsaoidjaodijsdoisajdsaoidjsaoidjsaoidsadoisadjoiajd jk aksjd asidj asoid jaoidjoisajdosajdosa jaoi joisa", column=1, row=1)
                        self.app.setMessageBg("l{number}".format(number=x), "khaki")


            self.app.entry("chatinput", "", index-1, 2)
            self.app.addButton("send", None, index-1, 3)