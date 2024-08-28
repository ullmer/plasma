#https://stackoverflow.com/questions/550001/fully-transparent-windows-in-pygame
#https://stackoverflow.com/questions/1997710/pygame-error-display-surface-quit-why
#https://stackoverflow.com/questions/44520491/can-i-move-the-pygame-game-window-around-the-screen

import pygame
import os
import win32api
import win32con
import win32gui
from pygame._sdl2 import Window

name2window = {} 
 
def newWindow(name, w,h):
  global name2window 
  window = Window(name, size=(w,h)
  name2window[name] = window
  return window

def getWindow(name):
  global name2window 
  if name=='firstWin': return Window.from_display_module()
  if name in name2window: result = name2window[name]; return result

def moveWindow(window, x,y):
  window.position = (x,y) #titlebar slightly off-screen

def transpWinSetup(screen, keyColor, winWidth, winHeight):
  imgIcon = pygame.image.load("images/animist01e.png")
  pygame.display.set_icon(imgIcon)
  pygame.display.set_caption("animist alpha")
  moveWindow(0, 0)

  # Create layered window
  hwnd = pygame.display.get_wm_info()["window"]
  win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                         win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
  # Set window transparency color
  win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*keyColor), 0, win32con.LWA_COLORKEY)

### end ###