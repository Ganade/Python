class Date:

    def __init__(self, day, month, year):
        self.day = day
        self. month = month
        self. year = year

    def formatted_date(self):
        print(f"{self.day}/{self.month}/{self.year}")


# d = Date(21, 11, 2007)
# d. formatted_date()
