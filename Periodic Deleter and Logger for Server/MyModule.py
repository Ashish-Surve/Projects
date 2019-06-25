import sys
import os
import HashingModule as hm
import psutil
from urllib.request import urlopen
import datetime
import traceback


def addtolog(filep,fd):
    #fd=open("LOG.txt",encoding="utf-8" ,mode="a")
    fd.write(filep+"\n")

def directory(path):
    scanned_files_count=0
    starting_time_scanning=datetime.datetime.now()
    no_dup_files=0
    flag=os.path.isabs(path)

    if flag==False:
        path=os.path.abspath(path)

    hash_dict=dict()
    newpath="LogDirectory"
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    logfilepath=os.path.abspath(os.path.join(newpath,"Logger"+str(datetime.datetime.now())+".txt"))

    fd=open(logfilepath,encoding="utf-8" ,mode="w")

    exists=os.path.isdir(path)
    fd.write("Address of all files which have been deleted is here.\nBy- Ashish Surve \n\n\n\n")
    if exists:
        for foldername,subfolder,filename in os.walk(path):
            #print("Current folder is: "+foldername)
            for filen in filename:
                filen=os.path.join(foldername,filen)
                hash=hm.md5(filen)
                scanned_files_count+=1
                #print(filen)
                if hash in hash_dict:
                    addtolog(filen,fd)
                    os.remove(filen)
                    no_dup_files+=1                      
                else:
                    hash_dict.update({hash:filen})                   
    else:
        print("Invalid Path")
    fd.close
    return logfilepath,starting_time_scanning,scanned_files_count,no_dup_files



def is_connected():
    try:
        urlopen("http://216.58.192.142",timeout=2)
        return True
    except:
        return False    

def sendemail(filep,to,start_time,scan_file_count,dup_file_count):
    import email, smtplib, ssl
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    subject = "Process Log from Andromeda"
    body = ("""Logging provided Ashish Surve\n"""
            """Starting time of scanning: """+str(start_time)
            +"\nNumber of files scanned: """+str(scan_file_count)
            +"\nNumber of Duplicate Files: "+str(dup_file_count)+"\n")    
        
    sender_email = "something@gmail.com"
    receiver_email = to
    password = input("Type your password and press enter:")
    #Edit the above line with email id and password.
    
    try:
      # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
       

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        filename = filep  # In same directory as script

        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)
        filename=os.path.basename(filename)
        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
        server.close()
        return True
    except Exception :
        print("Error: While Sending Email...")
        print(traceback.format_exc())
        return False
