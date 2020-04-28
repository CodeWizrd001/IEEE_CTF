import os
import random

charList = [
    'a','b','c','d','e','f','g',
    'h','i','j','k','l','m',
    'n','o','p','q','r','s','t',
    'u','v','w','x','y','z'
]

FlagText = """
<html>
<head> 
    <link rel="stylesheet" href="styles.css">
    <title>
        Find The Flag
    </title>
    Find The Flag
</head>
<body>
    <p>
        There's A Part Of The Flag In Here
    </p>
    <p>
        But Where Is It ?
    </p>
    <p>
        <a href="{0[1]}.html"> {0[0]}</a> <br>
        <a href="{0[2]}.html"> {0[0]}</a><br>
        <a href="{0[3]}.html"> {0[0]}</a><br>
        <a href="{0[4]}.html"> {0[0]}</a><br>
        <a href="{0[5]}.html"> {0[0]}</a><br>
        <a href="{0[6]}.html"> {0[0]}</a><br>
        <a href="{0[7]}.html"> {0[0]}</a><br>
        <a href="{0[8]}.html"> {0[0]}</a><br>
        <a href="{0[9]}.html"> {0[0]}</a><br>
        <a href="{0[10]}.html"> {0[0]}</a><br>
    </p>
</body>
<!-- Flag Text Part {0[11]} Of 6 :     {0[12]}         -->
</html>
"""

NoFlagText = """
<html>
<head> 
    <link rel="stylesheet" href="styles.css">
    <title>
        Find The Flag
    </title>
    Find The Flag
</head>
<body>
    <p>
        But Then There's No Flag In Here
    </p>
    <p>
        <a href="{0[1]}.html"> {0[0]}</a> <br>
        <a href="{0[2]}.html"> {0[0]}</a><br>
        <a href="{0[3]}.html"> {0[0]}</a><br>
        <a href="{0[4]}.html"> {0[0]}</a><br>
        <a href="{0[5]}.html"> {0[0]}</a><br>
        <a href="{0[6]}.html"> {0[0]}</a><br>
        <a href="{0[7]}.html"> {0[0]}</a><br>
        <a href="{0[8]}.html"> {0[0]}</a><br>
        <a href="{0[9]}.html"> {0[0]}</a><br>
        <a href="{0[10]}.html"> {0[0]}</a><br>
    </p>
</body>
<!-- Wassup -->
</html>
"""

FlagList = ['co','rr','ec','tt','pa','th']
NoFlagList = []
for i in charList :
    for j in charList :
        if i+j not in FlagList :
            NoFlagList.append(i+j)

i = 0 
j = 1
k = 0

FlagChunks = ["ieee_","nitc{","w3bcR4w","ling_","i5_such_","4_p4In}"]

print("".join(FlagChunks))

while FlagList != []:
    i += 1
    randomText = ""
    for k in range(10) :
        randomText += random.choice(charList)
    Formatter = [randomText]
    for k in range(10) :
        Formatter.append(random.choice(NoFlagList))
    if i%20 == 0 :
        x = FlagList[0]
        Formatter[random.randint(1,10)] = x 
        Formatter.append(j)
        Formatter.append(FlagChunks[j-1])
        if i%60 == 0:
            FlagList.remove(x)
            j += 1

    Formatter = tuple(Formatter)
    File = open("Created/"+NoFlagList[i-1]+".html","w")
    File.write(NoFlagText.format(Formatter))
    File.close()

while i < len(NoFlagList) :
    i += 1
    randomText = ""
    for k in range(10) :
        randomText += random.choice(charList)
    Formatter = [randomText]
    for k in range(10) :
        Formatter.append(random.choice(NoFlagList))

    Formatter = tuple(Formatter)
    File = open("Created/"+NoFlagList[i-1]+".html","w")
    File.write(NoFlagText.format(Formatter))
    File.close()

FlagList = ['co','rr','ec','tt','pa','th']
FlagChunks = ["ieee_","nitc{","w3bcR4w","ling_","i5_such_","4_p4In}"]

j = 1
i = 0
while FlagList != [] :
    i += 1
    randomText = ""
    for k in range(10) :
        randomText += random.choice(charList)
    Formatter = [randomText]
    for k in range(10) :
        Formatter.append(random.choice(NoFlagList))
    x = FlagList[0]
    try :
        y = FlagList[1]
    except :
        y = "co"
    Formatter[random.randint(1,10)] = y 
    Formatter.append(j)
    Formatter.append(FlagChunks[j-1])
    FlagList.remove(x)
    j += 1

    print(x,y)

    Formatter = tuple(Formatter)
    File = open("Created/"+x+".html","w")
    File.write(FlagText.format(Formatter))
    File.close()