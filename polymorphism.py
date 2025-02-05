#method overridding
class animal:
    def sound(self):
        print("Make sound ")

class Lion(animal):
    def sound(self):
        print("It Roars...... ")

class Dog(animal):
    def sound(self):
        print("It  barks..... ")


l=Lion()
l.sound()
D=Dog()
D.sound()




#Another example
class Bank:
    def Interest(self):
        return 6.5

class SBI(Bank):
    def Interest(self):
        return 5.5

class Axis(Bank):
    def Interest(self):
        return 4.8
    
class Cana(Bank):
    def Interest(self):
        return 5.0

s=SBI()
A=Axis()
C=Cana()
print(f'the interest rate is SBI is{s.Interest()}')
print(f'the interest rate is Axis is{A.Interest()}')
print(f'the interest rate is Cana is{C.Interest()}')






