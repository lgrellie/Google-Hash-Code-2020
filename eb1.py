sign_up = [1,0]
scans = [[1, 2, 4], [3, 6]]
f = open("solution","w+")
f.write("%d\n" % len(sign_up))
i = 0
for lib in sign_up :
	f.write("%d %d\n" % (lib, len(scans[i])))
	print(*scans[i], sep=' ', end='\n', file=f)
	i += 1
f.close()