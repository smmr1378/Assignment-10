class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return f"{self.hour}:{self.minute}"

hour = int(input("Enter the hour: "))
minute = int(input("Enter the minute: "))

time = Time(hour, minute)
print(time)