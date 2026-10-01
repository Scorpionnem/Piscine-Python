import time
from time import gmtime, strftime

current_time = time.time()

s = strftime("%b %d %Y", gmtime(current_time))

print("Time since January 1, 1970:", f"{current_time:,}",
      "or", f"{current_time:.2e}", "in scientific notation")
print(s)
