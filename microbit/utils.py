from time import sleep as time_sleep
from os import execv
from sys import executable, argv


def sleep(time):
    time_sleep(time/100)

def reset():
    execv(executable, [executable] + argv)