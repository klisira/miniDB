from database import Database
from time import sleep

db = Database("smdb", load=False)

db.create_table('classroom', ['building', 'room_number', 'capacity'], [str,str,int])
db.create_table('department', ['dept_name', 'building', 'budget'], [str,str,int], primary_key='dept_name')
db.create_table('course', ['course_id', 'title', 'dept_name', 'credits'], [str,str,str,int], primary_key='course_id')
db.create_table('instructor', ['ID', 'name', 'dept_name','salary'], [str,str,str,int], primary_key='ID')
db.create_table('section', ['course_id', 'sec_id', 'semester','year','building','room_number','time_slot_id'], [str,str,str,int,str,str,str])
db.create_table('teaches', ['ID', 'course_id', 'sec_id', 'semester', 'year'], [str,str,str,str,int])
db.create_table('student', ['ID', 'name', 'dept_name', 'tot_cred'], [str,str,str,int], primary_key='ID')
db.create_table('takes', ['ID', 'course_id', 'sec_id', 'semester', 'year', 'grade'], [str,str,str,str,int,str])
db.create_table('advisor', ['s_ID', 'i_ID'], [str,str], primary_key='s_ID')
db.create_table('time_slot', ['time_slot_id', 'day', 'start_hr', 'start_min', 'end_hr', 'end_min'], [str,str,int,int,str,str])
db.create_table('prereq', ['course_id', 'prereq_id'], [str,str])

