import smtplib
import getpass
myemail="nazish.hussain51@gmail.com"
password=getpass.getpass()
recemai = "vidya4821@gmial.com"
# creats SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

#start TLS for security
s.starttls()

#AUTHENTICATION
s.login(myemail, password)

#message to be sent
message = "how are you"

#sending the mail 
s.sendmail("nazish.hussain51@gmail.com","vidya4821@gmail.com",message)

#terminating the session
s.quit()


#!home/user/anaconda3/bin/python3`