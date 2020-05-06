import zipfile
import os

KeyPhrase = "The_Password_To_The_Final_Zip_File_Is_W3B5T3R"
print(len(KeyPhrase))
KeyPhrase = " W3B5T3R"
KeyList = list(KeyPhrase)
KeyList.reverse()

nameList = "Dont believe not even your eyes keep in mind the words of the wise"
nameList = nameList.split()
nameList.reverse()
n = len(nameList)

i = 0

name = nameList[i]+'.zip'
File = zipfile.ZipFile(name,"w")
File.write("wisdom.txt",compress_type=zipfile.ZIP_DEFLATED)
File.close()

while i < 3999 :
    i += 1
    oName = name
    name = nameList[i%n]+'.zip'
    File = zipfile.ZipFile(name,"w")
    File.write(oName,compress_type=zipfile.ZIP_DEFLATED)
    File.close()
    os.system("rm {}".format(oName))

i += 1

oName = name 
name = nameList[i%n]+'.zip'
File = zipfile.ZipFile(name,"w")
File.write(oName,compress_type=zipfile.ZIP_DEFLATED)
File.write("Flag.txt",compress_type=zipfile.ZIP_DEFLATED)
File.close()
os.system("rm {}".format(oName))

i += 1

oName = name 
name = nameList[i%n]+'.zip'
File = zipfile.ZipFile(name,"w")
File.write(oName,compress_type=zipfile.ZIP_DEFLATED)
File.write("Flag.txt",compress_type=zipfile.ZIP_DEFLATED)
File.close()
os.system("rm {}".format(oName))
print("Flag Packed")

i = 0
while i < 998 :
    i += 1
    oName = name
    name = nameList[i%n]+'.zip'
    File = zipfile.ZipFile(name,"w")
    File.write(oName,compress_type=zipfile.ZIP_DEFLATED)
    File.close()
    os.system("rm {}".format(oName))
print(name)
oName = name 
name = 'Time.zip'
File = zipfile.ZipFile(name,"w")
File.write(oName,compress_type=zipfile.ZIP_DEFLATED)
File.close()
os.system("rm {}".format(oName))