import input

def scoring(scores, is_scanned):
    sum = 0
    for i in range(len(scores)):
        sum += scores[i] * is_scanned[i]
    return sum

# def find_best_book(is_scanned, books):
#     best = -1
#     max_score = 0
#     for b in books:
#         if not is_scanned[b] and scores[b] > max_score:
#             best = b
#             max_score = scores[b]
#     return best
#
# def compute_lib_score(is_scanned, sign_ups, signed_up, lib):
#     begin_time = 0
#     lib_score = 0
#     my_scanned = copy.deepcopy(is_scanned)
#     for i in range(signed_up):
#         begin_time += libraries[sign_ups[i]][0][1]
#     begin_time += lib[0][1]
#     if begin_time < D:
#         to_scan = (D - begin_time) * lib[0][2]
#         for i in range(to_scan):
#             best = find_best_book(my_scanned, lib[1])
#             if best >= 0:
#                 my_scanned[best] = 1
#                 lib_score += scores[best]
#     return [lib_score, ]

def compute_scanned(scans):
    scanned = [0 for i in range(B)]
    for scan in scans:
        for b in scan:
            scanned[b] = 1
    return scanned

def compute_available_libs(libraries, sign_up, day):
    available = []
    next_day = libraries[sign_up[0]][0][1]
    i = 0
    while next_day < day:
        available.append(sign_up[i])
        i += 1
        next_day += libraries[sign_up[i]][0][1]
    return available


def compute_scans(sign_up):
    scans = [[]]
    for d in range(D):
        available_libs = compute_available_libs(sign_up, d)




def find_best_lib(is_scanned, sign_ups, signed_up):
    best_= -1
    max_score = 0
    for l in libraries:
        break
    return best
