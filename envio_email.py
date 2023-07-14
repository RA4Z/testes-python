from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()
texto = 'Estou enviado isto com Python'
senha = '1qasw23ed'
msg['From'] = 'rraz639@gmail.com'
msg['To'] = 'robertn@weg.net'
msg['Subject'] = 'Teste de E-mail com Python'

msg.attach(MIMEText(texto, 'plain'))

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

server.login(msg['From'], senha)

server.sendmail((msg['From'], msg['To']),
msg.as_string())

server.quit()

print('Mensagem enviada com sucesso!')

