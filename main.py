import smtplib
from email import msg

msg = msg()
msg['Subject'] = 'Welcome message'
msg['From'] = 'Test'
msg['To'] = 'thotakuri@rediff.com'
msg.set_content("Test email")

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("thotakurisrinivas@gmail.com", "")
server.send_message(msg)
server.quit()
