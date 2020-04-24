# ASCII to camera

To run this, clone the repository, then run

`pip install -r requirements.txt`

Make sure to install v4l2loopback by downloading and installing it [from source](https://github.com/umlaeute/v4l2loopback).

Start the v4l2loopback module

`modprobe v4l2loopback`

Then you should be able to do

`./camera.py | ffmpeg -f rawvideo -s 320x240 -pix_fmt gray -re -i - -an -c:v rawvideo -pix_fmt yuv420p -f v4l2 /dev/video3`

And you should be able to see the video on the newly created dummy device

`ffplay /dev/video3`
