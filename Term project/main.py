from appJar import gui

app = gui()
app.setSize(500, 500)
app.addLabelEntry('Text')
app.setEntry('Text', 'Frank')

def on_button_pressed(title):
    print('Button with title "{}" pressed!'.format(title))
    text = app.getEntry('Text')
    print('And the current text field shows "{}".'.format(text))
    

app.addButton("Press Button", on_button_pressed)
app.go()