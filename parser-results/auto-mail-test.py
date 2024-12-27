import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

smtp_server = "smtp.gmail.com"
smtp_port = 587
a = int(input('важные-1\nне важные-2\n'))
if a == 1:
    email_user = "Redstonefirstkz@gmail.com"
    email_password = "qucm tdvl fnax eqbs "
elif a == 2:
    email_user = "redstoneftc@gmail.com"
    email_password = "mssj otuu xtoi vbzb "

subject = "Тестовое сообщение"
body = "Здравствуйте! Во вложении вы найдете два Word-файла.\nСпасибо!"
email_file = "pars-mail-test.txt"  # Путь к файлу с email-адресами

if not os.path.exists(email_file):
    print(f"Файл '{email_file}' не найден. Проверьте путь.")
    exit()


def attach_file(msg, filename):
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={filename}")
        msg.attach(part)

with open(email_file, "r", encoding="utf-8") as file:
    email_list = file.read().splitlines()

for recipient in email_list:
    msg = MIMEMultipart()
    msg["From"] = email_user
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    attach_file(msg, "rus.pdf")
    attach_file(msg, "eng.pdf")

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_user, email_password)
        server.sendmail(email_user, recipient, msg.as_string())
        print(f"Письмо успешно отправлено: {recipient}")
    except Exception as e:
        print(f"Ошибка при отправке письма на {recipient}: {e}")
    finally:
        server.quit()
