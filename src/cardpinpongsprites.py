#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from . import gui
from pygame.locals import *
from . import canvas
import pygame
import random
import time

def _unicode(_str, encoding):
    if isinstance(_str, str):
        return _str
    else:
        return _str.decode('utf-8')

class PlayerCards(object):

	def __init__(self,name,type):
            pass

	def isClicked(self,pos):
            if self.rect.collidepoint(pos):
                return True

            return False
