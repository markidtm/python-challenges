# All Imports:
import datetime

# Printing Current Time:
now = datetime.datetime.now()
print ("-" * 25)
print (now)
print (now.year)
print (now.month)
print (now.day)
print (now.hour)
print (now.minute)
print (now.second)

# Printing The Time Before:
print ("-" * 25)
print ("1 week ago was it: ", now - datetime.timedelta(weeks=1))
print ("100 days ago was: ", now - datetime.timedelta(days=100))
print ("1 week from now is it: ",  now + datetime.timedelta(weeks=1))
print ("In 1000 days from now is it: ", now + datetime.timedelta(days=1000))

# Setting The Birthday:
birthday = datetime.datetime(2012,11,4)

#Printing If The Given Birthday is Now:
print ("-" * 25)
print ("Birthday in ... ", birthday - now)
print ("-" * 25)
