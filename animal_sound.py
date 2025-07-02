class animal:
    def speak(self):
        print("each animal speak own language")
class dog(animal):
    def speak(self):
        print("bark")

    
    
class cat(animal):
    def speak(self):
        print("meow")
    
class cow(animal):
    def speak(self):
        print('MOO')

a=cat()
a.speak()
n=cow()
n.speak()
