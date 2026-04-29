import functions as f
import math
k = 1
x = int(input('input: '))
print('answer for task a:')
for i in f.rec_a(x):
    print(i,)
    k+=1
    if k>10:
        break
i = 1
for s in f.rec_b(i):
    i+=1
    if i>5:
        break
print('\nanswer to the task b is: ', s, '\n')
n = int(input('input n for det: '))
print('\nlist of answers for task c:')
for det in f.rec_c(n):
    print(det)
print('\nanswers for d:')
for a in f.rec_d(n):
    print(a)
alpha = float(input('input alpha: '))
print(f'sin({alpha}) = ', list(f.rec_e(alpha))[-1], 'using Taylor\'s series')
print(f'using math function: sin({alpha}) = ', math.sin(alpha))