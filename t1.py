import time

from nano_profiler import nano_profiler as n_p
from t2 import spam


def foo():
    time.sleep(1)
    n_p.mark('foo')


def bar():
    time.sleep(2)
    spam()
    n_p.mark('bar')


n_p.start()
foo()
bar()
