import math
print ('''You are now using "Anagha's Mini Calculator".\n\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions''')
C = 'Y'
def pre ():
    global p
    if n in [-1, 1]:
        p = 'st'
    elif n in [-2, 2]:
        p = 'nd'
    elif n in [-3, 3]:
        p = 'rd'
    else:
        p = 'th'
while C.upper () == 'Y':
    c = int (input ("\n(Choose from the codes '1-19')-> "))
    if c == 1:
        s, D = float (input ('\n\nEnter the 1st number: ')), 'Y'
        while D.upper () == 'Y':
            o = input ("Enter the operation among '+ - * /': ")
            if o == '+':
                i = float (input ('Enter the next number: '))
                s += i
                D = input ('More numbers to be operated? (Choose Y/N): ')
            elif o == '-':
                i = float (input ('Enter the next number: '))
                s -= i
                D = input ('More numbers to be operated? (Choose Y/N): ')
            elif o == '*':
                i = float (input ('Enter the next number: '))
                s *= i
                D = input ('More numbers to be operated? (Choose Y/N): ')
            elif o == '/':
                i = float (input ('Enter the next number: '))
                try:
                    s /= i
                    D = input ('More numbers to be operated? (Choose Y/N): ')
                except ZeroDivisionError:
                    print ('⚠ Division by zero not allowed !!!')
            else:
                print ('Invalid entry!')
        print ('---------------\nComputed value =', s)
        C = input ('---------------\n\nWant to calculate something else? (Choose Y/N): ')
        if C.upper () == 'Y':
            print ("\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions")
    elif c == 2:
        while True:
            print ('\n\nYour choices:\n2.1=> Calculate percentage of input fraction\n2.2=> Calculate fraction of input percentage')
            sc = float (input ("\n(Choose from the codes '2.1 & 2.2')-> "))
            if sc == 2.1:
                while True:
                    f = input ('\nDecimal or fraction? (Choose D/F accordingly): ')
                    if f.upper () == 'D':
                        s = float (input ('Enter the fraction in decimals: '))
                        print ('---------------\nPercentage =', str (s * 100) + '%')
                        break
                    elif f.upper () == 'F':
                        n, d = int (input ('Enter the numerator: ')), int (input ('Enter the denominator: '))
                        print ('---------------\nPercentage =', str ((n/d) * 100) + '%')
                        break
                    else:
                        print ('Invalid entry!')
                break
            elif sc == 2.2:
                p = float (input ("Enter the percentage (without the '%' symbol): "))
                print ('---------------\nFraction =', p/100)
                break
            else:
                print ('Invalid entry!')
        C = input ('---------------\n\nWant to calculate something else? (Choose Y/N): ')
        if C.upper () == 'Y':
            print ("\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions")
    elif c == 3:
        s = float (input ('\n\nEnter the number: '))
        try:
            print ('---------------\nReciprocal =', 1/s)
        except ZeroDivisionError:
            print ('---------------\nReciprocal of zero does not exist.')
        C = input ('---------------\n\nWant to calculate something else? (Choose Y/N): ')
        if C.upper () == 'Y':
            print ("\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions")
    elif c == 4:
        s = float (input ('\n\nEnter the number: '))
        print ('---------------\nSquare =', s ** 2)
        C = input ('---------------\n\nWant to calculate something else? (Choose Y/N): ')
        if C.upper () == 'Y':
            print ("\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions")
    elif c == 5:
        s = float (input ('\n\nEnter the number: '))
        try:
            print ('---------------\nSquare Root =', math.sqrt (s))
        except ValueError:
            print ('---------------\nSquare roots of negative numbers do not exist.')
        C = input ('---------------\n\nWant to calculate something else? (Choose Y/N): ')
        if C.upper () == 'Y':
            print ("\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions")
    elif c == 6:
        s = float (input ('\n\nEnter the number: '))
        print ('---------------\nCube =', s ** 3)
        C = input ('---------------\n\nWant to calculate something else? (Choose Y/N): ')
        if C.upper () == 'Y':
            print ("\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions")
    elif c == 7:
        s = float (input ('\n\nEnter the number: '))
        if s >= 0:
            print ('---------------\nCube Root =', s ** (1/3))
        else:
            print ('---------------\nCube Root = -' + str (abs (s ** (1/3))))
        C = input ('---------------\n\nWant to calculate something else? (Choose Y/N): ')
        if C.upper () == 'Y':
            print ("\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions")
    elif c == 8:
        s, n = float (input ('\n\nEnter the number: ')), int (input ("Enter the value of 'n': "))
        pre ()
        print ('---------------\n' + str (n) + p, 'Power =', s ** n)
        C = input ('---------------\n\nWant to calculate something else? (Choose Y/N): ')
        if C.upper () == 'Y':
            print ("\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions")
    elif c == 9:
        while True:
            s, n = float (input ('\n\nEnter the number: ')), float (input ("Enter the value of 'n': "))
            if n == 0:
                print ('Invalid entry!')
            else:
                pre ()
                if s >= 0:
                    print ('---------------\n' + str (n) + p, 'Root =', s ** (1/n))
                    break
                else:
                    if n % 2 != 0:
                        print ('---------------\n' + str (n) + p, 'Root = -' + str (abs (s ** (1/n))))
                        break
                    else:
                        print ('---------------\n' + str (n) + p, 'root of negative numbers does not exist.')
                        break
        C = input ('---------------\n\nWant to calculate something else? (Choose Y/N): ')
        if C.upper () == 'Y':
                print ("\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions")
    elif c == 10:
        s = float (input ('\n\nEnter the exponent: '))
        print ('---------------\ne^(' + str (s) + ') =', math.exp (s))
        C = input ('---------------\n\nWant to calculate something else? (Choose Y/N): ')
        if C.upper () == 'Y':
            print ("\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions")
    elif c == 11:
        s = float (input ('\n\nEnter the exponent: '))
        print ('---------------\nπ^(' + str (s) + ') =', (math.pi) ** (s))
        C = input ('---------------\n\nWant to calculate something else? (Choose Y/N): ')
        if C.upper () == 'Y':
            print ("\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions")
    elif c == 12:
        s = float (input ('\n\nEnter the number inside log: '))
        try:
            print ('---------------\nlog (' + str (s) + ') =', math.log (s, 10))
        except ValueError:
            print ("---------------\nLogarithms of zero and negative numbers to the base '10' do not exist.")
        C = input ('---------------\n\nWant to calculate something else? (Choose Y/N): ')
        if C.upper () == 'Y':
            print ("\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions")
    elif c == 13:
        s = float (input ('\n\nEnter the number inside log: '))
        try:
            print ('---------------\nln (' + str (s) + ') =', math.log (s))
        except ValueError:
            print ("---------------\nLogarithms of zero and negative numbers to the base 'e' do not exist.")
        C = input ('---------------\n\nWant to calculate something else? (Choose Y/N): ')
        if C.upper () == 'Y':
            print ("\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions")
    elif c == 14:
        s, n = float (input ('\n\nEnter the number inside log: ')), float (input ('Enter the base: '))
        try:
            print ('---------------\nlog', (s, n), '=', math.log (s, n))
        except ValueError:
            print ('---------------\nLogarithms of zero and negative numbers or to zero and negative bases do not exist.')
        C = input ('---------------\n\nWant to calculate something else? (Choose Y/N): ')
        if C.upper () == 'Y':
            print ("\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions")
    elif c == 15:
        s = float (input ('\n\nEnter a number: '))
        print ('|' + str (s) + '| =', abs (s))
        C = input ('---------------\n\nWant to calculate something else? (Choose Y/N): ')
        if C.upper () == 'Y':
            print ("\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions")
    elif c == 16:
        s, n = int (input ('\n\nEnter a number: ')), 1
        if s == 0:
            print ('---------------\n0! = 1')
        elif s > 0:
            for i in range (2, s + 1):
                n *= i
            print ('---------------\n' + str (s) + '! =', n)
        else:
            print ('---------------\nFactorials of negative numbers do not exist.')
        C = input ('---------------\n\nWant to calculate something else? (Choose Y/N): ')
        if C.upper () == 'Y':
            print ("\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions")
    elif c == 17:
        while True:
            print ('\n\nYour choices:\n17.1=> Degree to Radian\n17.2=> Radian to Degree')
            sc = float (input ("\n(Choose from the codes '17.1 & 17.2')-> "))
            if sc == 17.1:
                s = float (input ('Enter the angle in degrees: '))
                print ('---------------\nAngle in radians =', str (math.radians (s)) + 'ᶜ')
                break
            elif sc == 17.2:
                s = float (input ('Enter the angle in radians: '))
                print ('---------------\nAngle in degrees =', str (math.degrees (s)) + '°')
                break
            else:
                print ('Invalid entry!')
        C = input ('---------------\n\nWant to calculate something else? (Choose Y/N): ')
        if C.upper () == 'Y':
            print ("\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions")
    elif c == 18:
        while True:
            print ('\n\nWhat should be the unit of your input?:\nA. Degrees\nB. Radians')
            sc = input ("\n(Choose from the codes 'A & B')-> ")
            if sc.upper () == 'A':
                s = float (input ('Enter the angle in degrees: '))
                u = str (s) + '°'
                s = math.radians (s)
                break
            elif sc.upper () == 'B':
                s = float (input ('Enter the angle in radians: '))
                u = str (s) + 'ᶜ'
                break
            else:
                print ('Invalid entry!')
        while True:
            print ('\nYour choices:\n18.1=> sine function (sin)\n18.2=> cosine function (cos)\n18.3=> tangent function (tan)\n18.4=> cotangent function (cot)\n18.5=> cosecant function (cosec)\n18.6=> secant function (sec)')
            Sc = float (input ("\n(Choose from the codes '18.1, 18.2, 18.3, 18.4, 18.5 & 18.6')-> "))
            try:
                if Sc == 18.1:
                    f = '---------------\nsin '
                    print (f + u, '=', math.sin (s))
                    break
                elif Sc == 18.2:
                    f = '---------------\ncos '
                    print (f + u, '=', math.cos (s))
                    break
                elif Sc == 18.3:
                    f = '---------------\ntan '
                    print (f + u, '=', math.tan (s))
                    break
                elif Sc == 18.4:
                    f = '---------------\ncot '
                    print (f + u, '=', 1/(math.tan (s)))
                    break
                elif Sc == 18.5:
                    f = '---------------\ncosec '
                    print (f + u, '=', 1/(math.sin (s)))
                    break
                elif Sc == 18.6:
                    f = '---------------\nsec '
                    print (f + u, '=', 1/(math.cos (s)))
                    break
                else:
                    print ('Invalid entry!')
            except:
                print (f + u + 'does not exist.')
                break
        C = input ('---------------\n\nWant to calculate something else? (Choose Y/N): ')
        if C.upper () == 'Y':
            print ("\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions")
    elif c == 19:
        while True:
            while True:
                print ('\n\nWhat should be the unit of your output?:\nA. Degrees\nB. Radians')
                sc = input ("\n(Choose from the codes 'A & B')-> ")
                if sc not in ['A', 'a', 'B', 'b']:
                    print ('Invalid entry!')
                else:
                    break
            print ('\nYour choices:\n19.1=> sine inverse (sin⁻¹)\n19.2=> cosine inverse (cos⁻¹)\n19.3=> tangent inverse (tan⁻¹)\n19.4=> cotangent inverse (cot⁻¹)\n19.5=> cosecant inverse (cosec⁻¹)\n19.6=> secant inverse (sec⁻¹)')
            Sc, a = float (input ("\n(Choose from the codes '19.1, 19.2, 19.3, 19.4, 19.5 & 19.6')- >")), math.radians (90)
            try:
                s = float (input ('Enter the value: '))
                if Sc == 19.1:
                    f = '---------------\nsin⁻¹ '
                    if sc.upper () == 'A':
                        print (f + str (s) + ' =', str (math.degrees (math.asin (s))) + '°')
                    if sc.upper () == 'B':
                        print (f + str (s) + ' =', str (math.asin (s)) + 'ᶜ')
                    break
                elif Sc == 19.2:
                    f = '---------------\ncos⁻¹ '
                    if sc.upper () == 'A':
                        print (f + str (s) + ' =', str (math.degrees (math.acos (s))) + '°')
                    if sc.upper () == 'B':
                        print (f + str (s) + ' =', str (math.acos (s)) + 'ᶜ')
                    break
                elif Sc == 19.3:
                    f = '---------------\ntan⁻¹ '
                    if sc.upper () == 'A':
                        print (f + str (s) + ' =', str (math.degrees (math.atan (s))) + '°')
                    if sc.upper () == 'B':
                        print (f + str (s) + ' =', str (math.atan (s)) + 'ᶜ')
                    break
                elif Sc == 19.4:
                    f = '---------------\ncot⁻¹ '
                    if sc.upper () == 'A':
                        print (f + str (s) + ' =', str (math.degrees (a - math.atan (s))) + '°')
                    if sc.upper () == 'B':
                        print (f + str (s) + ' =', str (a - math.atan (s)) + 'ᶜ')
                    break
                elif Sc == 19.5:
                    f = '---------------\ncosec⁻¹ '
                    if sc.upper () == 'A':
                        print (f + str (s) + ' =', str (math.degrees (a - math.asin (1/s))) + '°')
                    if sc.upper () == 'B':
                        print (f + str (s) + ' =', str (math.asin (1/s)) + 'ᶜ')
                    break
                elif Sc == 19.6:
                    f = '---------------\nsec⁻¹ '
                    if sc.upper () == 'A':
                        print (f + str (s) + ' =', str (math.degrees (a - math.acos (1/s))) + '°')
                    if sc.upper () == 'B':
                        print (f + str (s) + ' =', str (math.acos (1/s)) + 'ᶜ')
                    break
                else:
                    print ('Invalid entry!')
            except:
                print (f + str (s), 'does not exist.')
                break
        C = input ('---------------\n\nWant to calculate something else? (Choose Y/N): ')
        if C.upper () == 'Y':
            print ("\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions")
    else:
        print ("Invalid entry!\n\nChoose what you wish to find:\n1=> Arithmetic Operations\n2=> Percentage\n3=> Reciprocal\n4=> Square\n5=> Square Root\n6=> Cube\n7=> Cube Root\n8=> nth Power\n9=> nth Power Root\n10=> Exponent of 'e'\n11=> Exponent of 'π'\n12=> Logarithm to the base '10'\n13=> Logarithm to the base 'e'\n14=> Logarithm to any base\n15=> Modulus\n16=> Factorial\n17=> Angle Converter\n18=> Trigonometric Functions\n19=> Inverse Trigonometric Functions")
print ('\n\nThank you for using the calculator! :)')
