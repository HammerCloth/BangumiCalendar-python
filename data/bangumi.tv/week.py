from datetime import datetime, timedelta


class week:
    def __init__(self):
        self.today = datetime.today().date()
        self.w = self.today.weekday()
        self.Monday = self.today - timedelta(self.w)
        self.Tuesday = self.today - timedelta(self.w - 1)
        self.Wednesday = self.today - timedelta(self.w - 2)
        self.Thursday = self.today - timedelta(self.w - 3)
        self.Friday = self.today - timedelta(self.w - 4)
        self.Saturday = self.today - timedelta(self.w - 5)
        self.Sunday = self.today - timedelta(self.w - 6)

    def print(self):
        print(self.Monday.__str__()+" is Monday")
        print(self.Tuesday.__str__() + " is Tuesday")
        print(self.Wednesday.__str__() + " is Wednesday")
        print(self.Thursday.__str__() + " is Thursday")
        print(self.Friday.__str__() + " is Friday")
        print(self.Saturday.__str__() + " is Saturday")
        print(self.Sunday.__str__() + " is Sunday")


if __name__ == '__main__':
    week().print()
