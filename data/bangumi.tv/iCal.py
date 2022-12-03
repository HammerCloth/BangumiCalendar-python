import datetime
import uuid
from datetime import date,datetime

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
        event.add('dtstamp', datetime.today().date(), parameters={'VALUE': 'DATE'})
        event.add('uid', uuid.uuid1())
        event.add('dtstart', time, parameters={'VALUE': 'DATE'})
        event.add('class', 'PUBLIC')
        event.add('summary', summary)
        # event.add('dtstamp', datetime.now(tz=pytz.timezone('cn')))
        # event.add("sequence", "0")
        event.add("TRANSP", "TRANSPARENT")
        # event.add("descripion", summary)
        event.add("X-APPLE-UNIVERSAL-ID", "42902458-1dd4-5105-04d0-2dccc0194c5f")

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
