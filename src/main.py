#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from . import resources
from . import gui
import pygame
import time
from . import widgets
from . import canvas
from . import config
from pygame.locals import *
import sys
from .ppstates import  *
from .states import make_state_machine


def main_():
    resources.init()
    pygame.display.set_caption("Kanji Memo")
    pygame.mouse.set_visible(True)
    clock = pygame.time.Clock()
    state_machine = make_state_machine()

    while True:
        clock.tick(60)
        handler = state_machine.handle_events()
        widgets.poll.update()
        gui.draw()

