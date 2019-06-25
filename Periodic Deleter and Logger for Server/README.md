
<h2>---Periodic Duplicate File Remover and logger with Email extension---</h2>

<h4>What does this Project do?</h4><br>
1. This Project Scans a particular directory after predefined time interval.<br>
2. If any duplicate files exists then it deleted them.<br>
3. Then it logs them into a .txt file.<br>
4. Then it emails the log to a predefined email id.<br>

<h4>Usage</h4><br>
Appname Directory_Name time_period to_Email_ID <br>
1. Appname- is the Driver python file.<br>
2. Directory_Name - the directory to scan periodically.<br>
3. to_Email_ID- The email id to send the log to.<br>

<h4>1. Edit the password Field and Username field in the code near Line 77 in MyModule.py to be able to send the email from your email id.<br>
  2. You need schedule library in python for this code to work. Schedule library is'nt present in Python libraries by default.<br>
