import time
# epoch = a date and time from which a computer measures system time


# Convert a time in seconds since the Epoch to a string in local time.
# This is equivalent to asctime(localtime(seconds)).

# epoch = when your computer thinks time began (reference time)
print(time.ctime(0))    # converted a time expressed in seconds since epoch to a readable string
# now
print(time.ctime())     # now# When the time tuple is not present, current time as returned by localtime() is used.


# return current seconds since epoch
print(time.time())

# convert time.time ti readabe time
print(time.ctime(time.time()))

time_object = time.localtime()
time_object = time.gmtime()
print(time_object)

# format time string
localTime = time.strftime('%B %D %Y %H:%M:%S', time_object)
print(localTime)

time_string = '20 April, 2022'
print(time.strptime(time_string, '%d %B, %Y'))


# (year, mouth, day, hours, minutes, secs, day of the week, day of the year, dst)
time_tuple = (2022, 12, 20, 6, 53, 0, 1, 0, 0)
print(time.asctime(time_tuple))

# # convert tuple or object to seconds
time_tuple = (2024, 12, 20, 6, 53, 0, 1, 0, 0)
print(time.mktime(time_tuple))
