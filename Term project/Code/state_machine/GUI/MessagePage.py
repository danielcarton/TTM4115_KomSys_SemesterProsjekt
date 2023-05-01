from appJar import gui


class MessagePage():

    channels = []
    app = None
    asd = None
    messages = {}
    selectedChannel = "General"

    def __init__(self, app : gui, channels):
        self.channels = channels
        self.app = app
        pass

    def init(self, exitCallback, sendCallback):
        index = 0
        with self.app.frame("Messages", row = 0, column=0, rowspan=3):
            for i in self.channels:
                self.app.addButton(i, lambda btn=i : self.selectGroup(btn))
                index += 1
                self.app.addHorizontalSeparator(row=index, column=0, colspan=1, colour="gray")
                index += 1
            
        self.app.addVerticalSeparator(row=0, column=1, rowspan=index, colour="gray")

        self.app.addNamedButton("Go back", "QuitFromMainView", exitCallback, row=0, column=3, colspan=1)
        self.app.addLabel(title="header", text=self.selectedChannel, row=0, column=2)
        self.app.entry("chatinput", "", row=3, column=2)
        self.app.addButton("send", lambda : sendCallback(client=self.selectedChannel, userdata=None, msg=self.app.getEntry("chatinput")), row=3, column=3)

    def selectGroup(self, channel):
        self.selectedChannel = channel
        self.app.setLabel("header", self.selectedChannel)
        self.removeMessages()
        self.displayMessages()

    def removeMessages(self):
         if self.asd != None:
            self.app.removeWidgetType(48, "ScrollPane")
            self.asd = None

    def displayMessages(self):
        if self.messages.get(self.selectedChannel) == None:
            self.messages[self.selectedChannel] = []
    
        with self.app.scrollPane("ScrollPane", row=1, column=2, colspan=2, rowspan=1, sticky="NEW", stretch="COLUMN") as self.asd:
            for index in range(len(self.messages[self.selectedChannel])):
                with self.app.labelFrame("message{number}".format(number=index), stretch="COLUMN", sticky="NEW", colspan=2, column=0, row=index):
                    self.app.setSticky("NEW")
                    self.app.setStretch("COLUMN")
                    self.app.addLabel("l{number}".format(number=index), self.messages[self.selectedChannel][index]["sender"], column=0, row= 0)
                    self.app.addMessage("l{number}".format(number=index), self.messages[self.selectedChannel][index]["message"], column=1, row=1)
                    self.app.setMessageBg("l{number}".format(number=index), "khaki")

    def show_message(self, message):
        if self.messages.get(self.selectedChannel) == None:
            self.messages[self.selectedChannel] = []
        self.messages[self.selectedChannel].append(message)

        topic = str(message["topic"])
        topic = topic.replace("ttm4115/", "")
        if topic == "":
            return
        if topic != self.selectedChannel:
            return

        self.removeMessages()
            
        self.displayMessages()
               