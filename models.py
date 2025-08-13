# Constant Parameters
THRESHOLD = 100
NEG_THRESHOLD = -100

class Hand:
    def __init__(self, thumb, index, middle, ring, pinky):
        self.thumb = thumb
        self.index = index
        self.middle = middle
        self.ring = ring
        self.pinky = pinky
    def IsPinchGesture(self):
        return not(self.index.isZero()) and abs(self.index.x - self.thumb.x) < THRESHOLD / 2 and abs(self.index.y - self.thumb.y) < THRESHOLD / 2 and abs(self.middle.x - self.thumb.x) < THRESHOLD / 2 and abs(self.middle.y - self.thumb.y) < THRESHOLD / 2
    def IsIndexTouchingThumb(self):
        return not(self.index.isZero()) and abs(self.index.x - self.thumb.x) < THRESHOLD / 2 and abs(self.index.y - self.thumb.y) < THRESHOLD / 2
    def IsMiddleTouchingThumb(self):
        return not(self.middle.isZero()) and abs(self.middle.x - self.thumb.x) < THRESHOLD / 2 and abs(self.middle.y - self.thumb.y) < THRESHOLD / 2
    def IsRingTouchingThumb(self):
        return not(self.ring.isZero()) and abs(self.ring.x - self.thumb.x) < THRESHOLD / 2 and abs(self.ring.y - self.thumb.y) < THRESHOLD / 2
    def IsPinkyTouchingThumb(self):
        return not(self.pinky.isZero()) and abs(self.pinky.x - self.thumb.x) < THRESHOLD / 2 and abs(self.pinky.y - self.thumb.y) < THRESHOLD / 2

class State:
    def __init__(self, left, right, isCursor, isZooming, isScrolling, isTracking, isShifting, timeOfLastInput, debugMode):
        self.left = left
        self.right = right
        self.isCursor = isCursor
        self.isZooming = isZooming
        self.isScrolling = isScrolling
        self.isTracking = isTracking
        self.isShifting = isShifting
        self.timeOfLastInput = timeOfLastInput
        self.debugMode = debugMode
    def AreThumbsTouching(self):
        return not(self.left.thumb.isZero()) and not(self.right.thumb.isZero()) and abs(self.left.thumb.x - self.right.thumb.x) < THRESHOLD / 2 and abs(self.left.thumb.y - self.right.thumb.y) < THRESHOLD / 2
    def AreIndexesTouching(self):
        return not(self.left.index.isZero()) and not(self.right.index.isZero()) and abs(self.left.index.x - self.right.index.x) < THRESHOLD / 2 and abs(self.left.index.y - self.right.index.y) < THRESHOLD / 2
    def AreMiddlesTouching(self):
        return not(self.left.middle.isZero()) and not(self.right.middle.isZero()) and abs(self.left.middle.x - self.right.middle.x) < THRESHOLD / 2 and abs(self.left.middle.y - self.right.middle.y) < THRESHOLD / 2
    def ArePinkiesTouching(self):
        return not(self.left.pinky.isZero()) and not(self.right.pinky.isZero()) and abs(self.left.pinky.x - self.right.pinky.x) < THRESHOLD / 2 and abs(self.left.pinky.y - self.right.pinky.y) < THRESHOLD / 2


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def set(self, x, y):
        self.x = x
        self.y = y
    def isZero(self):
        return self.x == 0 and self.y == 0
