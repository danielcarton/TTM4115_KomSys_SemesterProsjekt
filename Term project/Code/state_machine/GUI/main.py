from appJar import gui
from LoginPage import LoginPage
from MessagePage import MessagePage
from MainPage import MainPage
from Button import Button
from state_machine_component import OurState
from stmpy import Machine, Driver

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
our_state.app.go()



