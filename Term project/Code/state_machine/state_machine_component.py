from stmpy import Machine, Driver


class OurState:

    user = None
    is_user_admin = False

    subscribed = []
    chosen_channel = None
    chose_message = None

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

    # def __init__(self) -> None:

    def show_login_page(self):
        """
        Show login win
        """
        # TODO
        # show login page and pass on_login as callback
        self.login_ui.init(self.on_login)

    def on_login(self, username, password, is_admin):
        # set user
        self.user = username
        self.is_user_admin = is_admin
        # trigger login transaction
        self.stm.send('login')

    def hide_login_page(self):
        """
        Hide login window
        """
        # TODO
        self.login_ui.exit()

    def show_home_page(self):
        """
        Show home window
        """
        # TODO
        # show home page and pass callbacks for button
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
        # TODO
        self.home_ui.exit()

    def on_exit(self):
        self.stm.send('exit')

    def show_messaging_page():
        """
        Show messaging window
        """
        # TODO
        # show messaging page and pass callback to send messages and to exit
        # messaging_ui.init(send_message, on_exit)
        # TODO add callback to mqtt => on_message

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
        # TODO
        self.messaging_ui.exit()

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
        self.task_view_hl_ui.init(self.on_edit, self.on_exit)

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


our_state = OurState()

# transitions
# naming scheme: <from_state>_<to_state>_trans


init_trans = {
    'source': 'initial',
    'target': 'login_state'
}

login_home_trans = {
    'trigger': 'login',
    'source': 'login_state',
    'target': 'home_state'
}

home_messaging_trans = {
    'trigger': 'messaging',
    'source': 'home_state',
    'target': 'messaging_state'
}

messaging_home_trans = {
    'trigger': 'exit',
    'source': 'messaging_state',
    'target': 'home_state'
}

home_tasks_view_trans = {
    'trigger': 'tasks',
    'source': 'home_state',
    'function': 'task_view_credential_check'
}

task_view_hl_task_edit_hl_trans = {
    'trigger': 'edit',
    'source': 'tasks_view_hl_state',
    'target': 'task_edit_hl_state'
}

task_edit_hl_task_view_hl_trans = {
    'trigger': 'send',
    'source': 'task_edit_hl_state',
    'target': 'tasks_view_hl_state'
}

task_view_ll_task_edit_ll_trans = {
    'trigger': 'edit',
    'source': 'tasks_view_ll_state',
    'target': 'task_edit_ll_state'
}

task_edit_ll_task_view_ll_trans = {
    'trigger': 'send',
    'source': 'task_edit_ll_state',
    'target': 'tasks_view_ll_state'
}

tasks_view_hl_home_trans = {
    'trigger': 'exit',
    'source': 'tasks_view_hl_state',
    'target': 'home_state'
}

tasks_view_ll_home_trans = {
    'trigger': 'exit',
    'source': 'tasks_view_ll_state',
    'target': 'home_state'
}

home_access_view_trans = {
    'trigger': 'access',
    'source': 'home_state',
    'function': 'access_view_credential_check'
}

access_view_hl_home_trans = {
    'trigger': 'exit',
    'source': 'access_view_hl_state',
    'target': 'home_state'
}

access_view_ll_home_trans = {
    'trigger': 'exit',
    'source': 'access_view_ll_state',
    'target': 'home_state'
}

acecss_view_hl_access_edit_hl_trans = {
    'trigger': 'edit',
    'source': 'access_view_hl_state',
    'target': 'access_edit_hl_state'
}

access_edit_hl_acess_view_hl_trans = {
    'trigger': 'edit',
    'source': 'access_edit_hl_state',
    'target': 'access_view_hl_state'
}

# states

login_state = {
    'name': 'login_state',
    'entry': 'show_login_page',
    'exit': 'hide_login_page; subscribe_topics'
}

home_state = {
    'name': 'home_state',
    'entry': 'show_home_page',
    'exit': 'hide_home_page'
}

messaging_state = {
    'name': 'messaging_state',
    'entry': 'show_messaging_page',
    'exit': 'hide_messaging_page; unsubscribe_topics'
}

tasks_view_hl_state = {
    'name': 'tasks_view_hl_state',
    'entry': 'show_task_hl_page; receive_messages_on_all_topics; update_tasks_from_relevant_topic',
    'exit': 'hide_task_hl_page'
}

tasks_view_ll_state = {
    'name': 'tasks_view_ll_state',
    'entry': 'show_task_ll_page; receive_messages_on_single_topic; update_tasks_from_single_topic',
    'exit': 'hide_task_ll_page'
}

task_edit_hl_state = {
    'name': 'task_edit_hl_state',
    'entry': 'show_edit_task_view_hl',
    'exit': 'hide_edit_task_view_hl; send_all_tasks_to_relevant_topic'
}

task_edit_ll_state = {
    'name': 'task_edit_ll_state',
    'entry': 'show_edit_task_view_ll',
    'exit': 'hide_edit_task_view_ll; send_all_tasks_to_single_topic'
}

access_view_hl_state = {
    'name': 'access_view_hl_state',
    'entry': 'show_access_hl_page; receive_access_messgae; update_own_access',
    'exit': 'hide_access_hl_page'
}

access_view_ll_state = {
    'name': 'access_view_ll_state',
    'entry': 'show_access_ll_page; receive_access_messagee; update_own_access',
    'exit': 'hide_access_ll_page'
}

access_edit_hl_state = {
    'name': 'access_edit_hl_state',
    'entry': 'show_edit_access_page',
    'exit': 'hide_edit_access_page; send_access_changes'
}

# init machine

machine = Machine(name='our_state_machine',
                  transitions=[
                      init_trans,
                      login_home_trans,
                      home_messaging_trans,
                      messaging_home_trans,
                      home_tasks_view_trans,
                      task_view_hl_task_edit_hl_trans,
                      task_view_ll_task_edit_ll_trans,
                      task_edit_hl_task_view_hl_trans,
                      task_edit_ll_task_view_ll_trans,
                      tasks_view_hl_home_trans,
                      tasks_view_ll_home_trans,
                      home_access_view_trans,
                      access_view_hl_home_trans,
                      access_view_ll_home_trans,
                      acecss_view_hl_access_edit_hl_trans,
                      access_edit_hl_acess_view_hl_trans,
                  ],
                  obj=our_state,
                  states=[
                      login_state,
                      home_state,
                      messaging_state,
                      tasks_view_hl_state,
                      tasks_view_ll_state,
                      task_edit_hl_state,
                      task_edit_ll_state,
                      access_view_hl_state,
                      access_view_ll_state,
                      access_edit_hl_state
                  ])
our_state.stm = machine

driver = Driver()
driver.add_machine(machine)
driver.start()
