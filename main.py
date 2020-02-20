from input import *

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

def compute_available_libs(sign_up, day):
    available = []
    next_day = 0
    for lib in sign_up:
        next_day += libraries[lib][0][1]
        if next_day < day:
            available += [lib]
        else:
            break
    # while next_day < day:
    #     available += [sign_up[i]]
    #     i += 1
    #     print(i, sign_up, day)
    #     next_day += libraries[sign_up[i]][0][1]
    return available

def gluton_books(lib, scanned_books):
    books = []
    scannable = libraries[lib][1]
    for i in range(len(scanned_books)):
        if scanned_books[i]:
            try:
                scannable.remove(i)
            except ValueError:
                pass
    for i in range(libraries[lib][0][2]):
        if scannable:
            best = scannable[0]
            for book in scannable:
                if scores[book] > scores[best]:
                    best = book
            books += [best]
            try:
                scannable.remove(best)
            except ValueError:
                pass
    return books

def compute_scans(sign_up):
    scans = [[] for l in range(L)]
    scanned_books = [0 for i in range(B)]
    for d in range(D):
        available_libs = compute_available_libs(sign_up, d)
        print(available_libs)
        for lib in available_libs:
            scans[lib] += gluton_books(lib, scanned_books)
            for list in scans:
                for i in list:
                    scanned_books[i] = 1
    return scans

print("B: {0}\tL: {1}\tD: {2}\n".format(B, L, D))
print(scores)
print(libraries)
scans = compute_scans(list(range(L)))
is_scanned = compute_scanned(scans)
print(scans)
print(is_scanned)
print(scoring(scores, is_scanned))