fout=open("out.csv","a")
for num in range(1,26):
    f = open(str(num)+".csv")
    f.next() 
    for line in f:
         fout.write(line)
    f.close() 
fout.close()
