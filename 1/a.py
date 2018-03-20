import codecs

f1 = codecs.open("1.txt", "r", "utf-8")
f2 = codecs.open("2.txt", "r", "gbk") 
f3 = codecs.open("o.txt", "w", "utf-8")
line = f1.readline()
l1 = 0
while line:
	if (l1 % 4 == 2):
		l2 = f2.readline()
		print(l2, end='')
		f3.write(l2)
	else:
		print(line, end='')
		f3.write(line)

	
	line = f1.readline()
	l1 = l1+1

   
f1.close() 
f2.close() 
f3.close() 
