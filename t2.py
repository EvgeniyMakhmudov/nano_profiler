import time
from nano_profiler import nano_profiler as n_p


def spam():
    time.sleep(0.5)
    n_p.mark('spam')
