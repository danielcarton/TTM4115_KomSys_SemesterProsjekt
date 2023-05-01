class Tasks():

    tasks = []
    selectedTask = 0
    taskView = None

    def __init__(self, app ):
        self.app = app
        self.tasks.append({'name' : 'task1', 'payload' : '{"done : 0"}'})
        self.tasks.append({'name' : 'task2', 'payload' : '{"done : 0"}'})
        self.tasks.append({'name' : 'task3', 'payload' : '{"done : 0"}'})
        self.tasks.append({'name' : 'task4', 'payload' : '{"done : 0"}'})

    def init(self):
        with self.app.frame("taskslist", row=0, column=0, rowspan=3):
            for index in range(len(self.tasks)):
                self.app.addButton(self.tasks[index]["name"], lambda index=index: self.showTasksPayload(index), row=index),

    def showTasksPayload(self, index):
        self.selectedTask = int(index.replace("task", "")) - 1

        if self.taskView != None:
            self.app.removeWidgetType(38, "taskView")

        with self.app.frame("taskView", row=0, column=1, rowspan=3) as self.taskView:
            self.app.addTextArea(title="payload_area", text=self.tasks[self.selectedTask]["payload"], row=0, column=0, rowspan=3)
            self.app.addButton("Save", self.saveTask, row=3, column=0)
        
    def saveTask(self):
        pass