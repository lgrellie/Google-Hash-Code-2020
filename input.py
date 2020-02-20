path = "../instances/a_example.txt"

f = open(path, "r")
if f.mode == 'r':
    contents = f.readlines()
    for line in contents:
        print(line)

[B, L, D] = list(map(int, contents[0].split(" ")))
scores = list(map(int, contents[1].split(" ")))

libraries = [[[], []] for i in range(L)]
for l in range(L):
    libraries[l][0] = list(map(int, contents[2 + 2*l].split(" ")))
    libraries[l][1] = list(map(int, contents[3 + 2*l].split(" ")))

is_scanned = [0 for b in range(B)]


print("books: {0}\tlibraries: {1}\tdays: {2}\n".format(B, L, D))
print(scores)
print(libraries)
print(is_scanned)

def scoring(scores, is_scanned):
    sum = 0
    for i in range(len(scores)):
        sum += scores[i] * is_scanned[i]
    return sum

def filter_signups(lib_order, ):

def find_best_book(is_scanned):
    best = -1
    max_score = 0
    for b in range(B):
        if not is_scanned[b] and scores[b] > max_score:
            best = b
            max_score = scores[b]
    return best

def compute_lib_score(is_scanned, sign_ups, signed_up):
    begin_time = 0
    for i in range(signed_up):
        begin_time += libraries[sign_ups[i]][0][1]
    if begin_time < D:
        while 

print(scoring(scores, is_scanned))
