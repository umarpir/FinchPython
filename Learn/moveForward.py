import time

from finch import Finch

finch = Finch()

#move forward for 1 second
finch.wheels(1,1);
time.sleep(1)

#move backwards for 1 second
finch.wheels(-1,-1)
time.sleep(1)

#finish script
finch.close()
