# might not need all this. idk.
# i'm looking at my test programs. i don't know what's in which libraries, and at this point i'm too afraid to ask
import sys, os, time, json
##########

# defines some functions

# clears terminal
def termclr():
    os.system('cls' if os.name=='nt' else 'clear')

# typewriter
def type(x):
    for c in x:
        print(f"{c}", end="", flush=True) # works in vscodium's debugger, but not in konsole or kitty? strange.
        time.sleep(0.05)

# too lazy to type this
def pause():
    time.sleep(0.15)

###########

# json handling
# note: this requires the config file to exist in the current directory, or it WILL error out.

# accesses said config file
with open('spconfig.json', 'r') as cfg:
    data = json.load(cfg)

# get these variables assigned
sys = data['system']
name = data['name']
age = data['age']
prn = data['pronouns']
intr = data['interests']
hob = data['hobbies']
fn1 = data['field1']
fd1 = data['field1data']
fn2 = data['field2']
fd2 = data['field2data']
fl1 = data['flair1']
fl2 = data['flair2']
fl3 = data['flair3']
tc = data['titlecolour']
hc = data['headcolour']
fc = data['flaircolour']
dc = data['divcolour']

clr = "\033[0m\n" # stops formatting bleed, ensures new lines work in places where they sometimes don't


##########

#clears your terminal
termclr()

#types things. idk bro. what do you want from me in these comments
print(f"\033[{tc}m", end="")
type(sys + clr)
print(f"\033[{dc}m")
type(div + clr)

print(f"\033[{fc}m")
type(fl1 + clr)

print(f"\033[{hc}m")
type("╭SYSTEM:" + clr)
print("├ name: " + name)
pause()
print("├ age: " + age)
pause()
print("╰ pronouns: " + prn)
pause()

print(f"\033[{fc}m")
type(fl2 + clr)

print(f"\033[{hc}m")
type("╭MISC INFO:" + clr)
print("├ interests: " + intr)
pause()
print("├ hobbies: " + hob)
pause()
print("├ " + fn1 + ": " + fd1)
pause()
print("╰ " + fn2 + ": " + fd2)

print(f"\033[{fc}m")
type(fl3 + clr)
print(f"\033[{dc}m")
type(div + clr)
