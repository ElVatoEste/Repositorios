import smtplib 

message = "Jajaja te envie un mensaje desde un codigo que hice uwu"
subject = "Probando"

message= "Subject: {}\n\n{}".format(subject, message)
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

User =  None # [Aqui poner la dirrecion de correo]
Password = None # [Aqui poner la contraseña del correo]

server.login(User, Password)

# server.sendmail(Remitente , Destinario, message)

server.quit()

