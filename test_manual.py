import sys
from time import sleep

from nano_profiler import NanoProfiler


def test_1():
    n_p = NanoProfiler(name='Foo Bar Baz', autostart=True)
    sleep(0.1)
    n_p.mark('Foo')
    sleep(0.125)
    n_p.mark('Bar')
    n_p.mark('Baz')


def test_2():
    n_p = NanoProfiler(name='A long caption of my profiler with short comments', autostart=True)
    sleep(0.25)
    n_p.mark('T1')

    sleep(0.01)
    n_p.mark('T2')

    sleep(0.35)
    n_p.mark('T3')


def test_3():
    n_p = NanoProfiler(name='my stat', autostart=True)
    sleep(0.05)
    n_p.mark('Test case with short caption ans long comments')

    sleep(0.05)
    n_p.mark('Execute function to prepare data')

    sleep(0.05)
    n_p.mark('Find a target value from a long life circle')


def test_4():
    n_p = NanoProfiler(name='', autostart=True)
    n_p._points[0]['time'] = 0
    n_p._points.append({
        'time': 10,
        'label': 'Test case with big seconds'
    })
    n_p._points.append({
        'time': 110,
        'label': '100 seconds'
    })
    n_p._points.append({
        'time': 1110,
        'label': '1000 seconds'
    })
    n_p._points.append({
        'time': 3600*24*7 + 1110,
        'label': '*Ring* *Ring*, *breathe*, Seven days!'
    })


def test_5():
    n_p = NanoProfiler(name='Test case from real.', autostart=True)
    n_p._points[0]['time'] = 0
    n_p._points.append({
        'time': 10,
        'label': 'This was not surprise for me...'
    })


# for run test_case 1 execute python3 test_manual.py 1
test_case = 'test_{}'.format(sys.argv[1])
func = locals()[test_case]
func()
