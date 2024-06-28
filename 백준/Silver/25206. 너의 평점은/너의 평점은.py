gs = {'A+': 4.5, "A0": 4.0, 'B+': 3.5, "B0": 3.0, 'C+': 2.5, "C0": 2.0, 'D+': 1.5, "D0": 1.0, 'F': 0.0}
sc_hap = 0 
gr_hap = 0
for _ in range(20):
    ob, sc, gr = map(str, input().split())

    if gr != 'P':
        gr_hap += float(sc)
        sc_hap += gs[gr] * float(sc)

print('%.6f' % (sc_hap / gr_hap))