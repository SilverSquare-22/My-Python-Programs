def evenlen (s):
    for j in s:
        if s.count (j) % 2 !=0:
            print ('\nIt cannot be rearranged into a palindrome.')
        else:
            print ('\nIt can be rearranged into a palindrome.')
        break
s = input ('Enter a string: ')
s = s.lower ()
if len (s) % 2 == 0:
    evenlen (s)
else:
    for i in s:
        if s.count (i) % 2 != 0:
            s = s.replace (i, '')
            break
    evenlen (s)
