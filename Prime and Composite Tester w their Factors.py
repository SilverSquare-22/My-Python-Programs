n, s = int (input ('Enter a number: ')), 0
if n not in (0, 1):
    print ('\nFactors: ', end = '')
for i in range (1, n):
    if n % i == 0:
        print (i, end = ', ')
        s += 1
if s == 1:
    print (n, '\n=> It is a prime number.')
else:
    if n in (0, 1):
        print ('\nFactor:', n, '\n=> It is neither a prime number nor a composite number.')
    else:
        print (n, '\n=> It is a composite number.')
