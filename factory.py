from greetings.hello import Hello
from greetings.goodbye import Goodbye

def get_greeter(kind):
    if kind == "hello":
        return Hello()
    elif kind == "goodbye":
        return Goodbye()
    else:
        raise ValueError("Unknown greeting type")
