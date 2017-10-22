# imageblender
Takes two images of human faces, and blends them.

It's starting to overlay them in the same position, but that's pretty primitive at this point

use like: `GOOGLE_APPLICATION_CREDENTIALS=${HOME}/google_app_name-randomstuff.json python gv.py`

# Setup
This is a little involved, not all my fault ( tho some certainly is )

## Setup the google vision API for your google cloud account.
Well, this takes some doing. The google docs are fair. I don't understand why you have to turn on so many things in the google cloud web console to use the API, but whatever. 

I'm not entirely sure of how to limit the access at google to only the vision api, so if you know about that, holler at ya boy

[You may find this page helpful to get you started](https://cloud.google.com/vision/docs/auth)

## python virtualenv
Setup a new virtualenv, and install the requirements.txt 🎉

This uses Pillow, it's not terrible

