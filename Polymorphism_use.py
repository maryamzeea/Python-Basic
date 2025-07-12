#POLYMORPHISM USE

class Device:
    def start(self):
            return "Device is started."

class Mobile(Device):
    def start(self):
        return "Mobile is power on."

class Laptop(Device):
    def start(self):
        return "Laptop is booting up."

d = Device()
m = Mobile()
l = Laptop()

print(f"{d.start()}\n{m.start()}\n{l.start()}")



