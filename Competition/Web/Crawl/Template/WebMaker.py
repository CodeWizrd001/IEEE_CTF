import os
import random

charList = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

FlagText = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    
    <title>Find The Flag</title>

    <link href="https://fonts.googleapis.com/css2?family=Electrolize&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <link rel="stylesheet" href="styles.css">
    
</head>
<body>
    <div class="container">
        <div id="content">
            <h1>Find The Flag</h1>
            <hr>
            <p>There's A Part Of The Flag In Here But Where Is It ?</p>

            <div>
                <a href="{0[1]}.html"> {0[0]}</a><br>
        <a href="{0[2]}.html"> {0[0]}</a><br>
        <a href="{0[3]}.html"> {0[0]}</a><br>
        <a href="{0[4]}.html"> {0[0]}</a><br>
        <a href="{0[5]}.html"> {0[0]}</a><br>
        <a href="{0[6]}.html"> {0[0]}</a><br>
        <a href="{0[7]}.html"> {0[0]}</a><br>
        <a href="{0[8]}.html"> {0[0]}</a><br>
        <a href="{0[9]}.html"> {0[0]}</a><br>
        <a href="{0[10]}.html"> {0[0]}</a><br>
            </div>
        </div>
    </div>
</body>
<!-- Flag Text Part {0[11]} Of 6 :     {0[12]}         -->
</html>
"""

NoFlagText = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Find The Flag</title>

    <link href="https://fonts.googleapis.com/css2?family=Electrolize&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <link rel="stylesheet" href="styles.css">

</head>
<body>

    <div class="container">
        <div id="content">
            <h1>Find The Flag</h1>
        <hr>
        <p>
            But Then There's No Flag In Here
        </p>
        <div>
        <a href="{0[1]}.html"> {0[0]}</a><br>
        <a href="{0[2]}.html"> {0[0]}</a><br>
        <a href="{0[3]}.html"> {0[0]}</a><br>
        <a href="{0[4]}.html"> {0[0]}</a><br>
        <a href="{0[5]}.html"> {0[0]}</a><br>
        <a href="{0[6]}.html"> {0[0]}</a><br>
        <a href="{0[7]}.html"> {0[0]}</a><br>
        <a href="{0[8]}.html"> {0[0]}</a><br>
        <a href="{0[9]}.html"> {0[0]}</a><br>
        <a href="{0[10]}.html"> {0[0]}</a><br>
        </div>
        </div>
    </div>
</body>
<!-- Wassup -->
</html>
"""

FlagList = ['co', 'rr', 'ec', 'tt', 'pa', 'th']
NoFlagList = []
for i in charList:
    for j in charList:
        if i+j not in FlagList:
            NoFlagList.append(i+j)

i = 0
j = 1
k = 0

FlagChunks = ["ieee_", "nitc{", "w3bcR4w", "ling_", "i5_such_", "4_p4In}"]

print("".join(FlagChunks))

while FlagList != []:
    i += 1
    randomText = ""
    for k in range(10):
        randomText += random.choice(charList)
    Formatter = [randomText]
    for k in range(10):
        Formatter.append(random.choice(NoFlagList))
    if i % 20 == 0:
        x = FlagList[0]
        Formatter[random.randint(1, 10)] = x
        Formatter.append(j)
        Formatter.append(FlagChunks[j-1])
        if i % 60 == 0:
            FlagList.remove(x)
            j += 1

    Formatter = tuple(Formatter)
    File = open("Created/"+NoFlagList[i-1]+".html", "w")
    File.write(NoFlagText.format(Formatter))
    File.close()

while i < len(NoFlagList):
    i += 1
    randomText = ""
    for k in range(10):
        randomText += random.choice(charList)
    Formatter = [randomText]
    for k in range(10):
        Formatter.append(random.choice(NoFlagList))

    Formatter = tuple(Formatter)
    File = open("Created/"+NoFlagList[i-1]+".html", "w")
    File.write(NoFlagText.format(Formatter))
    File.close()

FlagList = ['co', 'rr', 'ec', 'tt', 'pa', 'th']
FlagChunks = ["ieee_", "nitc{", "w3bcR4w", "ling_", "i5_such_", "4_p4In}"]

j = 1
i = 0
while FlagList != []:
    i += 1
    randomText = ""
    for k in range(10):
        randomText += random.choice(charList)
    Formatter = [randomText]
    for k in range(10):
        Formatter.append(random.choice(NoFlagList))
    x = FlagList[0]
    try:
        y = FlagList[1]
    except:
        y = "co"
    Formatter[random.randint(1, 10)] = y
    Formatter.append(j)
    Formatter.append(FlagChunks[j-1])
    FlagList.remove(x)
    j += 1

    print(x, y)

    Formatter = tuple(Formatter)
    File = open("Created/"+x+".html", "w")
    File.write(FlagText.format(Formatter))
    File.close()
