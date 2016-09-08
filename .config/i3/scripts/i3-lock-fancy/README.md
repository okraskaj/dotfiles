i3lock-fancy
============

This is an i3lock bash script that takes a screenshot of the desktop, blurs the background and adds a lock icon and text. The fork contains a fix for dual monitor setups, fortune support, and DPMS support. Now with our own screenshots!

Original author's website: [github pages website](http://meskarune.github.io/i3lock-fancy/)

![screen shot of lockscreen](https://git.indohy.us/dubbleohnexus/i3lock-fancy-fork/raw/master/screen.png)

Dependancies
------------
* [i3lock-color-git](https://github.com/Arcaena/i3lock-color)
* imagemagick
* scrot
* Liberation Fonts
* xset (optional)
* fortune (optional)

The lock screen in action:

![lockscreen animation](https://git.indohy.us/dubbleohnexus/i3lock-fancy-fork/raw/master/smallscreen.gif)

Use this with xautolock to automatically lock the screen after a set time.

Systemd Unit file (edit for your own use):

    [Unit]
    Description=Lock the screen automatically after a timeout
    
    [Service]
    Type=simple
    User=meskarune
    Environment=DISPLAY=:0
    ExecStart=/usr/bin/xautolock -time 5 -locker /usr/local/bin/lock/lock -detectsleep
    
    [Install]
    WantedBy=graphical.target
