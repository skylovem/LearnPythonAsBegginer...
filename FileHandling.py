f=open("mty.txt","w+")
data="true you"
f.write(data)
f.close
g=open("goo.txt","x")
aww=[3,76,9,34,2.4,7]
for value in aww:
    record=str(aww)
    g.write(record)
    g.write("\n")
g.close
