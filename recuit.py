import main
import random

kmax = 500
emax = 2000000

#Defining voisin()
def switch_close(scans):
	switched = scans.copy()
	index = randint(0, len(switched) - 1)
	next = (index + 1) if ((index + 1) < len(switched)) else (index - 1)
	switched[index], switched[next] = switched[next], switched[index]
	return switched

def recuit() :
	#Generating state 0
	s = []

	for l in range(l) :
		s.append(l)

	g = s.copy()

	scans = compute_scans(s)
	e = scoring(scans, compute_scanned(scans))
	m = e

	k = 0

	while (k < kmax and e < emax) :
		sn = switch_close(s)
		scans_n = compute_scans(sn)
		en = scoring(scans_n, compute_scanned(scans_n))
		if (en > e or random.random() < P(en - e, temp(k/kmax))) :
			s, e = sn, en
		if e > m :
			g, m = s.copy, e
		k += 1
	return g