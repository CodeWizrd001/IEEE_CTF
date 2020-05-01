import mechanize 
br = mechanize.Browser()

charList = [
    'a','b','c','d','e','f','g',
    'h','i','j','k','l','m',
    'n','o','p','q','r','s','t',
    'u','v','w','x','y','z'
]

ansList = []
corList = ['co','rr','ec','tt','pa','th']

for i in corList :
    a = br.open("http://3.16.28.159:1503/{}.html".format(i))
    b = a.get_data()
    b = b.decode()
    if "Part" in b :
        ansList.append(b)

for i in ansList :
    for j in i.split("\n") :
        if "Part" in j :
            try :
                j = j.split("Of 6 :     ")[1]
                j = j.split("         -->")[0]
            except :
                continue
            print(j,end="")
        
