d = input ("Enter the date of the format 'DD-MM-YYYY' ('-' included): ")
while len (d) != 10 or (int (d [: 2]) > 31) or (int (d [3:5]) > 12) or (d [: 5] in ('29-02', '30-02', '31-02', '31-04', '31-06', '31-09', '31-11')):
    if (d [: 5] == '29-02') and ((int (d [-4:]) % 4 == 0 and int (d [-4:]) % 100 != 0) or (int (d [-4:]) % 400 == 0)):
        break
    else:
        d = input ("Enter correct date ('DD-MM-YYYY' format): ")
s = int (d [:2]) + int (d [-2:]) + ((int (d [-2:]))//4)
if ((int (d [-4:]) % 4 == 0 and int (d [-4:]) % 100 != 0) or (int (d [-4:]) % 400 == 0)) and d [3:5] in ('01', '02'):
    s -= 1
if d [3:5] in ('01', '10'):
    s += 1
elif d [3:5] == '05':
    s += 2
elif d [3:5] == '08':
    s += 3
elif d [3:5] in ('02', '03', '11'):
    s += 4
elif d [3:5] == '06':
    s += 5
elif d [3:5] in ('09', '12'):
    s += 6
if (int (d [-4:-2]) + 1) % 4 == 1:
    s += 6
elif (int (d [-4:-2]) + 1) % 4 == 2:
    s += 4
elif (int (d [-4:-2]) + 1) % 4 == 3:
    s += 2
D = {0: '>>> Saturday!', 1: '>>> Sunday!', 2: '>>> Monday!', 3: '>>> Tuesday!', 4: '>>> Wednesday!', 5: '>>> Thursday!', 6: '>>> Friday!'}
print (D [s % 7])
