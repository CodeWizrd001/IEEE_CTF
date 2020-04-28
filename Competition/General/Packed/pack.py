import zipfile

KeyPhrase = "The_Password_To_The_Final_Zip_File_Is_W3B5T3R"
print(len(KeyPhrase))
KeyPhrase = " W3B5T3R"
KeyList = list(KeyPhrase)
KeyList.reverse()

password = "W3B5T3R"

i = 0 
x = KeyList[i]

print(x)
File = zipfile.ZipFile("zipfile_"+x+".zip","w")
File.setpassword(pwd='W3B5T3R'.encode())
File.write("Flag.txt",compress_type=zipfile.ZIP_DEFLATED)
File.close()

while i < len(KeyList) :
    i += 1
    try :
        x = KeyList[i]
    except :
        break 
    try :
        y = KeyList[i-1]
    except :
        y = "_"
    File = zipfile.ZipFile("zipfile_"+x+".zip","w")
    File.write("zipfile_"+y+".zip",compress_type=zipfile.ZIP_DEFLATED)
    File.close()