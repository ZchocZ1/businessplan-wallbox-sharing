import sys; sys.path.insert(0,'.')
import slides_a as A, slides_b as B, slides_c as C
for f in (A.s01,A.s02,A.s03,A.s04,A.s05,B.s06,B.s07,B.s08,B.s09,C.s10,C.s11,C.s12,C.s13,C.s14): f()
print('rendered 14')
