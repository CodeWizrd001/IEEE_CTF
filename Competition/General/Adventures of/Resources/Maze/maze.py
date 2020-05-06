import os


try :
    os.mkdir("Maze")
except :
    os.rmdir("Maze")
    os.mkdir("Maze")
charList = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]


path = "Maze"
for i in charList :
    os.mkdir("{}/{}".format(path,i))

for i in charList :
    for j in charList :
        os.mkdir("{}/{}/{}".format(path,i,j))

for i in charList :
    for j in charList :
        for k in charList :
            os.mkdir("{}/{}/{}/{}".format(path,i,j,k))

path = "Maze/h/u/r"
for i in charList :
    os.mkdir("{}/{}".format(path,i))

for i in charList :
    for j in charList :
        os.mkdir("{}/{}/{}".format(path,i,j))

for i in charList :
    for j in charList :
        for k in charList :
            os.mkdir("{}/{}/{}/{}".format(path,i,j,k))

path = "Maze/h/u/r/a/k/e"
for i in charList :
    os.mkdir("{}/{}".format(path,i))