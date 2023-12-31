import time
import calendar
import datetime 
# print(time.localtime())

# localtime = time.asctime(time.localtime( time.time()))
# print(localtime)
yy = 1947
mm = 8
dd = 15
#print (time.asctime(time.localtime()))
# l=(calendar.month(yy,mm))
# #print (calendar.calendar(yy,mm))
# print (l)
# date_time = date.(yy,mm,dd)
# date_time = date.today()
# print (date_time)

x = datetime.datetime (yy,mm,dd)
print (x.strftime("%A"))