import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Настройки отправителя
smtp_server = "smtp.gmail.com"  # SMTP сервер (например, Gmail)
smtp_port = 587  # Порт SMTP
email_user = "your_email@gmail.com"  # Ваш email
email_password = "your_password"  # Пароль или app password от email

# Настройки получателя
to_email = "recipient_email@example.com"  # Email получателя

# Создание сообщения
subject = "Отправка двух Word-файлов и текста"
body = "Здравствуйте! Во вложении вы найдете два Word-файла.\nСпасибо!"

msg = MIMEMultipart()
msg["From"] = email_user
msg["To"] = to_email
msg["Subject"] = subject

    # Добавляем текст в тело письма
msg.attach(MIMEText(body, "plain"))

# Функция для добавления файла
def attach_file(filename):
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={filename}",
        )
        msg.attach(part)

# Прикрепляем два Word-файла
attach_file("file1.docx")  # Замените на путь к первому Word-файлу
attach_file("file2.docx")  # Замените на путь ко второму Word-файлу

# Подключение к серверу и отправка письма
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Начало шифрованного соединения
    server.login(email_user, email_password)
    server.sendmail(email_user, to_email, msg.as_string())
    print("Письмо успешно отправлено!")
except Exception as e:
    print(f"Ошибка при отправке письма: {e}")
finally:
    server.quit()
