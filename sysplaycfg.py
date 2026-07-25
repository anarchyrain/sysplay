# linux users: get python-tkinter from your package manager
# everyone else should be fine but like. i guess if it throws a tkinter error try that first regardless?

import json, sys
from tkinter import *

# basic ass GUI

root = Tk()
root.title("sysfetch config creator")
root.geometry('800x600') # sorry 4k monitor users

head = Label(root, text="Configure your stuff:")
head.grid()
wrn = Label(root, text="Please include any spacing. For colours, please use ANSI codes\nWITHOUT\"\\033[\" or \"m\" (ex. \\033[31m is 31).\n")
wrn.grid(column=1, row=0)

# this is literally what it took for me to get this to work without re-writing the entire GUI please don't stone me
csh = Label(root, text="Basic colours cheat sheet:")
csh.grid(column=2, row=0)
cs1 = Label(root, text="Black: 30")
cs1.grid(column=2, row=1)
cs2 = Label(root, text="Red: 31")
cs2.grid(column=2, row=2)
cs3 = Label(root, text="Green: 32")
cs3.grid(column=2, row=3)
cs4 = Label(root, text="Orange: 33")
cs4.grid(column=2, row=4)
cs5 = Label(root, text="Blue: 34")
cs5.grid(column=2, row=5)
cs6 = Label(root, text="Magenta: 35")
cs6.grid(column=2, row=6)
cs7 = Label(root, text="Cyan: 36")
cs7.grid(column=2, row=7)
cs8 = Label(root, text="Light Grey: 37")
cs8.grid(column=2, row=8)
cs9 = Label(root, text="Grey: 90")
cs9.grid(column=2, row=9)
cs10 = Label(root, text="Light Red: 91")
cs10.grid(column=2, row=10)
cs11 = Label(root, text="Light Green: 92")
cs11.grid(column=2, row=11)
cs12 = Label(root, text="Yellow: 93")
cs12.grid(column=2, row=12)
cs13 = Label(root, text="Light Blue: 94")
cs13.grid(column=2, row=13)
cs14 = Label(root, text="Pink: 95")
cs14.grid(column=2, row=14)
cs15 = Label(root, text="Light Cyan: 96")
cs15.grid(column=2, row=15)
cs8 = Label(root, text="White: 97")
cs8.grid(column=2, row=16)

# fucking around and finding out

#row counter
rowc = 1

def rowplus(): # row counter incrementer
    global rowc
    rowc += 1
    return rowc

# i wasn't expecting that to work. anyway

# easy way to read this:
# [x]l = creates the "label" (text) for x
# [x]t = takes text input for x

# system name
sysl = Label(root, text="System Name")
sysl.grid(column=0, row=rowplus())
syst = Entry(root, width=20)
syst.grid(column=1, row=rowc)

# your name (or collective idc)
namel = Label(root, text="Your/collective name")
namel.grid(column=0, row=rowplus())
namet = Entry(root, width=20)
namet.grid(column=1, row=rowc)

# age
agel = Label(root, text="Age")
agel.grid(column=0, row=rowplus())
aget = Entry(root, width=20)
aget.grid(column=1, row=rowc)

# pronouns
prnl = Label(root, text="Pronouns")
prnl.grid(column=0, row=rowplus())
prnt = Entry(root, width=20)
prnt.grid(column=1, row=rowc)

# interests
intl = Label(root, text="Interests")
intl.grid(column=0, row=rowplus())
intt = Entry(root, width=20)
intt.grid(column=1, row=rowc)

# hobbits - i mean hobbies
hobl = Label(root, text="Hobbies")
hobl.grid(column=0, row=rowplus())
hobt = Entry(root, width=20)
hobt.grid(column=1, row=rowc)

# potential for custom fields
# ignore any jank related to these
# fun fact: you can copy these and change the variable names and add more custom fields!
# or just do it in the json since if you're this far you already know what you're doing but yknowww
cfn1l = Label(root, text="Custom field 1")
cfn1l.grid(column=0, row=rowplus())
cfn1t = Entry(root, width=20)
cfn1t.grid(column=1, row=rowc)

cfi1l = Label(root, text="Custom field 1 input")
cfi1l.grid(column=0, row=rowplus())
cfi1t = Entry(root, width=20)
cfi1t.grid(column=1, row=rowc)

