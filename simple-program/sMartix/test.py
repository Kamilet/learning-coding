from sMartix import *


a = [[1, 2], [1, 0]]
b = Smatrix(a).clean(echo=1)
c = [[1, 3, 4], [2, '']]
d = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]


sm_check(a)
print(sm_numcheck(a))
print(a)
print(b)
print(sm_cons(c, echo=1))
e = Smatrix(d)
e.view()
e = e.rotate('mirrorcolume')
e = Smatrix(e)
e.view()
print(help(Smatrix))


print(sm_numcheck([['A',1],[1,2]]))
print(sm_numcheck([['1',1],[1,2]]))
print(sm_numcheck([[1,1.321],[1,2]]))

print(sm_number([['A',1],[1,2]], force = 1))
print(sm_number([['1',1],[1,2]]))
print(sm_number([[1,1.321],[1,2]]))


a_1 = [[1,'A'],[1,1]]
a_2 = [[1, 1],[1,2]]
a_3 = [[1,'1'],[2,4]]
print(sm_minus(a_1,a_2,force = 1))

print(sm_gen(4,eye=1))
a = [[1, 2, 1, 5],
     [1, 2, 1, 4],
     [1, 1, 1, 6],
     [1, 7, 2, 5]]
A = Smatrix(a)
print('Start with',A.find('',2,'r',1),'in row')
print('Start with',A.find('',2,'c',1),'in colume')
print('Start with',A.find(1,3,'o',1),'in oblique')

mu1 = [[1,0,2],
       [-1,3,1]]

mu2 = [[3,1],
       [2,1],
       [1,0]]

mu3 = [[5,1],
       [2,2]]

print('矩阵1:')
Smatrix(mu1).view()
print('矩阵1，转置:')
temp = Smatrix(mu1).rotate()
Smatrix(temp).view()

print('矩阵1:')
Smatrix(mu1).view()
print('矩阵1+矩阵1:')
temp = sm_sum(mu1,mu1)
Smatrix(temp).view()

print('矩阵1:')
Smatrix(mu1).view()
print('矩阵2:')
Smatrix(mu2).view()
print('矩阵1 * 矩阵2:')
temp = sm_multis(mu1,mu2)
Smatrix(temp).view()
print('矩阵2 * 矩阵1:')
temp = sm_multis(mu2,mu1)
Smatrix(temp).view()
print('矩阵1 * 矩阵2 * 5:')
temp = sm_multis(mu1,5,mu2)
Smatrix(temp).view()

print('矩阵3:')
Smatrix(mu3).view()
print('矩阵1 * 矩阵2 * 矩阵3:')
temp = sm_multis(mu1,mu2,mu3)
Smatrix(temp).view()

print('矩阵1 * 矩阵3:前列后行不等报错')
#temp = sm_multis(mu1,mu3)

mu4 = [[1,0,2],
       [-1,3,1]]
print(sm_trans(mu4))
m5 = [[(1+1j),(4-2j)],[4,(-1j)]]
print(sm_con_trans(m5))

mu6 = [[1,1,1],
       [3,1,4],
       [8,9,5]]

mu7 = [[0,0,-1,0],
       [0,1,0,0],
       [-1,0,1,0]]

print(sm_det(mu6))
print(sm_det(mu7,force=1))



mu8 = [[0,1,2],
       [1,1,4],
       [2,-1,0]]
a = sm_inverse(mu8)
Smatrix(a).view()

mu9 = [[1,2,3],
       [2,2,1],
       [3,4,3]]

print(sm_det(mu9))
print(sm_alge(mu9,0,0))
print(sm_alge(mu9,1,0))
print(sm_alge(mu9,2,0))
print(sm_alge(mu9,0,1))
print(sm_alge(mu9,1,1))
print(sm_alge(mu9,2,1))
print(sm_alge(mu9,0,2))
print(sm_alge(mu9,1,2))
print(sm_alge(mu9,2,2))
print(sm_inverse(mu9))
