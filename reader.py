import imaplib
import credentials
from bs4 import BeautifulSoup
import quopri
import pyttsx3
from google_speech import Speech

host = 'imap.gmail.com'
port = 993
user = credentials.user
password = credentials.password
lang = "pt_br"

server = imaplib.IMAP4_SSL(host, port)
server.login(user, password)
server.select('Inbox')

#Capturando os e-mails da NL com status "não lido"
status, data = server.search(None, "(FROM 'newsletter@filipedeschamps.com.br' UNSEEN)")

for num in data[0].split():
    status, data = server.fetch(num, "(RFC822)")
    email_msg = data[0][1]

    soup = BeautifulSoup(markup=email_msg, features='lxml')
    news = soup.find_all('td')[0].text

    utf = quopri.decodestring(news)
    text = utf.decode('utf-8')
    
    # 
    speech = Speech(text, lang)
    sox_effects = ("speed", "1.1")
    speech.play(sox_effects)

server.close()
