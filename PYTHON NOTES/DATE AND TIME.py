# from datetime import datetime
#
# datetime = datetime.now()
# print(datetime)
#
#
# print("DATE: ", datetime.date())
#
# print("TIME: ", datetime.time())
#
# print("MONTH: ", datetime.month)
#
# print("YEAR: ", datetime.year)
#
# print("\t")
#
# print("HOUR: ", datetime.hour)
#
# print("MINUTES: ", datetime.minute)
#
# print("SECOND: ", datetime.second)
#
# print("MICROSECOND: ", datetime.microsecond)


######################

#DATE


import datetime


# tdy = datetime.date.today()
# print(tdy)
# print(tdy.year)
# print(tdy.day)
# print(tdy.month)
# print(tdy.weekday())   #monday= 0, sunday = 6
# print(tdy.isoweekday())   #monday= 1, sunday = 7

#
# tdelta = datetime.timedelta(days=3)      # for checking previous days and future days from today
# print(tdy+tdelta)
# print(tdy-tdelta)



# bday = datetime.date(2023, 12, 7)
# till_bday = bday - tdy
# print(till_bday)
# print(till_bday.days)
# print(till_bday.total_seconds())


#TIME


# t = datetime.time(8, 45, 30, 13423)
# print(t.hour)
#
# dt = datetime.datetime.today()
# tdelta  = datetime.timedelta(hours=12)
# print(dt + tdelta)


#
# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)



import pytz


# dt = datetime.datetime(2023, 5, 31, 12, 30, 45,tzinfo=pytz.UTC )
# dt_now = datetime.datetime.now(tz=pytz.UTC)
# print(dt,"\t", dt_now)
#
# ist_now =dt_now.astimezone(pytz.timezone("US/Mountain"))
# print(ist_now)
# for tz in pytz.all_timezones:
#     print(tz)



# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# dt_mtn = datetime.datetime.now()
# mtn_tz = pytz.timezone("US/Mountain")
# dt_mtn = mtn_tz.localize(dt_mtn)     #we want to use localize because we cannot cehck astime in naive time or we need to do the first mwthod
# dt_east = dt_mtn.astimezone(pytz.timezone("US/Eastern"))
# print(dt_east)



# dt_mtn = datetime.datetime.now(tz=pytz.timezone("US/Mountain"))
# print(dt_mtn.strftime("%b %d, %Y"))   #strftime - datetime to string
#
# dt_str = "July 26, 2016"
# dt = datetime.datetime.strptime(dt_str, "%B %d, %Y")   #strptime - string to datetime
# print(dt)

#########################



# import time
# print("CURRENT TIME: ", time.ctime(time.time()))   #ctime will show time in human readable form
#
#
# print(time.localtime(time.time()))   # it has more details than ctime)
#
# t = time.localtime(time.time())
#
# print("Year:", t.tm_year)
# print("Month:", t.tm_mon)
# print("Minutes:", t.tm_min)
#



# import time
# t = time.time()
# ms = int(t*1000)
# print("MILLISECOND:", ms)

#
# from datetime import datetime,  timezone
# now = datetime.now(timezone.utc)
# print(now)


# from datetime import datetime
# import pytz
#
# a = datetime.now(pytz.timezone("US/Central"))
# print(a.strftime("%Y:%m:%d %H %S %Z %z" ))
#
# #extract components from above a
# print(a.tzname())
# print(a.utcoffset())    #offset is the diff btwn our timezone and utc's



# from datetime import datetime
# iso_format = datetime.now().isoformat()
# print(iso_format)       #it is computer readable format
#
# iso_string = "2023-05-31T23:03:01.275436"
# print(datetime.fromisoformat(iso_string))  #convert iso into human readable format




# import time
# from datetime import datetime
# gmt = time.gmtime(time.time())
# print(gmt)
#  print(gmt.tm_year, ":", gmt.tm_mon, ":", gmt.tm_mday)






# from datetime import datetime
# from datetime import time
#
# now = datetime.now()
# print(now.time())
#
# t = time()
# print(t)
#
# t1 = time(hour=12, minute=2, second=45)
# print(t1)
#
# t2 = time(12, 2, 45, 273658)
# print(t2)


#
# from datetime import datetime
# import time
#
# now = datetime.now()
# now = datetime.now().time()
# print(now.strftime("%Y/%m/%d %H:%M:%S"))
# print(now.strftime("%A/%d %B/%Y"))
# print(now.strftime("%H:%M:%S.%f-%p"))   #%F for microseconds
# print(now.strftime("%I:%M:%S"))   #%I for 24 hour format
# print(now.strftime("%H:%M %p"))
#
#
# dt = x_int = int(now.strftime("%Y%m%d"))
# print(dt)
#
# #convert back to datetime
# dt = datetime.strptime(str(dt), "%Y%m%d")
# print(dt)
# time = time.sleep(5)
# quit(dt)



#timedelta for adding time days, from current time or date

# from _datetime import datetime, timedelta
# td = datetime.now()
# t = td + timedelta(days=4)
# print(t)




# import calendar
#
# year = 2023
# month = 6

# print(calendar.monthcalendar(year,month))
#
# print(calendar.calendar(year))


# print(calendar.monthcalendar(2023, 6))
# print(calendar.isleap(2023))
#
#
#
# print(calendar.MONDAY)
# print(calendar.TUESDAY)
# print(calendar.WEDNESDAY)
# print(calendar.THURSDAY)
# print(calendar.FRIDAY)
# print(calendar.SATURDAY)
# print(calendar.SUNDAY)
















































