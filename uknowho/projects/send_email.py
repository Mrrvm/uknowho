import smtplib

def send_email(to_email, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("uknowho.geral@gmail.com", "tuamaede4")

    #msg = "this is a simple message sent from uknowho"
    server.sendmail("uknowho.geral@gmail.com", to_email, message)
    server.quit()