from factory import get_greeter

if __name__ == "__main__":
    kind = input("Type of greeting (hello/goodbye): ")
    greeter = get_greeter(kind)
    print(greeter.greet())
