import pyautogui
import time
from enum import Enum
import speech_recognition as sr
import sys

r = sr.Recognizer()
mic = sr.Microphone()

class CommandTypes(Enum):
    LEFTINDEX = 'leftindex'
    LEFTMIDDLE = 'leftmiddle'
    LEFTRING = 'leftring'
    LEFTPINKY = 'leftpinky'
    RIGHTINDEX = 'rightindex'
    RIGHTMIDDLE = 'rightmiddle'
    RIGHTRING = 'rightring'
    RIGHTPINKY = 'rightpinky'
    LEFTPINCH = 'leftpinch'
    RIGHTPINCH = 'rightpinch'
    INDEXES = 'indexes'
    THUMBS = 'thumbs'
    MIDDLES = 'middles'
    PINKIES = 'pinkies'
    PINCHES = 'pinches' 

class Command:
    def __init__(self, name, command, cooldown, timeOfLast):
        self.name = name
        self.command = command
        self.cooldown = cooldown
        self.timeOfLast = timeOfLast
    def execute(self, state=None):
        if (self.timeOfLast == None or time.time() - self.timeOfLast > self.cooldown):
            self.command(state)
            self.timeOfLast = time.time()

def HandleLeftIndex(state=None):
    if (state.isZooming):
        print('Zooming in')
        pyautogui.hotkey('command', '+')
    elif (state.isScrolling):
        print('Scrolling down')
        pyautogui.scroll(-10)
    elif (state.isShifting):    
        print('Starting Dictation')
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            transcript = r.recognize_google(audio)
            pyautogui.write(transcript)
    else:
        pyautogui.click()

def HandleLeftMiddle(state=None):
    if (state.isZooming):
        print('Zooming out')
        pyautogui.hotkey('command', '-')
    elif (state.isScrolling):
        print('Scrolling up')
        pyautogui.scroll(10)
    elif (state.isShifting):
        print('Opening spotlight search')
        pyautogui.hotkey('command', 'space')
    else:
        pyautogui.press('tab')

def HandleLeftRing(state=None):
    if (state.isShifting):
        print('new tab')
        pyautogui.hotkey('command', 't')
    else:
        print('Pressing Enter')
        pyautogui.press('enter')

def HandleLeftPinky(state=None):
    if (state.isShifting):
        print('close tab')
        pyautogui.hotkey('command', 'w')
    else:
        print('Pressing Escape')
        pyautogui.press('esc')

def HandleLeftPinch(state=None):
    print('Changing Desktop Left')
    pyautogui.hotkey('ctrl', 'left')

def HandleRightPinch(state=None):
    print('Changing Desktop Right')
    pyautogui.hotkey('ctrl', 'right')

def HandleIndexesTouching(state=None):
    print('Toggled tracking')
    state.isTracking = not(state.isTracking)

def HandleMiddlesTouching(state=None):
    state.debugMode = not(state.debugMode)
    print(f'Toggled Debug Mode - {state.debugMode}')

def HandleThumbsTouching(state=None):
    print('Exiting')
    exit()

def HandlePinkiesTouching(state=None):
    print('Exiting')
    sys.exit(0)


Commands = {
    CommandTypes.LEFTINDEX: Command(CommandTypes.LEFTINDEX, HandleLeftIndex, 0.5, None),
    CommandTypes.LEFTMIDDLE: Command(CommandTypes.LEFTMIDDLE, HandleLeftMiddle, 1, None),
    CommandTypes.LEFTRING: Command(CommandTypes.LEFTRING, HandleLeftRing, 1, None),
    CommandTypes.LEFTPINKY: Command(CommandTypes.LEFTPINKY, HandleLeftPinky, 1, None),
    CommandTypes.LEFTPINCH: Command(CommandTypes.LEFTPINCH, HandleLeftPinch, 2, None),
    CommandTypes.RIGHTPINCH: Command(CommandTypes.RIGHTPINCH, HandleRightPinch, 2, None),
    CommandTypes.INDEXES: Command(CommandTypes.INDEXES, HandleIndexesTouching, 5, None),
    CommandTypes.THUMBS: Command(CommandTypes.THUMBS, HandleThumbsTouching, 0.1, None),
    CommandTypes.MIDDLES: Command(CommandTypes.MIDDLES, HandleMiddlesTouching, 5, None),
    CommandTypes.PINKIES: Command(CommandTypes.PINKIES, HandlePinkiesTouching, 0.1, None),

}