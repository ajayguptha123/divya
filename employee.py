import pyttsx3
import urllib
import pymongo as mg
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def employee_entry():
    engine = pyttsx3.init()
    engine.say("enter your employee id")
    engine.runAndWait()
    engine = pyttsx3.init()
    emp_id=input("enter empid :")
    engine.runAndWait()
    engine = pyttsx3.init()
    engine.say("enter your name")
    engine.runAndWait()
    emp_name=input("enter your name:")
    engine = pyttsx3.init()
    engine.say("enter your Email id")
    engine.runAndWait()
    Email_id=input("enter your Email id:")
    
    db=db_connect()
    emp = db.employee
    emp_count=emp.find({"emp_id":emp_id}).count()
    if emp_count ==0:
        employee={"emp_id":emp_id,
                  "name":emp_name,
                  "Email_id":Email_id,
                        }
        result=emp.insert_one(employee)
        if result.acknowledged:
            print("your details entered")
    else:
        print("your details are already in database")
        
    return emp_id,emp_name
        
    '''
    with open('emp.json','r') as emp:
        emp1=json.load(emp)
    
    employee={dirc:emp_name}
    
    emp1.update(employee)
    
    with open('emp.json','w') as emp2:
        json.dump(emp1,emp2)
    '''
    
def dir_create(dirc):
    path="B:\\face_recognition\\CNN_project\\train_img\\"+dirc
    # Create target Directory if don't exist
    if not os.path.exists(path):
        os.mkdir(path)
        engine = pyttsx3.init()
        engine.say("your directory is created. Iam taking your images.")
        engine.runAndWait()
        print("Directory " , dirc ,  " Created ")
    else:    
        print("Directory " , dirc ,  " already exists")
        engine = pyttsx3.init()
        engine.say("your directory is already created.No need to create again.")
        engine.runAndWait()
    return path

def db_connect():
    username = urllib.parse.quote_plus('hanmanthreddy')
    password = urllib.parse.quote_plus('hanu@1221')
    mongodb_URL="mongodb://%s:%s@ds115595.mlab.com:15595/facerecognizer"% (username, password)
    client=mg.MongoClient(mongodb_URL,connectTimeoutMS=30000)
    db=client.get_default_database()
    return db

def emailToEmp(Tomail,mssg):
    msg = MIMEMultipart()
    msg.set_unixfrom('author')
    msg['From'] = 'noreply-promotions@fnibot.com'
    msg['To'] = Tomail
    msg['Subject'] = 'Attendence of Foodni'
    message = mssg
    msg.attach(MIMEText(message))
    
    mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
    mailserver.ehlo()
    mailserver.login('noreply-promotions@fnibot.com', 'Fnic@7916')
    
    mailserver.sendmail('noreply-promotions@fnibot.com',Tomail,msg.as_string())
    
    mailserver.quit()