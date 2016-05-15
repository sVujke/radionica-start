import datetime

print "Koje godine si rodjen/rodjena?"
godina_rodjenja = raw_input()

godina = datetime.date.today().year
#godina = int(godina)
godina_rodjenja = int(godina_rodjenja)

if godina < godina_rodjenja:
    print "ne zezaj"
else:

    print "Uneta godina rodjenja:", godina_rodjenja
    print "Trenutna godina:", godina
    starost=godina - godina_rodjenja
    print "Starost:", starost
if starost >=18:
    print "Punoletan/punoletna si"
else:
    print "Klinac si"