db.insert('classroom', ['Packard', '101', '500'])
db.insert('classroom', ['Painter', '514', '10'])
db.insert('classroom', ['Taylor', '3128', '70'])
db.insert('classroom', ['Watson', '100', '30'])
db.insert('classroom', ['Watson', '120', '50'])
db.insert('department', ['Biology', 'Watson', '90000'])
db.insert('department', ['Comp. Sci.', 'Taylor', '100000'])
db.insert('department', ['Elec. Eng.', 'Taylor', '85000'])
db.insert('department', ['Finance', 'Painter', '120000'])
db.insert('department', ['History', 'Painter', '50000'])
db.insert('department', ['Music', 'Packard', '80000'])
db.insert('department', ['Physics', 'Watson', '70000'])
db.insert('course', ['BIO-101', 'Intro. to Biology', 'Biology', '4'])
db.insert('course', ['BIO-301', 'Genetics', 'Biology', '4'])
db.insert('course', ['BIO-399', 'Computational Biology', 'Biology', '3'])
db.insert('course', ['CS-101', 'Intro. to Computer Science', 'Comp. Sci.', '4'])
db.insert('course', ['CS-190', 'Game Design', 'Comp. Sci.', '4'])
db.insert('course', ['CS-315', 'Robotics', 'Comp. Sci.', '3'])
db.insert('course', ['CS-319', 'Image Processing', 'Comp. Sci.', '3'])
db.insert('course', ['CS-347', 'Database System Concepts', 'Comp. Sci.', '3'])
db.insert('course', ['EE-181', 'Intro. to Digital Systems', 'Elec. Eng.', '3'])
db.insert('course', ['FIN-201', 'Investment Banking', 'Finance', '3'])
db.insert('course', ['HIS-351', 'World History', 'History', '3'])
db.insert('course', ['MU-199', 'Music Video Production', 'Music', '3'])
db.insert('course', ['PHY-101', 'Physical Principles', 'Physics', '4'])
db.insert('instructor', ['10101', 'Srinivasan', 'Comp. Sci.', '65000'])
db.insert('instructor', ['12121', 'Wu', 'Finance', '90000'])
db.insert('instructor', ['15151', 'Mozart', 'Music', '40000'])
db.insert('instructor', ['22222', 'Einstein', 'Physics', '95000'])
db.insert('instructor', ['32343', 'El Said', 'History', '60000'])
db.insert('instructor', ['33456', 'Gold', 'Physics', '87000'])
db.insert('instructor', ['45565', 'Katz', 'Comp. Sci.', '75000'])
db.insert('instructor', ['58583', 'Califieri', 'History', '62000'])
db.insert('instructor', ['76543', 'Singh', 'Finance', '80000'])
db.insert('instructor', ['76766', 'Crick', 'Biology', '72000'])
db.insert('instructor', ['83821', 'Brandt', 'Comp. Sci.', '92000'])
db.insert('instructor', ['98345', 'Kim', 'Elec. Eng.', '80000'])
db.insert('section', ['BIO-101', '1', 'Summer', '2009', 'Painter', '514', 'B'])
db.insert('section', ['BIO-301', '1', 'Summer', '2010', 'Painter', '514', 'A'])
db.insert('section', ['CS-101', '1', 'Fall', '2009', 'Packard', '101', 'H'])
db.insert('section', ['CS-101', '1', 'Spring', '2010', 'Packard', '101', 'F'])
db.insert('section', ['CS-190', '1', 'Spring', '2009', 'Taylor', '3128', 'E'])
db.insert('section', ['CS-190', '2', 'Spring', '2009', 'Taylor', '3128', 'A'])
db.insert('section', ['CS-315', '1', 'Spring', '2010', 'Watson', '120', 'D'])
db.insert('section', ['CS-319', '1', 'Spring', '2010', 'Watson', '100', 'B'])
db.insert('section', ['CS-319', '2', 'Spring', '2010', 'Taylor', '3128', 'C'])
db.insert('section', ['CS-347', '1', 'Fall', '2009', 'Taylor', '3128', 'A'])
db.insert('section', ['EE-181', '1', 'Spring', '2009', 'Taylor', '3128', 'C'])
db.insert('section', ['FIN-201', '1', 'Spring', '2010', 'Packard', '101', 'B'])
db.insert('section', ['HIS-351', '1', 'Spring', '2010', 'Painter', '514', 'C'])
db.insert('section', ['MU-199', '1', 'Spring', '2010', 'Packard', '101', 'D'])
db.insert('section', ['PHY-101', '1', 'Fall', '2009', 'Watson', '100', 'A'])
db.insert('teaches', ['10101', 'CS-101', '1', 'Fall', '2009'])
db.insert('teaches', ['10101', 'CS-315', '1', 'Spring', '2010'])
db.insert('teaches', ['10101', 'CS-347', '1', 'Fall', '2009'])
db.insert('teaches', ['12121', 'FIN-201', '1', 'Spring', '2010'])
db.insert('teaches', ['15151', 'MU-199', '1', 'Spring', '2010'])
db.insert('teaches', ['22222', 'PHY-101', '1', 'Fall', '2009'])
db.insert('teaches', ['32343', 'HIS-351', '1', 'Spring', '2010'])
db.insert('teaches', ['45565', 'CS-101', '1', 'Spring', '2010'])
db.insert('teaches', ['45565', 'CS-319', '1', 'Spring', '2010'])
db.insert('teaches', ['76766', 'BIO-101', '1', 'Summer', '2009'])
db.insert('teaches', ['76766', 'BIO-301', '1', 'Summer', '2010'])
db.insert('teaches', ['83821', 'CS-190', '1', 'Spring', '2009'])
db.insert('teaches', ['83821', 'CS-190', '2', 'Spring', '2009'])
db.insert('teaches', ['83821', 'CS-319', '2', 'Spring', '2010'])
db.insert('teaches', ['98345', 'EE-181', '1', 'Spring', '2009'])
db.insert('student', ['00128', 'Zhang', 'Comp. Sci.', '102'])
db.insert('student', ['12345', 'Shankar', 'Comp. Sci.', '32'])
db.insert('student', ['19991', 'Brandt', 'History', '80'])
db.insert('student', ['23121', 'Chavez', 'Finance', '110'])
db.insert('student', ['44553', 'Peltier', 'Physics', '56'])
db.insert('student', ['45678', 'Levy', 'Physics', '46'])
db.insert('student', ['54321', 'Williams', 'Comp. Sci.', '54'])
db.insert('student', ['55739', 'Sanchez', 'Music', '38'])
db.insert('student', ['70557', 'Snow', 'Physics', '0'])
db.insert('student', ['76543', 'Brown', 'Comp. Sci.', '58'])
db.insert('student', ['76653', 'Aoi', 'Elec. Eng.', '60'])
db.insert('student', ['98765', 'Bourikas', 'Elec. Eng.', '98'])
db.insert('student', ['98988', 'Tanaka', 'Biology', '120'])
db.insert('takes', ['00128', 'CS-101', '1', 'Fall', '2009', 'A'])
db.insert('takes', ['00128', 'CS-347', '1', 'Fall', '2009', 'A-'])
db.insert('takes', ['12345', 'CS-101', '1', 'Fall', '2009', 'C'])
db.insert('takes', ['12345', 'CS-190', '2', 'Spring', '2009', 'A'])
db.insert('takes', ['12345', 'CS-315', '1', 'Spring', '2010', 'A'])
db.insert('takes', ['12345', 'CS-347', '1', 'Fall', '2009', 'A'])
db.insert('takes', ['19991', 'HIS-351', '1', 'Spring', '2010', 'B'])
db.insert('takes', ['23121', 'FIN-201', '1', 'Spring', '2010', 'C+'])
db.insert('takes', ['44553', 'PHY-101', '1', 'Fall', '2009', 'B-'])
db.insert('takes', ['45678', 'CS-101', '1', 'Fall', '2009', 'F'])
db.insert('takes', ['45678', 'CS-101', '1', 'Spring', '2010', 'B+'])
db.insert('takes', ['45678', 'CS-319', '1', 'Spring', '2010', 'B'])
db.insert('takes', ['54321', 'CS-101', '1', 'Fall', '2009', 'A-'])
db.insert('takes', ['54321', 'CS-190', '2', 'Spring', '2009', 'B+'])
db.insert('takes', ['55739', 'MU-199', '1', 'Spring', '2010', 'A-'])
db.insert('takes', ['76543', 'CS-101', '1', 'Fall', '2009', 'A'])
db.insert('takes', ['76543', 'CS-319', '2', 'Spring', '2010', 'A'])
db.insert('takes', ['76653', 'EE-181', '1', 'Spring', '2009', 'C'])
db.insert('takes', ['98765', 'CS-101', '1', 'Fall', '2009', 'C-'])
db.insert('takes', ['98765', 'CS-315', '1', 'Spring', '2010', 'B'])
db.insert('takes', ['98988', 'BIO-101', '1', 'Summer', '2009', 'A'])
db.insert('takes', ['98988', 'BIO-301', '1', 'Summer', '2010', None])
db.insert('advisor', ['00128', '45565'])
db.insert('advisor', ['12345', '10101'])
db.insert('advisor', ['23121', '76543'])
db.insert('advisor', ['44553', '22222'])
db.insert('advisor', ['45678', '22222'])
db.insert('advisor', ['76543', '45565'])
db.insert('advisor', ['76653', '98345'])
db.insert('advisor', ['98765', '98345'])
db.insert('advisor', ['98988', '76766'])
db.insert('time_slot', ['A', 'M', '8', '0', '8', '50'])
db.insert('time_slot', ['A', 'W', '8', '0', '8', '50'])
db.insert('time_slot', ['A', 'F', '8', '0', '8', '50'])
db.insert('time_slot', ['B', 'M', '9', '0', '9', '50'])
db.insert('time_slot', ['B', 'W', '9', '0', '9', '50'])
db.insert('time_slot', ['B', 'F', '9', '0', '9', '50'])
db.insert('time_slot', ['C', 'M', '11', '0', '11', '50'])
db.insert('time_slot', ['C', 'W', '11', '0', '11', '50'])
db.insert('time_slot', ['C', 'F', '11', '0', '11', '50'])
db.insert('time_slot', ['D', 'M', '13', '0', '13', '50'])
db.insert('time_slot', ['D', 'W', '13', '0', '13', '50'])
db.insert('time_slot', ['D', 'F', '13', '0', '13', '50'])
db.insert('time_slot', ['E', 'T', '10', '30', '11', '45 '])
db.insert('time_slot', ['E', 'R', '10', '30', '11', '45 '])
db.insert('time_slot', ['F', 'T', '14', '30', '15', '45 '])
db.insert('time_slot', ['F', 'R', '14', '30', '15', '45 '])
db.insert('time_slot', ['G', 'M', '16', '0', '16', '50'])
db.insert('time_slot', ['G', 'W', '16', '0', '16', '50'])
db.insert('time_slot', ['G', 'F', '16', '0', '16', '50'])
db.insert('time_slot', ['H', 'W', '10', '0', '12', '30'])
db.insert('prereq', ['BIO-301', 'BIO-101'])
db.insert('prereq', ['BIO-399', 'BIO-101'])
db.insert('prereq', ['CS-190', 'CS-101'])
db.insert('prereq', ['CS-315', 'CS-101'])
db.insert('prereq', ['CS-319', 'CS-101'])
db.insert('prereq', ['CS-347', 'CS-101'])
db.insert('prereq', ['EE-181', 'PHY-101'])

