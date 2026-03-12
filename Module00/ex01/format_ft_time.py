import time

from time import gmtime, strftime

current_time = time.time()

s = strftime("%b %d %Y", gmtime(current_time))

print("Time since January 1, 1970:", "{:,}".format(current_time), "or", "{:.2e}".format(current_time), "in scientific notation")
print(s)
