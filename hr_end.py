import sqlite3

db = sqlite3.connect('tb_aspirants.db')
crsr = db.cursor()
crsr.execute('select * from tb_aspirants')
alldata=crsr.fetchall()
# (8217279272, 'KANISHKA', 'KIRANKIRUKANISHKA@GMAIL.COM', 'PUNE', 'DIPLOMA', 65, None, 0, 'C,JAVA', 'Resumes/8217279272.pdf')


def displayDetails(asps):
    print('--------------------------------------------------')
    # for aspLst in asps:
    #     for aspDtls in aspLst:
    #         print(aspDtls)
    #     print('--------------------------------------------------')
    for aspLst in asps:
        print(
            f'Name: {aspLst[1]}          Mobile Num: {aspLst[0]}       Mail ID: {aspLst[2]}           Location: {aspLst[3]}')
        print(f'Highest Education: {aspLst[4]}        Percentage: {aspLst[5]}')
        if aspLst[7] > 0:
            print(f'Previous Job Role: {aspLst[6]}        Experience: {aspLst[7]} year(s)')
        print(f'Skill set: {aspLst[8]}')
        print(f'Resume: {aspLst[9]}')
        print('--------------------------------------------------')

def searchAsp():
    tempnum=input("1. Search by Mobile Number\n2. Search by mail id\n")
    if tempnum=='1':
        mobNum = int(input('Enter the Aspirant Mobile Number: '))
        crsr.execute("select * from tb_aspirants where MOB_NUM = :mobNum",{'mobNum':mobNum})
        aspDetails = crsr.fetchall()
        displayDetails(aspDetails)
    elif tempnum=='2':
        mailId = input('Enter the Aspirant Mail Id: ').upper()
        crsr.execute('select * from tb_aspirants where MAIL_ID = :mailid', {'mailid': mailId})
        aspDetails = crsr.fetchall()
        displayDetails(aspDetails)
        # displayDetails(crsr.fetchone())

def searchJob():
    tempnum=input('1. Search for fresher profiles\n2. Search for experienced profiles\n')
    if tempnum=='1':
        education = input('1. Diploma Holders\n2. Graduates\n3. Post Graduates\n')
        if education=='1':
            crsr.execute('select * from tb_aspirants where EXPERIENCE=0 and HIGHEST_EDU="DIPLOMA"')
            aspDetails = crsr.fetchall()
            displayDetails(aspDetails)

        elif education=='2':
            crsr.execute('select * from tb_aspirants where EXPERIENCE=0 and HIGHEST_EDU="GRADUATION"')
            aspDetails = crsr.fetchall()
            displayDetails(aspDetails)
        elif education=='3':
            crsr.execute('select * from tb_aspirants where EXPERIENCE=0 and HIGHEST_EDU="POST GRADUATION"')
            aspDetails = crsr.fetchall()
            displayDetails(aspDetails)

    elif tempnum=='2':
        skill = input('Enter the Skill required by the aspirant: ').upper()
        for asp in alldata:
            if skill in asp[8] and asp[7]>0:
                crsr.execute('select * from tb_aspirants where MOB_NUM = :mobNum',{'mobNum':asp[0]})
                aspDetails = crsr.fetchall()
                displayDetails(aspDetails)

choice=input('Select the action:\n1. View an aspirant details\n2. Search aspirants as per requirement\n')
if choice=='1':
    searchAsp()
elif choice=='2':
    searchJob()


