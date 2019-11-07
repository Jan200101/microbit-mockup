try:
    DEBUG
except NameError:
    DEBUG = False

WIDTH = 5
HEIGHT = 5

try:
    A_KEY
except NameError:
    A_KEY = "a"

try:
    B_KEY
except NameError:
    B_KEY = "b"

from .accelerometer import *
from .buttons import *
from .compass import *
from .display import *
from .filesystem import *
from .images import *
from .music import *
from .pins import *
from .radio import *
from .utils import *

from .exceptionhandler import *
