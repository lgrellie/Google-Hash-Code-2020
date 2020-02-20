path = "../instances/a_example.txt"

f = open(path, "r")
if f.mode == 'r':
    contents = f.readlines()
    for line in contents:
        print(line)

[B, L, D] = list(map(int, contents[0].split(" ")))
scores = list(map(int, contents[1].split(" ")))

libraries = [[[], []] for i in range(L)]
for l in range(l):
    libraries[l][0] = list(map(int, contents[2 + 2*l].split(" ")))
    libraries[l][1] = list(map(int, contents[3 + 2*l].split(" ")))

is_scanned = [0 for b in range(B)]
