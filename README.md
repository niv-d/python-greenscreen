# Python-Greenscreen
This is a python script (and windows binary if you head over to release) designed to take a normal webcams footage and add a greenscreen to it. Virtually. It's a virtual greenscreen!
## How it Works
Insight on how it works may give you a better start at using it. 

When the application first launches it takes a frame from the webcam. This frame is used as reference(you can reset this reference by hitting enter(the script version) or the reset button(the GUI version)). 

Any differences between the captured frame and the current frame will be turned into the greenscreen. To tweak this there is a tolerence and noise removeal options documented further below.

All this using minimal CPU usage, roughly <5% on my main system (an i7 4790k)
## Getting Started

For windows, you can find windows binaries on the Github release page.
Just download and run the executable named "main.exe"

To watch a video of the setup process go [here](https://www.youtube.com/watch?v=HpZxoBdegTE)
or read the instructions below

Some things before we begin:
This script works off of the difference between two frames of reference. Because of that, you need to keep changes in your enviroment to a minimum. The hardest part of this rule might be lighting. You need good (or atleast consistent) lighting to really be able to get decent results. Camera angle also helps, if you can hide any reflections or shadows that works too.

Quickstart:

*please make sure that your webcam is not being used by anything else*
1. Make sure your webcam is plugged in, the script may crash if it's not plugged in.
2. Click the reset button while there is no movement and you (or your subject) is out of frame. You can use the timer to help with this.
3. If you need to change the color of the greenscreen, go for it its the R G B values.
4. For the threshold it's really up to you, I usually find it best to drag it up until the "noise" on the picture is mostly gone, then add 10.
5. The type dropdown is to change the type of noise removal. Usually you will want this to be circle. Look at the indepth video below to find out more information about this setting.
6. The size of noise removeal is another up-to-you setting. Smaller with a high threshold may leave holes in your subject. To larn may affect perfomance of the feed. Usually I find a value of 10-20 under the threshold to produces nice results. Your experience may vary

All in all it really depends on the results you want and finding the sweet spot for your setup. Watch the videos for more information.

[Indepth video of the functions](https://www.youtube.com/watch?v=HpZxoBdegTE)

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
