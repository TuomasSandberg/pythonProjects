class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    def swim(self):
        print("mowing in water")

    def breathe(self):  # inherit a function and modify it
        super().breathe()
        print("doing this under water")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
