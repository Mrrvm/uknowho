import smtplib

def send_email(to_email, username, my_email, title):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("uknowho.geral@gmail.com", "tuamaede4")

    message = "Hi, the user " + username + " wants to help you on your Project!\n You may contact him by the address " + my_email
    #msg = "this is a simple message sent from uknowho"
    server.sendmail("uknowho.geral@gmail.com", to_email, message)
    server.quit()