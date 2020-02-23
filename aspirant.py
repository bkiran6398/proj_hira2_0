import sqlite3
db = sqlite3.connect('tb_aspirants.db')
crsr = db.cursor()

# crsr.execute(""" create table tb_aspirants(
#                  MOB_NUM INTEGER NOT NULL PRIMARY KEY, NAME TEXT, MAIL_ID TEXT,LOCATION,
#                  HIGHEST_EDU TEXT, GRADE INTEGER,PREV_JOB TEXT,EXPERIENCE INTEGER DEFAULT 0,TECH_SKILLS TEXT,RESUME TEXT) """)
# db.commit()
#
# crsr.execute("Delete from tb_aspirants")
# db.commit()
crsr.execute('Select * from tb_aspirants')
print(crsr.fetchall())
# print('aspirant class')

class Aspirant:

    def __init__(self,mobnum,new=True):
        self.mobnum=mobnum
        if new==True:
            crsr.execute("insert into tb_aspirants(MOB_NUM) values(:mobnum)",{'mobnum':self.mobnum})
        db.commit()

    jobRole=None
    exp=0
    dstLoc=''

    def takeContactInfo(self):
        self.name = input('Enter your Full Name: ').upper()
        self.mailid = input('Enter your Mail id: ').upper()
        self.location = input('Enter your City name: ').upper()


    def takeEducationInfo(self):

        while True:
            try:
                tempNum = input('select your highest education:\n1.Diploma\n2.Graduation\n3.Post Graduation\n')
                tempDict = {'1': 'Diploma', '2': 'Graduation', '3': 'Post Graduation'}
                self.highestEdu= tempDict.get(tempNum).upper()
                break
            except AttributeError:
                print('Please select a valid option')
        while True:
            try:
                self.grade=round(float(input('Enter your Percentage: ')))
                break
            except ValueError:
                print('Please Enter a valid Percentage')


    def takeProfessionalInfo(self):
        self.jobRole=input('Enter the Previous job role: ').upper()
        while True:
            try:
                self.exp=int(input('Enter the total number of years experienced: '))
                break
            except ValueError:
                print('Please enter the total number of Experience in digits')

        db.commit()

    def takeTechSkills(self):
        self.prgskls=input('Enter the programming skills known(Seperated by comma)\n').upper()


    def takeResume(self):
        print('Please upload your Resume in pdf format')
        while True:
            try:
                srcLoc = input('Enter the Resume file path: ')
                lst = []
                for char in srcLoc:
                    if char != "\\":
                        lst.append(char)
                    else:
                        lst.append('/')

                srcLoc = str(''.join(lst[1:-1]))
                print(srcLoc)
                resSrc = open(srcLoc, 'rb')
                self.dstLoc = '' + 'Resumes/' + str(self.mobnum) + '.pdf'
                resDst = open(self.dstLoc, 'wb')
                for i in resSrc:
                    resDst.write(i)
                resSrc.close()
                resDst.close()
                break
            except FileNotFoundError:
                print('Select a valid resume(.pdf) file path')

        crsr.execute("""update tb_aspirants set name=:name,mail_id= :mailid,location=:loc,HIGHEST_EDU = :highestEdu,GRADE = :grade,PREV_JOB = :jobRole,
                        EXPERIENCE = :exp,TECH_SKILLS = :techSkls,RESUME = :resume where MOB_NUM= :mobnum""",
                     {'name': self.name, 'mailid': self.mailid, 'loc': self.location, 'highestEdu': self.highestEdu,
                      'grade': self.grade,'jobRole': self.jobRole, 'exp': self.exp, 'techSkls': self.prgskls, 'resume': self.dstLoc,'mobnum': self.mobnum})
        db.commit()





