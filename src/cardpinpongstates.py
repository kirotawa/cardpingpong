#!/usr/bin/env python
# -*- coding: UTF-8

from .ppstates import State, make_state_machine, NextState
from .cardpinpongsprites import *
from . import gui
from . import resources
from pygame.locals import *
from . import canvas
from . import config
import time
import sys
from threading import Thread
import random

__doc__= '''Classes que representam todo os estados do jogo'''

class PresentationState(State):
    def enter(self,*args):
        pass

    def event_handler(self):
        eventlist = gui.process_mouse()
        for ev in eventlist:
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    sys.exit(0)
        return eventlist

        def exit(self):
            pass

