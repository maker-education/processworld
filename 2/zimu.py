import codecs

f1 = codecs.open("1.srt", "r", "utf-8")
f2 = codecs.open("zw.txt", "w", "utf-8") 
f3 = codecs.open("yw.txt", "w", "utf-8")
line = f1.readline()
while line:
	f2.write(line)
	f3.write(line)
	line = f1.readline()
	f2.write(line)
	f3.write(line)
	line = f1.readline()
	f2.write(line)
	line = f1.readline()
	f3.write(line)
	line = f1.readline()
	f2.write(line)
	f3.write(line)
	line = f1.readline()


   
f1.close() 
f2.close() 
f3.close() 