cfn2l = Label(root, text="Custom field 2")
cfn2l.grid(column=0, row=rowplus())
cfn2t = Entry(root, width=20)
cfn2t.grid(column=1, row=rowc)

cfi2l = Label(root, text="Custom field 2 input")
cfi2l.grid(column=0, row=rowplus())
cfi2t = Entry(root, width=20)
cfi2t.grid(column=1, row=rowc)

# flair

fl1l = Label(root, text="Flair 1 (Pre-Info)")
fl1l.grid(column=0, row=rowplus())
fl1t = Entry(root, width=20)
fl1t.grid(column=1, row=rowc)

fl2l = Label(root, text="Flair 2 (Mid-info)")
fl2l.grid(column=0, row=rowplus())
fl2t = Entry(root, width=20)
fl2t.grid(column=1, row=rowc)

fl3l = Label(root, text="Flair 3 (Post-Info)")
fl3l.grid(column=0, row=rowplus())
fl3t = Entry(root, width=20)
fl3t.grid(column=1, row=rowc)

# dividers
divl = Label(root, text="Dividers")
divl.grid(column=0, row=rowplus())
divt = Entry(root, width=20)
divt.grid(column=1, row=rowc)

# colours

tcl = Label(root, text="Title/System Name Colour")
tcl.grid(column=0, row=rowplus())
tct = Entry(root, width=20)
tct.grid(column=1, row=rowc)

hcl = Label(root, text="Header Colour")
hcl.grid(column=0, row=rowplus())
hct = Entry(root, width=20)
hct.grid(column=1, row=rowc)

fcl = Label(root, text="Flair Colour")
fcl.grid(column=0, row=rowplus())
fct = Entry(root, width=20)
fct.grid(column=1, row=rowc)

dcl = Label(root, text="Divider Colour")
dcl.grid(column=0, row=rowplus())
dct = Entry(root, width=20)
dct.grid(column=1, row=rowc)

# weed just hit
# about to redefine vibe coding
# fuck LLMs get yourself a stoner butch tgirl with access to w3schools
# good luck!

#########################################################################
# if anything breaks, it's GOING to be here.
#########################################################################
def clicked():
    global system
    system = syst.get()
    global name
    name = namet.get()
    global age
    age = aget.get()
    global pronouns
    pronouns = prnt.get()
    global interests
    interests = intt.get()
    global hobbies
    hobbies = hobt.get()
    # oh my fucking god there has to be a better way
    global field1
    field1 = cfn1t.get()
    global field1data
    field1data = cfi1t.get()
    global field2
    field2 = cfn2t.get()
    global field2data
    field2data = cfi2t.get()
    global flair1
    flair1 = fl1t.get()
    global flair2
    flair2 = fl2t.get()
    global flair3
    flair3 = fl3t.get()
    #hey is that all
    global div
    div = divt.get()
    global tc
    tc = tct.get()
    global fc
    fc = fct.get()
    global hc
    hc = hct.get()
    global dc
    dc = dct.get()

    # FINALLY
    # WAIT NO THIS PART SCARES ME I'VE BEEN PROCRASTINATING
    config = {
        "system":system,
        "name":name,
        "age":age,
        "pronouns":pronouns,
        "interests":interests,
        "hobbies":hobbies,
        "field1":field1,
        "field1data":field1data,
        "field2":field2,
        "field2data":field2data,
        "flair1":flair1,
        "flair2":flair2,
        "flair3":flair3,
        "div":div,
        "titlecolour":tc,
        "headcolour":hc,
        "flaircolour":fc,
        "divcolour":dc
    }

    configout = json.dumps(config)

    # unimportant code for debug purposes because i'm still procrastinating
    # print(configout)
    # ok we good

    with open("spconfig.json", "w") as cfout:
        cfout.write(configout)

    # give me some feedback here bestie this is a LOT of code that could silently fail
    result = Label(root, text="Config created!")
    result.grid(column=1, row=rowc)

    # that was less scary than i thought it would be. anyway,

    def close():
        sys.exit()

    done = Button(root, text="Close", command=close)
    done.grid(column=2,row=rowc)



# nuclear launch codes
go = Button(root, text="Let's go!", command=clicked)
go.grid(column=0, row=rowplus())


root.mainloop()