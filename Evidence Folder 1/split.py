import binascii

f = open("Not-Hacker-Files.zip",'rb')
full = binascii.hexlify(f.read())
f.close()

one = ""
two = ""
three  = ""
four = ""

while (len(full) >= 8):
    one += full[:2] 
    two += full[2:4]
    three += full[4:6]
    four += full[6:8]
    full = full[8:]  

#Add rest to one
one += full[:2]

f = open("FileFragment1",'wb')
f.write(binascii.unhexlify(one))
f.close()

f = open("FileFragment2",'wb')
f.write(binascii.unhexlify(two))
f.close()

f = open("FileFragment3",'wb')
f.write(binascii.unhexlify(three))
f.close()

f = open("FileFragment4",'wb')
f.write(binascii.unhexlify(four))
f.close()
