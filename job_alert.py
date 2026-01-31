import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

EMAIL_FROM = os.environ.get("EMAIL_FROM")
EMAIL_TO = os.environ.get("EMAIL_TO")
APP_PASSWORD = os.environ.get("APP_PASSWORD")

EXCLUDE_COMPANY = [
    "asus","華碩","pegatron","和碩","askey",
    "asmedia","祥碩","lanner","立端","瑞傳","portwell"
]

JOBS = [
    ("LinkedIn","ABC GmbH","ESG Manager","Taipei","https://linkedin.com"),
    ("104","EuroSystems Taiwan","永續專案管理師","台北","https://104.com.tw"),
]

def send_email():
    msg = MIMEMultipart()
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = f"【ESG 職缺整理】{datetime.today().strftime('%Y-%m-%d')}"

    body = "本週 ESG / 永續 / 環境法規相關職缺：\n\n"
    for p,c,t,l,link in JOBS:
        if not any(e.lower() in c.lower() for e in EXCLUDE_COMPANY):
            body += f"- [{p}] {c}｜{t}｜{l}\n  {link}\n\n"

    msg.attach(MIMEText(body, "plain", "utf-8"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_FROM, APP_PASSWORD)
        server.send_message(msg)

send_email()

