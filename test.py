import datetime

begin = datetime.date(2020, 4, 1)
end = datetime.date(2020, 5, 1)
d = begin
delta = datetime.timedelta(days=1)
while d <= end:
    d.strftime("%Y-%m-%d")
    d += delta
    print(str("{}~{}".format(str(d),str(d))))
