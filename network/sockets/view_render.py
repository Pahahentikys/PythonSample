def index():
    with open("views/index.html") as view:
        return view.read()

def more():
    with open("views/more.html") as view:
        return view.read()