import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False

if(debug):
    print("mode:"+mode)
    print("key: "+key)
    print("inp: "+inp)

keyFixed = key

# If key length is shorter than the text length
if (len(key) < len(inp)):
    for i in range((len(inp) % len(key)) + (len(inp)//len(key))*len(key)):
        key = key + keyFixed

#Human Mode
if (mode == "human"):
    output = ""
    for i in range(len(inp)):
        output = output + chr(ord(inp[i])^ord(key[i]))
    print(output)

#numOut Mode
if (mode == "numOut"):
    output = ""
    for i in range(len(inp)):
        output = output + hex(ord(inp[i])^ord(key[i]))[2:] + " "
    print(output)
