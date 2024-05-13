class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

fraction = Fraction(numerator, denominator)
print(fraction)