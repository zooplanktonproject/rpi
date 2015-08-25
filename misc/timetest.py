import time
import random
from itertools import count

fps = 24
loop_delta = 1./fps

current_time = target_time = time.time()
for i in count():
    #### loop frequency evaluation
    previous_time = current_time
    current_time = time.time()
    time_delta = current_time - previous_time
    print 'loop #%d frequency: %s' % (i, 1. / time_delta)

    #### processing
    # processing example that sleeps a random time between 0 and loop_delta/2.
    time.sleep(random.uniform(0, loop_delta / 2.))

    #### sleep management
    target_time += loop_delta
    sleep_time = target_time - time.time()
    if sleep_time > 0:
        time.sleep(sleep_time)
    else:
        print 'took too long'
