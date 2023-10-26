import smtplib

# Calling SMTP
s = smtplib.SMTP('smtp.gmail.com', 587)
# TLS for network security
s.starttls()
# User email Authentication
s.login("festus.hoopa@gmail.com", "uzhtqstbegtfftzr")
# Message to be sent
message = "this was using python"
# Sending the mail
s.sendmail("festus.hoopa@gmail.com", "loulisabu@gmail.com", message)