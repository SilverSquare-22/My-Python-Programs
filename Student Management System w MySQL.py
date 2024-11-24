try:
    import mysql.connector as s
    while True:
        h, u, p = input ('Enter host-> '), input ('Enter username-> '), input ('Enter password-> ')
        try:
            f = s.connect (host = h, user = u, passwd = p)
            break
        except s.errors.DatabaseError:
            print ('Wrong host, username or password. Enter the right credentials.')
            print ('------------------------------------------------------------------------------------------')
    print ('------------------------------------------------------------------------------------------')
    if f.is_connected () == False:
        print ('Error connecting MySQL. Please make sure that the required module(s) is downloaded and try again.')
    else:
        C = f.cursor ()
        C.execute ('CREATE DATABASE IF NOT EXISTS student')
        C.execute ('USE student')
        C.execute ('SHOW TABLES')
        r = C.fetchall ()
        C.execute ('''CREATE TABLE IF NOT EXISTS stutable (AdmnNo int PRIMARY KEY NOT NULL, StudentName varchar (50), FatherName varchar (50), MotherName varchar (50),
               Gender char (1), Class int, Section char (1), OptionalSub varchar (60), Percent_Attendance float, Fees float, Percent_HalfYearly float, Percent_Finals float)''')
        def VS ():
            print ('Enter admission number of the student', end = '')
            while True:
                try:
                    a = int (input ('-> '))
                    C.execute ('SELECT * FROM stutable WHERE AdmnNo = ' + str (a))
                    r = C.fetchall ()
                    if len (r) == 0:
                        print ('No matching record found ❌')
                    else:
                        print ('------------------------------------------------------------------------------------------')
                        print (('AdmnNo:', 'StudentName:', 'FatherName:', 'MotherName:', 'Gender:', 'Class:', 'Section:', 'OptionalSub:', 'Percent_Attendance:', 'Fees:', 'Percent_HalfYearly:', 'Percent_Finals:'))
                        for i in r:
                            print (i)
                    break
                except ValueError:
                    print ('Invalid entry! Enter a valid admission number', end = '')
        def US ():
            print ('Enter admission number of the student whose record is to be updated', end = '')
            while True:
                try:
                    a = int (input ('-> '))
                    C.execute ('SELECT * FROM stutable WHERE AdmnNo = ' + str (a))
                    r = C.fetchall ()
                    if len (r) == 0:
                        print ('No matching record found ❌')
                    else:
                        for i in r:
                            if i [0] == a:
                                def us_1 ():
                                    print ('Enter new admission number', end = '')
                                    while True:
                                        try:
                                            A = int (input ('-> '))
                                            C.execute ('UPDATE stutable SET AdmnNo = ' + str (A) + ' WHERE AdmnNo = ' + str (a))
                                            f.commit ()
                                            break
                                        except ValueError:
                                            print ('Invalid entry! Enter a valid admission number', end = '')
                                def us_2 ():
                                    A = input ('Enter new student name-> ')
                                    C.execute ('UPDATE stutable SET StudentName = ' + "'" + A + "' " + 'WHERE AdmnNo = ' + str (a))
                                    f.commit ()
                                def us_3 ():
                                    A = input ("Enter new father's name-> ")
                                    C.execute ('UPDATE stutable SET FatherName = ' + "'" + A + "' " + 'WHERE AdmnNo = ' + str (a))
                                    f.commit ()
                                def us_4 ():
                                    A = input ("Enter new mother's name-> ")
                                    C.execute ('UPDATE stutable SET MotherName = ' + "'" + A + "' " + 'WHERE AdmnNo = ' + str (a))
                                    f.commit ()
                                def us_5 ():
                                    A = input ('Enter correct gender-> ')
                                    C.execute ('UPDATE stutable SET Gender = ' + "'" + A + "' " + 'WHERE AdmnNo = ' + str (a))
                                    f.commit ()
                                def us_6 ():
                                    print ('Enter new class', end = '')
                                    while True:
                                        try:
                                            A = int (input ('-> '))
                                            C.execute ('UPDATE stutable SET Class = ' + str (A) + ' WHERE AdmnNo = ' + str (a))
                                            f.commit ()
                                            break
                                        except ValueError:
                                            print ('Invalid entry! Enter a valid class', end = '')
                                def us_7 ():
                                    A = input ('Enter new section-> ')
                                    C.execute ('UPDATE stutable SET Section = ' + "'" + A + "' " + 'WHERE AdmnNo = ' + str (a))
                                    f.commit ()
                                def us_8 ():
                                    A = input ('Enter new optional subjects-> ')
                                    C.execute ('UPDATE stutable SET OptionalSub = ' + "'" + A + "' " + 'WHERE AdmnNo = ' + str (a))
                                    f.commit ()
                                def us_9 ():
                                    print ('Enter updated % attendance', end = '')
                                    while True:
                                        try:
                                            A = float (input ('-> '))
                                            C.execute ('UPDATE stutable SET Percent_Attendance = ' + str (A) + ' WHERE AdmnNo = ' + str (a))
                                            f.commit ()
                                            break
                                        except ValueError:
                                            print ('Invalid entry! Enter a valid % attendance', end = '')
                                def us_10 ():
                                    print ('Enter new fees', end = '')
                                    while True:
                                        try:
                                            A = float (input ('-> '))
                                            C.execute ('UPDATE stutable SET Fees = ' + str (A) + ' WHERE AdmnNo = ' + str (a))
                                            f.commit ()
                                            break
                                        except ValueError:
                                            print ('Invalid entry! Enter a valid fee', end = '')
                                def us_11 ():
                                    print ('Enter correct % Half Yearly', end = '')
                                    while True:
                                        try:
                                            A = float (input ('-> '))
                                            C.execute ('UPDATE stutable SET Percent_HalfYearly = ' + str (A) + ' WHERE AdmnNo = ' + str (a))
                                            f.commit ()
                                            break
                                        except ValueError:
                                            print ('Invalid entry! Enter a valid % Half Yearly', end = '')
                                def us_12 ():
                                    print ('Enter correct % Finals', end = '')
                                    while True:
                                        try:
                                            A = float (input ('-> '))
                                            C.execute ('UPDATE stutable SET Percent_Finals = ' + str (A) + 'WHERE AdmnNo = ' + str (a))
                                            f.commit ()
                                            break
                                        except ValueError:
                                            print ('Invalid entry! Enter a valid % Finals', end = '')
                                print ('------------------------------------------------------------------------------------------')
                                print ("Menu:\n1=> Admission Number        2=> Student Name        3=> Father's Name        4=> Mother's Name")
                                print ('5=> Gender                     6=> Class                  7=> Section                 8=> Optional Subjects')
                                print ('9=> % Attendance            10=> Fees                 11=> % Half Yearly        12=> % Finals')
                                print ('------------------------------------------------------------------------------------------')
                                print ('Enter the code corresponding to your choice [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 or 12]', end = '')
                                while True:
                                    try:
                                        u = int (input ('-> '))
                                        if u == 1:
                                            us_1 ()
                                            print ('Record updated ✔')
                                            break
                                        elif u == 2:
                                            us_2 ()
                                            print ('Record updated ✔')
                                            break
                                        elif u == 3:
                                            us_3 ()
                                            print ('Record updated ✔')
                                            break
                                        elif u == 4:
                                            us_4 ()
                                            print ('Record updated ✔')
                                            break
                                        elif u == 5:
                                            us_5 ()
                                            print ('Record updated ✔')
                                            break
                                        elif u == 6:
                                            us_6 ()
                                            print ('Record updated ✔')
                                            break
                                        elif u == 7:
                                            us_7 ()
                                            print ('Record updated ✔')
                                            break
                                        elif u == 8:
                                            us_8 ()
                                            print ('Record updated ✔')
                                            break
                                        elif u == 9:
                                            us_9 ()
                                            print ('Record updated ✔')
                                            break
                                        elif u == 10:
                                            us_10 ()
                                            print ('Record updated ✔')
                                            break
                                        elif u == 11:
                                            us_11 ()
                                            print ('Record updated ✔')
                                            break
                                        elif u == 12:
                                            us_12 ()
                                            print ('Record updated ✔')
                                            break
                                        else:
                                            print ('Invalid entry! Enter a valid choice', end = '')
                                    except ValueError:
                                        print ('Invalid entry! Enter a valid choice', end = '')
                            break
                        else:
                            print ('No matching record found ❌')
                    break
                except ValueError:
                    print ('Invalid entry! Enter a valid admission number', end = '')
        def AS ():
            k = 'Y'
            while k == 'Y':
                while True:
                    try:
                        a1 = int (input ('Enter admission number-> '))
                        b2 = input ("Enter student's name-> ")
                        c3 = input ("Enter father's name-> ")
                        d4 = input ("Enter mother's name-> ")
                        e5 = input ('Enter gender-> ')
                        f6 = int (input ('Enter class-> '))
                        g7 = input ('Enter section-> ')
                        h8 = input ('Enter optional subjects-> ')
                        i9 = float (input ('Enter % attendance-> '))
                        j10 = float (input ('Enter fees-> '))
                        k11 = float (input ('Enter % Half Yearly-> '))
                        l12 = float (input ('Enter % Finals-> '))
                        C.execute ("INSERT INTO stutable VALUES ({}, '{}', '{}', '{}', '{}', {}, '{}', '{}', {}, {}, {}, {})".format (a1, b2, c3, d4, e5, f6, g7, h8, i9, j10, k11, l12))
                        f.commit ()
                        print ('------------------------------------------------------------------------------------------')
                        print ('Record added ✔')
                        break
                    except (ValueError, s.errors.IntegrityError):
                        print ('Invalid entry! Enter a valid detail.')
                        print ('------------------------------------------------------------------------------------------')
                k = input ('Whether more records to be added? (Choose Y for YES and N for NO)-> ')
        def DS ():
            k = 'Y'
            C.execute ('SELECT * FROM stutable')
            r = C.fetchall ()
            if len (r) == 0:
                print ('EMPTY SET')
            else:
                while k == 'Y':
                    print ('Enter admission number of the student whose record is to be deleted', end = '')
                    while True:
                        try:
                            a = int (input ('-> '))
                            for i in r:
                                if i [0] == a:
                                    C.execute ('DELETE FROM stutable WHERE AdmnNo = ' + str (a))
                                    f.commit ()
                                    print ('Record deleted ✔')
                                    print ('------------------------------------------------------------------------------------------')
                                    k = input ('Whether more records to be deleted? (Choose Y for YES and N for NO)-> ')
                                    break
                            else:
                                print ('No matching record found ❌')
                                k = 'N'
                                break
                            break
                        except ValueError:
                            print ('Invalid entry! Enter a valid admission number', end = '')
        def oth ():
            print ('Enter a query that you would like to execute', end = '')
            while True:
                try:
                    q = input ('-> ')
                    C.execute (q)
                    r = C.fetchall ()
                    if len (r) != 0:
                        print ('------------------------------------------------------------------------------------------')
                        for i in r:
                            print (i)
                        break
                    else:
                        print ('EMPTY SET')
                        break
                except s.errors.ProgrammingError:
                    print ('Invalid entry! Enter a valid query', end = '')
        print ('Welcome to Student Management System!\nChoose the desired option to work with:')
        print ('1=> View student details')
        print ('2=> Update student details')
        print ('3=> Add a student')
        print ('4=> Delete a student')
        print ('5=> Other')
        while True:
            try:
                c = int (input ('-> '))
                if c == 1:
                    VS ()
                    break
                elif c == 2:
                    US ()
                    break
                elif c == 3:
                    AS ()
                    break
                elif c == 4:
                    DS ()
                    break
                elif c == 5:
                    oth ()
                    break
                else:
                    print ('Invalid entry! Enter a valid choice [1, 2, 3, 4 or 5]', end = '')
            except ValueError:
                print ('Invalid entry! Enter a valid choice [1, 2, 3, 4 or 5]', end = '')
        f.close ()
except ModuleNotFoundError:
    print ('The required module(s) does not exist. Please install and try again.')
