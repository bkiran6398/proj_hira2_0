from aspirant import Aspirant
import sqlite3

#initialize database
db = sqlite3.connect('tb_aspirants.db')
crsr = db.cursor()

def takeDetails(asp1):
    """method to call all the other methods to take details of the aspirant"""
    asp1.takeContactInfo()
    asp1.takeEducationInfo()
    asp1.takeTechSkills()
    tempNum = input('Are you fresher or Experienced:\n1.Fresher\n2.Experienced\n')
    if tempNum == '2':
        asp1.takeProfessionalInfo()
    asp1.takeResume()
    print('Thank you for your info, one of our representatives will contact you soon.')

def displayDetails(asps):
    """To display the details of aspirant in a structured format"""
    print('--------------------------------------------------')
    for aspLst in asps:
        print(
            f'Name: {aspLst[1]}          Mobile Num: {aspLst[0]}       Mail ID: {aspLst[2]}           Location: {aspLst[3]}')
        print(f'Highest Education: {aspLst[4]}        Percentage: {aspLst[5]}')
        if aspLst[7] > 0:
            print(f'Previous Job Role: {aspLst[6]}        Experience: {aspLst[7]} year(s)')
        print(f'Skill set: {aspLst[8]}')
        print(f'Resume: {aspLst[9]}')
        print('--------------------------------------------------')

print('Welcome...')
print('Please fill the following details to apply for the job')
while True:
    #try-except is used to make sure a int value is entered
    try:
        mobnum = int(input('Enter your 10 digit Mobile number: '))
        break
    except ValueError:
        print('Please Enter a valid 10 digit Mobile number')

asp=None
try:
    asp= Aspirant(mobnum)
    takeDetails(asp)
except sqlite3.IntegrityError:
    crsr.execute('select * from tb_aspirants where mob_num = :mobnum', {'mobnum': mobnum})
    asps = crsr.fetchall()
    displayDetails(asps)
    choice = input('User already exist... Would you like to update your details? Yes/No:').upper()
    if choice == 'YES':
        asp = Aspirant(mobnum,False)
        takeDetails(asp)




