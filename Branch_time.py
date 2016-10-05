import datetime
from pytz import timezone
import time

portland = timezone('America/Los_Angeles')
portland_time = datetime.datetime.now(portland)
print "The current time in Portland is: " +(portland_time.strftime('%H:%M'))

ny = timezone('America/New_York')
ny_time = datetime.datetime.now(ny)


if ny_time.hour >= 9 and ny_time.hour < 21:
    print 'Hello from NY, you guys are lucky, we are open, for now...'
else:
    print 'You snooze you lose, we are closed, try again later, or not, either way!'


london = timezone('Europe/London')
london_time = datetime.datetime.now(london)

if london_time.hour >= 9 and london_time.hour < 20:
    print 'You Yankees are lucky, we here in London are currently open.'
else:
    print 'Aw bloody hell, London office is closed.  Try again later we are closed!'






def Branch_hours():
    pl_time = datetime.datetime.today()
    ny_time = datetime.datetime.now() + datetime.timedelta(hours = 3)
    london_time = datetime.datetime.now() + datetime.timedelta(hours = 8)

