#Create a Time class with hours and minutes.
#Overload the + operator to add two Time objects correctly.

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        total_minutes = self.hours * 60 + self.minutes + other.hours * 60 + other.minutes
        new_hours = total_minutes // 60
        new_minutes = total_minutes % 60
        return Time(new_hours, new_minutes)

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}"

t1 = Time(2, 45)
t2 = Time(1, 30)
time_sum = t1 + t2
print(f"Sum of times: {time_sum}")




#Create a Distance class with attributes feet and inches.
#Overload the * operator to multiply the distance by a scalar value.(any numeric value)

class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __mul__(self, scalar):
        total_inches = self.feet * 12 + self.inches
        new_total_inches = total_inches * scalar
        new_feet = int(new_total_inches // 12)
        new_inches = new_total_inches % 12
        return Distance(new_feet, new_inches)
    
    def __str__(self):
        return f"{self.feet} feet, {self.inches} inches"
    
distance1 = Distance(5, 6)
scaled_distance = distance1 * 2.5
print(f"Scaled distance: {scaled_distance}")




#Create a Rectangle class with length and width.
#Overload the == operator to compare the area of two rectangles.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __eq__(self, other):
        return self.area() == other.area()

rect1 = Rectangle(5, 10)
rect2 = Rectangle(7, 7)
print(f"Are rectangles equal in area? {rect1 == rect2}")




