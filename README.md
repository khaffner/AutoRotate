# Autorotate

This project contains "everything" needed to make your own autorotate on your linux computer.\
What's needed:
- A computer running Linux with Xorg. I use Pop OS 20.04
- Python 3.6 or newer
- An android phone with accelerometer and Tasker installed
- Some velcro or other way of attaching the phone securely on a vertical surface
  
## Setup
1. Clone this repo.
2. Look at [rotation.py](rotation.py). It's quite tiny, read through it.
3. Change "replaceme" with something more secure. Think of it as a password.
4. Now look at [the tasker profile](taskerprofile_rotatenormal.xml).
   1. There too, change "replaceme" to the same as step 3.
   2. Find the IP of your computer. Replace the IP in the xml with your correct IP as well.
   3. Run xrandr --listmonitors on your computer. Note the name of the display you want to rotate. For my demo purpose, it was eDP-1. Replace that in the xml as well.
5. Now you may import the profile into Tasker. You could also create the profile completely from scratch.
6. This is now just the profile for rotating the screen back to normal. I suggest you make 3 copies, and replace "normal" with inverted, left and right in each of them respectively.
7. You also need to replace the orientation of the state in the profile to match the rotations.
   1. If you rotate the phone 90 degrees left, send the request that rotates left, and so on.

## Usage
Strap the phone to the back of the screen in question, connect a charger to keep it alive, run [rotation.py](rotation.py) however you want, and you should be done!

## Security
Yes, the security here is laughable. Non-encrypted and the secret in the url, that's stupid.\
But it's ok as a proof of concept, it's better than nothing.\
Just be aware of hackers rotating your screen for fun. And if they're on your local network, you've got bigger problems.

## Credits
My friend [Michael Gundersen](https://github.com/theagilepadawan) made something similar using Alfred on MacOS, and also Tasker on an Android phone. That project inspired me to make this Linux-equivalent.