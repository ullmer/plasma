#https://stackoverflow.com/questions/550001/fully-transparent-windows-in-pygame
#https://stackoverflow.com/questions/1997710/pygame-error-display-surface-quit-why

import pygame
import os
import win32api
import win32con
import win32gui

def transpWinSetup(screen, keyColor, winWidth, winHeight):
  imgIcon = pygame.image.load("images/animist01e.png")
  pygame.display.set_icon(imgIcon)
  pygame.display.set_caption("animist alpha")
  os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
  pygame.display.set_mode((winWidth,winHeight))

  # Create layered window
  hwnd = pygame.display.get_wm_info()["window"]
  win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                         win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
  # Set window transparency color
  win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*keyColor), 0, win32con.LWA_COLORKEY)

### end ###
