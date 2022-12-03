from datetime import date

from icalendar import Calendar, Event


class iCal:
    def __init__(self):
        g = open("../../ical/BEGIN:VCALENDAR.ics", "rb")
        self.cal = Calendar.from_ical(g.read())

    def display(self):
        print(self.cal.to_ical().decode("utf-8").replace('\r\n', '\n').strip())
        return self

    def setEvent(self, summary, time):
        event = Event()
        event.add('summary', summary)
        event.add('dtstart', time, parameters={'VALUE': 'DATE'})
        event.add('dtend', time, parameters={'VALUE': 'DATE'})
        # event.add('dtstamp', datetime.now(tz=pytz.timezone('cn')))
        event.add('uid', "18552541076@163.com")
        # event.add("sequence", "0")
        event.add("descripion", summary)
        self.cal.add_component(event)
        return self

    def write(self):
        f = open("../../ical/BEGIN:VCALENDAR.ics", "wb")
        f.write(self.cal.to_ical())
        f.close()
        return self


if __name__ == '__main__':
    ical = iCal()
    ical.setEvent("aaa", date.today()).display().write()
