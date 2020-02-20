import input

def scoring(scores, is_scanned):
    sum = 0
    for i in range(len(scores)):
        sum += scores[i] * is_scanned[i]
    return sum

def find_best_book(is_scanned, books):
    best = -1
    max_score = 0
    for b in books:
        if not is_scanned[b] and scores[b] > max_score:
            best = b
            max_score = scores[b]
    return best

def compute_lib_score(is_scanned, sign_ups, signed_up):
    begin_time = 0
    lib_score = 0
    for i in range(signed_up):
        begin_time += libraries[sign_ups[i]][0][1]
    if begin_time < D:
        print(a)
    return lib_score

def find_best_lib(is_scanned, sign_ups, signed_up):
    best_= -1
    max_score = 0
    for l in libraries:
        break
    return best
