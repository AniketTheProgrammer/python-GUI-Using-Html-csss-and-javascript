import eel

eel.init("web")

@eel.expose
def helloWorld():
    return 'Hello world from python'

eel.start("index.html")    