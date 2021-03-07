import poplib
import pyperclip

pop3server = 'mail.bilkent.edu.tr'
username = 'name.surname@ug.bilkent.edu.tr'
password = 'password'
pop3server = poplib.POP3_SSL(pop3server, port=995)

pop3server.user(username)
pop3server.pass_(password)
pop3info = pop3server.stat() 
mailcount = pop3info[0] 

x = []
x = pop3server.retr(mailcount)[1]

q = x[-2]
q = q.decode("utf-8")       
x = q.find("Code: ")
q = q[x+6:x+11]
print(q)

pop3server.quit()

pyperclip.copy(q)
spam = pyperclip.paste()

#input()