print("1 -> exclusive table lock example")
print("2 -> exclusive row lock example")
print("3 -> shared table lock example")
print("4 -> shared row lock example")
print("5 -> multiple row locks example")
print("anything else to exit")

while True:
    print("1 -> exclusive table lock example")
    print("2 -> exclusive row lock example")
    print("3 -> shared table lock example")
    print("4 -> shared row lock example")
    print("5 -> multiple row locks example")
    print("anything else to exit")
    ex = input()
    if ex == '1':
        db.show_table('meta_locks')
        print("locking X table student")
        db.lockX_table('student')
        sleep(5)
        db.show_table('meta_locks')
        sleep(5)
        print("Trying to do the Select operation")
        db.select('student', '*', 'dept_name==History')
        sleep(5)
        print("unlocking the table but with wront parameters(unlockS) and trying Select ")
        db.unlock_table('student', 'shared')
        sleep(5)
        print("unlocking the table  and trying Select again")
        db.unlock_table('student', 'exclusive')
        db.show_table('meta_locks')
        sleep(5)
        db.select('student','*' , 'dept_name==History')
    elif ex == '2':
        db.show_table('meta_locks')
        print("locking X the third entry with of the table student")
        db.lockX_row('student', 3)
        sleep(5)
        db.show_table('meta_locks')
        sleep(5)
        print("Trying to do the Select")
        db.select('student', '*', 'dept_name==History')
        sleep(5)
        print("Trying to do the Delete")
        db.delete('student', 'dept_name==History')
        sleep(5)
        print("Unlocking the 3rd row but with unlock_row(S)")
        db.unlock_row('student', 'shared', 3)
        db.show_table('meta_locks')
        sleep(5)
        print("Unlocking the 3rd row  with the right unlock parameters..")
        db.unlock_row('student', 'exclusive', 3)
        db.show_table('meta_locks')
        sleep(5)
        print("Trying Delete once again")
        sleep(2)
        db.delete('student', 'dept_name==History')
    elif ex == '3':
        db.show_table('meta_locks')
        print("locking S table student")
        db.lockS_table('student')
        sleep(5)
        db.show_table('meta_locks')
        sleep(5)
        print("Trying to do the Delete operation")
        db.delete('student', 'dept_name==History')
        sleep(5)
        print("unlocking the table but with wront parameters(unlockX) and trying Delete ")
        print("")
        sleep(2)
        db.unlock_table('student', 'exclusive')
        db.delete('student', 'dept_name==History')
        sleep(5)
        print("")
        print("Trying to do the Select")
        print("")
        sleep(2)
        db.select('student', '*', 'dept_name==History')
        sleep(3)
        print("Select doesn't care if shared locks exist in the table..")
        sleep(4)
        print("")
        print("unlocking the table  and trying Delete again")
        print("")
        db.unlock_table('student', 'shared')
        db.show_table('meta_locks')
        sleep(5)
        db.delete('student', 'dept_name==History')
        sleep(5)
        print("Now we will see that multiple shared locks in the table can coexist")
        sleep(3)
        db.lockS_table('student')
        db.show_table('meta_locks')
        sleep(2)
        db.lockS_table('student')
        db.show_table('meta_locks')
        sleep(2)
        db.lockS_table('student')
        db.show_table('meta_locks')
        sleep(4)
        print("Now trying to dismiss all the locks")
        sleep(3)
        db.unlock_table('student', 'shared')
        db.show_table('meta_locks')
        sleep(3)
        db.unlock_table('student', 'shared')
        db.show_table('meta_locks')
        sleep(3)
        db.unlock_table('student', 'shared')
        db.show_table('meta_locks')
        sleep(3)
        print("No more shared locks exist on the table 'student'. What if we try to unlock once again?")
        sleep(5)
        print("")
        db.unlock_table('student', 'shared')
        db.show_table('meta_locks')
    elif ex == 4:
        db.show_table('meta_locks')
        print("lockS the 5th row of student")
        db.lockS_row('student', 5)
        sleep(5)
        db.show_table('meta_locks')
        sleep(5)
        print("Trying to do the Delete operation")
        db.delete('student', 'dept_name==History')
        sleep(5)
        print("unlocking the row but with wront parameters(unlockX) and trying Delete ")
        print("")
        sleep(2)
        db.unlock_row('student', 'exclusive', 5)
        db.delete('student', 'dept_name==History')
        sleep(5)
        print("")
        print("Trying to do the Select")
        print("")
        sleep(2)
        db.select('student', '*', 'dept_name==History')
        sleep(3)
        print("Select doesn't care if shared locks exist in the table or the rows of the table..")
        sleep(4)
        print("")
        print("unlocking the row  and trying Delete again")
        print("")
        db.unlock_row('student', 'shared', 5)
        db.show_table('meta_locks')
        sleep(5)
        db.delete('student', 'dept_name==History')
        sleep(5)
        print("Now we will see that multiple shared locks in the row can coexist")
        sleep(3)
        db.lockS_row('student', 5)
        db.show_table('meta_locks')
        sleep(2)
        db.lockS_row('student', 5)
        db.show_table('meta_locks')
        sleep(2)
        db.lockS_row('student', 5)
        db.show_table('meta_locks')
        sleep(4)
        print("Now trying to dismiss all the locks")
        sleep(3)
        db.unlock_row('student', 'shared', 5)
        db.show_table('meta_locks')
        sleep(3)
        db.unlock_row('student', 'shared', 5)
        db.show_table('meta_locks')
        sleep(3)
        db.unlock_row('student', 'shared', 5)
        db.show_table('meta_locks')
        sleep(3)
        print("No more shared locks exist on the row of the table 'student'. What if we try to unlock once again?")
        sleep(5)
        print("")
        db.unlock_row('student', 'shared', 5)
        db.show_table('meta_locks')
    elif ex == '5':
        print("Showing the capabilities of the dictionary as a data structure for the row locks.")
        print("Trying lockS at student row 5 and lockX student row 6")
        sleep(5)
        db.lockS_row('student', 5)
        db.lockX_row('student', 6)
        db.show_table('meta_locks')
        sleep(2)
        print("Trying lockS at student row 5 and lockX student row 6")
        sleep(5)
        db.lockS_row('student', 5)
        db.lockX_row('student', 1)
        db.show_table('meta_locks')
        sleep(2)
        print("Trying lockS at student row 6 and lockX student row 8")
        sleep(5)
        db.lockS_row('student', 6)
        db.lockX_row('student', 8)
        db.show_table('meta_locks')
        sleep(2)
        print("Trying lockS at student row 5 and lockX student row 2")
        sleep(5)
        db.lockS_row('student', 5)
        db.lockX_row('student', 2)
        db.show_table('meta_locks')
        sleep(2)
        print("Trying lockS at student row 17 and lockX student row 17")
        sleep(5)
        db.lockS_row('student', 17)
        db.lockX_row('student', 17)
        db.show_table('meta_locks')
        sleep(2)
        print("Trying lockX at student row 52 and lockS student row 52")
        sleep(5)
        db.lockX_row('student', 52)
        db.lockS_row('student', 52)
        db.show_table('meta_locks')
        sleep(2)
        print("Trying lockS at student row 5 and lockX student row 15")
        sleep(5)
        db.lockS_row('student', 5)
        db.lockX_row('student', 15)
        db.show_table('meta_locks')
        sleep(2)
        print('some random row locks on table "instructor" ')
        sleep(5)
        db.lockS_row('instructor', 3)
        db.lockX_row('instructor', 2)
        db.show_table('meta_locks')
        sleep(5)
        db.lockS_row('instructor', 7)
        db.lockX_row('instructor', 6)
        db.show_table('meta_locks')
        sleep(5)
        db.lockS_row('instructor', 6)
        db.lockX_row('instructor', 9)
        db.show_table('meta_locks')
        sleep(5)
        db.lockS_row('instructor', 7)
        db.lockX_row('instructor', 8)
        db.show_table('meta_locks')
        sleep(5)
        db.lockS_row('instructor', 7)
        db.lockX_row('instructor', 17)
        db.show_table('meta_locks')
        sleep(5)
        db.lockS_row('instructor', 17)
        db.lockX_row('instructor', 2)
        db.show_table('meta_locks')
        sleep(5)
        db.lockS_row('instructor', 22)
        db.lockX_row('instructor', 1)
        db.show_table('meta_locks')
    else:
        break
