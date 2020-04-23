# ASCII to camera

To run this, clone the repository, then run

`pip install -r requirements.txt`

Make sure to install v4l2loopback:
`sudo apt-get install -y v4l2loopback-dkms`

Start the v4l2loopback module
`modprobe v4l2loopback`

Then you should be able to do

`./camera.py | ffmpeg -y -f rawvideo -s 600x600 -pix_fmt gray -i - -an -f v4l2 /dev/video2`

And you should be able to see the video on the newly created dummy device

`ffplay /dev/video2`


