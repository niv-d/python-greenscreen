# Python-Greenscreen
This is a python script (and windows binary if you head over to release) designed to take a normal webcams footage and add a greenscreen to it.
## How it Works
Insight on how it works may give you a better start at using it. 

When the application first launches it takes a frame from the webcam. This frame is used as reference(you can reset this reference by hitting enter(the script version) or the reset button(the GUI version)). 

Any differences between the captured frame and the current frame will be turned into the greenscreen. To tweak this there is a tolerence and noise removeal options documented further below.
## Getting Started

For windows, you can find windows binaries on the Github release page.
Just download and run the executable named "main.exe"

To watch a video of the setup process go [here]()
or read the instructions below


### Prerequisites
For running greenscreen.py (No GUI version)
```
Python 3
OpenCV 3
```
For running main.py, in addition to the above you need (GUI version)
```
PyQt5
```
### Running
After installing the above simply run eithier of the following
```
python greenscreen.py
```
```
python main.py
```
## License
null

## Notes
This is one of my first full python projects, any advice is welcome!
