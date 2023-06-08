import random
import threading
import time
from lib.constants import DELTA_T


class Index:
    def __init__(self):
        self.index = threading.Timer(0.1 * DELTA_T, random.choice([1, 2]))
