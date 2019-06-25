import sys
import os
import HashingModule as hm
import MyModule as mm
import traceback
import time
import schedule

hash_dict=dict()

def go():
    try:
        path=sys.argv[1]
        #print(path)
        toemail=sys.argv[3]
        #print(toemail)
        logfilepath,start_time,scanned_files,dup_files=mm.directory(path)
        check=mm.sendemail(logfilepath,toemail,start_time,scanned_files,dup_files)
        if(check):
            print("Email Sent to "+toemail+ "with attachement file "+logfilepath)
        else:
            print("email sending error")
            exit()    


    except Exception:
        print("Exception")
        print(traceback.format_exc())

    
def main():
    print("---Periodic Duplicate File Remover and logger with Email extension---")
    print("Application name: {}".format(sys.argv[0]))

    if len(sys.argv)<4 or len(sys.argv)>4:
        print("ERR: Invalid Number of Args")

    if sys.argv[1].lower=="-h":
        print("Script is designed for a lot of things...")
        exit()

    if sys.argv[1].lower=="-u":
        print("Usage: Appname Directory_Name time_period to_Email_ID ")
        exit() 

    if len(sys.argv)!=4:
        print("ERR: Invalid no of Args")
        exit()

    try :
        i=0
        timee=int(sys.argv[2])
        schedule.every(timee).minutes.do(go)
        while True:
            schedule.run_pending()
            time.sleep(1)
            print(i)
            i+=1

    except Exception as e:
        print("ERR: Invalid Input"+str(e))
        print(traceback.format_exc())

if __name__=="__main__":
    main()    

