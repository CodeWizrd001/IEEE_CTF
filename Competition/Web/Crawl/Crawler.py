import mechanize 
br = mechanize.Browser()

charList = [
    'a','b','c','d','e','f','g',
    'h','i','j','k','l','m',
    'n','o','p','q','r','s','t',
    'u','v','w','x','y','z'
]

ansList = []

for i in charList :
    for j in charList :
        a = br.open("http://localhost:10111/Pages/{}.html".format(i+j))
        b = a.get_data()
        b = b.decode()
        if "Part" in b :
            ansList.append(b)

for i in ansList :
    for j in i.split("\n") :
        if "Part" in j :
            print(j)
        
