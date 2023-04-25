from appJar import gui


class MessagePage():

    channels = []
    app = None
    asd = None
    messages = []

    def __init__(self, app : gui, channels):
        self.channels = channels
        self.app = app
        pass

    def init(self, exitCallback):
        index = 0
        with self.app.frame("Messages", row = 0, column=0, rowspan=3):
            for i in self.channels:
                self.app.addLabel(i, i, index, 0)
                index += 1
                self.app.addHorizontalSeparator(row=index, column=0, colspan=1, colour="gray")
                index += 1
            
        self.app.addVerticalSeparator(row=0, column=1, rowspan=index, colour="gray")

        self.app.addNamedButton("Quit", "QuitFromMainView", self.temp, row=0, column=2, colspan=1)
        self.app.entry("chatinput", "", row=3, column=2)
        self.app.addButton("send", None, row=3, column=3)

    def temp(self):
        self.show_message({"sender" : "Haakon", "message" : "hei"})
        
    def show_message(self, message):
        self.messages.append(message)
        if self.asd != None:
            self.app.removeWidgetType(48, "ScrollPane")
            
        with self.app.scrollPane("ScrollPane", row=1, column=2, colspan=2, rowspan=1, sticky="NEW", stretch="COLUMN") as self.asd:
            for index in range(len(self.messages)):
                with self.app.labelFrame("message{number}".format(number=index), stretch="COLUMN", sticky="NEW", colspan=2, column=0, row=index):
                    self.app.setSticky("NEW")
                    self.app.setStretch("COLUMN")
                    self.app.addLabel("l{number}".format(number=index), self.messages[index]["sender"], column=0, row= 0)
                    self.app.addMessage("l{number}".format(number=index), self.messages[index]["message"], column=1, row=1)
                    self.app.setMessageBg("l{number}".format(number=index), "khaki")
               