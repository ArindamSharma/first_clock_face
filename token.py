def mencode(string):
    a=""
    for i in string:
        # print(ord(i))
        a+=str(len(str(ord(i))))+str(ord(i))
    return a
def mdecode(string):
    a=""
    i=0
    while(i<len(string)):
        clen=int(string[i])
        # print(i,i+clen+1)
        a+=chr(int(string[i+1:i+clen+1]))
        i=i+1+clen
    return a
# For Encoding 
# print(mencode("enter message"))

# For Decoding
print(mdecode("3103310531163104311729829531122973116295249249265273286269280271265248271286253277312226831043118282311426928829531173108310225628725729928428028525626527528829728128631073107271299278257277311431002862573121312029028831062743119299312128831162863111284310526925427825525425528527331113114249248312029031163120"))