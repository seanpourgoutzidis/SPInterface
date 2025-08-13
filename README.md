# SPInterface

This application allows you to control your Mac with gestures. 
I created this to demonstrate that there is more than one way to interact with your computer and to show how extensible gestural interfaces can be.

## Technical Details

SPInterface uses OpenCV and Mediapipe to track gestures. Upon registering gestures, it will use PyAutoGui to make inputs to the user's Mac. 
This implementation was inspired by [https://github.com/baukk/Gesture-Recognition](https://github.com/baukk/Gesture-Recognition).

## How to install

1. Clone the repo `git clone https://github.com/seanpourgoutzidis/SPInterface.git`
2. Create a virtual environment by running `python -m venv venv`
3. Source the virtual environment by running `source venv/bin/activate`
4. Run `pip install -r requirements.txt` to install requirements
5. Run the script with `python spinterface.py`

OR for an easy download and running experience:

Download and double-click on the `spinterface` UNIX executable in this repo or download the application file from [here](https://drive.google.com/drive/folders/18dbiEGc-qIFJMcLnUz8TF7c6weR5K57R?usp=sharing).
Note that the app file takes a while to start up, while the UNIX executable tends to be faster!

## Manual 

* Left hand
    * Index - thumb = click mouse
    * Middle - thumb = press tab
    * Ring - thumb = press enter
    * Pinky - thumb = press esc
    * Pinch - Change window left
* Right hand
    * Index- Thumb + movement = move mouse
    * Middle - Thumb = press and swipe to zoom in or out
    * Ring - Thumb = press and swipe to scroll up or down
    * Pinky - thumb = shift
        * Left index = Dictation
        * Left middle = Spotlight Search
        * Left ring = command + t
        * Left ring = command + w
    * Pinch = change window right
* Pinky touching = exit
* Indexes touching = start tracking
* Middles touching = open debug mode window

## Demo

(Link to demo video)[https://youtu.be/jx4TeRAwqYA]
