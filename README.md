# SYSPLAY
A silly little profile writer for people with DID/OSDD who are also freaking nerds.

## Why?
I was bored. I wanted to. I made a little version for myself and had enough fun that I spent the next 36 hours creating a way for others to use it without learning to code for themselves. I even learned a thing or two. So, I guess the real question is *why not?*

## What does it do?
The program comes in 2 parts.

The first, **SysplayCFG,** generates the config file (spconfig.json) that Sysplay itself needs.

*SysplayCFG does not import or store data from previous configs and WILL overwrite them WITHOUT PROMPTING when generating new configs.* I highly recommend renaming old configs you want to keep.

<img width="1280" height="720" alt="sysplaycfg" src="https://github.com/user-attachments/assets/dc531d1f-9b70-4422-9d91-7efe4bdb85e4" />

Then, you can run **Sysplay** itself to display the info. Like this!

<img width="1280" height="720" alt="sysplay" src="https://github.com/user-attachments/assets/3d664d11-2805-4afb-9169-a431edfa24de" />

## How to run

First, ensure you have Python installed and relatively updated - this should run on any version newer than 3.0, but is confirmed working on the latest version.

Second, download both sysplay.py and sysplaycfg.py *into the same folder.* I recommend a dedicated folder as a configuration file will be generated here.

Start with sysplaycfg:

`cd /path/to/folder`

`python sysplaycfg.py`

After filling out the form, SysplayCFG will generate the configuration file in the same folder. Feel free to leave anything you want blank - some things may still display as a blank field, though.

Then, you can run sysplay:

`cd /path/to/folder`

`python sysplay.py`

Congratulations! Funky little profile!

## Known issues

***Tkinter errors:*** Some Linux distros do not include Tkinter with Python. Please install the python-tkinter package through your distro's package manager. Windows and Mac users should not be affected by this.

***Unicode characters sometimes break:*** Something in the config generator escapes slashes, and I can't get it to stop. I'm unsure if this is a Python/JSON limitation or just me not knowing what I'm doing. Copy-pasting the Unicode character itself or editing the config to remove the extra `\` should work.

***Not all ANSI colours work:*** Possibly limited by different terminals. The base 16 colours are confirmed working, but I've had mixed results with anything outside of that. If you're having trouble with basic colours, please ensure you did not include the `\033[` before or the `m` after. *This also applies to your own ANSI colour values.*

***GUI is ugly:*** I don't know how to make a less ugly GUI, and at this point I'm too afraid to ask :D
