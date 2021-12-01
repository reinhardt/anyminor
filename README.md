# Any Minor

An adaptive soundtrack to you typing on your keyboard

## Installation

Make sure alsalib is available. If you're on NixOS:

    # nix-shell .

Then:

    # pip install -r requirements

## Usage

    # python watch_keyboard.py | python soundtrack.py

On Linux, `watch_keyboard.py` must be run as root because it needs elevated permissions
to listen in on the keyboard device:

    # sudo python watch_keyboard.py | python soundtrack.py

As you continue typing on your keyboard the music will change to represent the intensity
of your work. A lot of keys in a short time span will result in a denser soundtrack,
while sporadic or no keyboard activity will give you a minimalistic audio experience.
