from stmpy import Machine, Driver
from LoginPage import LoginPage
from appJar import gui

from MainPage import MainPage
from MessagePage import MessagePage
from Tasks import Tasks
from mqtt_component import MQTT_Client

class OurState():

    user = None
    is_user_admin = False

    subscribed = []
    chosen_channel = None
    chose_message = None
    app = None
    mqtt = None
    login_ui = None
    home_ui = None
    messaging_ui = None
    task_view_hl_ui = None
    task_view_ll_ui = None
    task_edit_hl_ui = None
    task_edit_ll_ui = None
    access_hl_ui = None
    access_ll_ui = None
    edit_access_ui = None
    app = None

    def __init__(self) -> None:
        self.app = gui()
        self.app.setSize("fullscreen")
        self.mqtt = MQTT_Client()


    def show_login_page(self):
        """
        Show login win
        """
        # TODO
        # show login page and pass on_login as callback
        if self.login_ui == None:
            self.login_ui = LoginPage(self.app)
        self.login_ui.init(self.on_login)


    def on_login(self):
        # set user
        #self.user = username
        #self.is_user_admin = is_admin
        # trigger login transaction
        
        self.stm.send('login')

    def hide_login_page(self):
        """
        Hide login window
        """
        self.app.removeAllWidgets()

    def show_home_page(self):
        """
        Show home window
        """
        # TODO
        # show home page and pass callbacks for button
        if self.home_ui == None:
            self.home_ui = MainPage(self.app)

        self.home_ui.init(self.on_messaging_button,
                          self.on_tasks_button,
                          self.on_access_button)

    def on_messaging_button(self):
        # trigger messaging transaction
        self.stm.send('messaging')

    def on_tasks_button(self):
        # trigger tasks transaction
        self.stm.send('tasks')

    def on_access_button(self):
        # trigger access transaction
        self.stm.send('access')

    def hide_home_page(self):
        """
        Hide home window
        """
        self.app.removeAllWidgets()

    def on_exit(self):
        self.stm.send('exit')

    def show_messaging_page(self):
        """
        Show messaging window
        """
        if self.messaging_ui == None:
            self.messaging_ui = MessagePage(self.app, ['TA', 'Group1'])
        self.messaging_ui.init(self.on_exit)
        self.messaging_ui.show_message({'sender' : 'haakon', 'message' : "asdsagdsad"})

    def send_message(self, message):
        """
        """
        # TODO
        # send messagfe to mqtt

    def on_message(self, message):
        """
        """
        # TODO
        # display message in ui
        self.messaging_ui.show_message(message)

    def hide_messaging_page(self):
        """
        Hide messaging window
        """
        self.app.removeAllWidgets()

    def task_view_credential_check(self) -> str:
        """
        Return name of task view state depending on user's access
        """
        if self.is_user_admin:
            return 'tasks_view_hl_state'
        else:
            return 'tasks_view_ll_state'

    def access_view_credential_check(self) -> str:
        """
        Return name of access view state depending on user's access
        """
        if self.is_user_admin:
            return 'access_view_hl_state'
        else:
            return 'access_view_ll_state'

    def subscribe_topics(self):
        for channel in self.subscribed:
            self.mqtt.subscribe(channel)
        # TODO

    def unsubscribe_topics(self):
        for channel in self.subscribed:
            self.mqtt.unsubscribe(channel)
        # TODO
    
    def on_edit(self):
        self.stm.send('edit')

    def show_task_hl_page(self):
        """
        Show the tasks for the high level access
        """
        # TODO
        # show task HL page and pass callback to edit tasks HL and to exit
        if self.task_view_hl_ui == None:
            self.task_view_hl_ui = Tasks(self.app)
        self.task_view_hl_ui.init()

    def receive_messages_on_all_topics(self, message, topics):
        """
        """
        # TODO

    def update_tasks_from_relevant_topic(self, tasks, topics):
        """
        """
        # TODO

    def hide_task_hl_page(self):
        """
        """
        # TODO
        self.task_view_hl_ui.exit()

    def show_task_ll_page(self):
        """
        """
        # TODO
        # show task LL page and pass callback to edit tasks HL and to exit
        self.task_view_ll_ui.init(self.on_edit, self.on_exit)

    def receive_messages_on_single_topic(self, message, topic):
        """
        """
        # TODO

    def update_tasks_from_single_topic(self, tasks, topic):
        """
        """
        # TODO

    def hide_task_ll_page(self):
        """
        """
        # TODO
        self.task_view_ll_ui.exit()

    def show_edit_task_view_hl(self):
        """
        """
        # TODO
        # show task edit HL page and pass callback to exit
        self.task_edit_hl_ui.init(self.on_exit)

    def hide_edit_task_view_hl(self):
        """
        """
        # TODO
        self.task_edit_hl_ui.exit()

    def send_all_tasks_to_relevant_topic(self, tasks, topics):
        """
        """
        # TODO

    def show_edit_task_view_ll(self):
        """
        """
        # TODO
        # show task edit HL page and pass callback to exit
        self.task_edit_ll_ui.init(self.on_exit)

    def hide_edit_task_view_ll(self):
        """
        """
        # TODO
        self.task_edit_ll_ui.exit()

    def send_all_tasks_to_single_topic(self, tasks, topic):
        """
        """
        # TODO

    def show_access_hl_page(self):
        """
        """
        # TODO
        # show access HL page and pass callback to exit
        self.access_hl_ui.init(self.on_exit)
        # TODO add callback to mqtt => on_access_message

    def on_access_message(self, message):
        """
        """
        # TODO

    def hide_access_hl_page(self):
        """
        """
        # TODO
        self.access_hl_ui.exit()

    def show_access_ll_page(self):
        """
        """
        # TODO
        # show access LL page and pass callback to exit
        self.access_ll_ui.init(self.on_exit)
        # TODO add callback to mqtt => on_access_message

    def hide_access_ll_page(self):
        """
        """
        # TODO
        self.access_ll_ui.exit()

    def receive_access_message(self, access_message):
        """"
        """
        # TODO

    def update_own_access(self, new_access):
        """
        """
        # TODO

    def show_edit_access_page(self):
        """
        """
        # TODO
        # show edit access page and pass callback to exit
        self.edit_access_ui.init(self.on_exit)

    def hide_edit_access_page(self):
        """
        """
        # TODO
        self.edit_access_ui.exit()

    def send_access_changes(self, new_access):
        """"""
        """"""
        # TODO


