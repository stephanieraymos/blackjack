class Monster:
    title = "scarer" # auto initialized with each instance

    def __init__(self, name, color):
        self.name = name  
        self.color = color
        # Instance attribute (apply to specific instance of this class)

    def scare(self, sound):
        print(self.name + "says" + sound)

    def drink(self, drink):
        print(self.name + "wants to sip on some" + drink)

    # drink(tea)