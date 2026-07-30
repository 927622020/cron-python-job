import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "jeevanantham4213@gmail.com"
sender_password = os.environ["GMAIL_APP_PASSWORD"]

receiver_email = [
    "jeevanantham4213@gmail.com","jeevanantham.r@cavininfotech.com","muthu.g@cavininfotech.com"
]

# Create email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = ", ".join(receiver_email)
message["Subject"] = "Cron Job Status"

body = "Cron job ran successfully."
message.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)

    server.sendmail(
        sender_email,
        receiver_email,
        message.as_string()
    )

    server.quit()
    print("Email sent successfully.")

except Exception as e:
    print(f"Error: {e}")

##################################################################################
##################################################################################

# import mysql.connector
# import smtplib
# from email.mime.text import MIMEText
# from datetime import datetime

# # ---------------- MySQL Configuration ----------------
# # db = mysql.connector.connect(
# #     host="localhost",
# #     user="your_username",
# #     password="your_password",
# #     database="prodmax_assam",
# #     autocommit=True
# # )

# # from datetime import datetime, timedelta


# db = mysql.connector.connect(
#     host= "kpi-drm.mysql.database.azure.com",
#     user= "citpl_kpi",
#     password= "1J50)r2!t~G$",
#     database= "prodmax_assam",
#     autocommit=True

# )



# # ---------------- Email Configuration ----------------
# sender_email = "jeevanantham4213@gmail.com"
# app_password = "smvedtivdhorkoje"

# receiver_emails = [
#     "jeevanantham4213@gmail.com",
#     "jeevanantham.r@cavininfotech.com"
# ]

# try:
#     cursor = db.cursor()

#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     # current_time = (datetime.now() - timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S")
#     # current_time = datetime.now()

#     print(current_time)
#     # Call Stored Procedure
#     cursor.execute("SELECT NOW()")
#     print("DB Time:", cursor.fetchone())
#     print("Python Time:", current_time)

#     cursor.callproc('down_line', [current_time])
#     db.commit()

#     print("SUCCESS: Stored Procedure Executed Successfully",current_time)

#     # ---------------- Send Email ----------------
#     body = f"""
# Stored Procedure Executed Successfully

# Procedure : prodmax_assam.down_line
# Execution Time : {current_time}

# Status : SUCCESS
# """

#     msg = MIMEText(body)
#     msg["Subject"] = "Cron Job Status - SUCCESS"
#     msg["From"] = sender_email
#     msg["To"] = ", ".join(receiver_emails)

#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login(sender_email, app_password)

#     server.sendmail(
#         sender_email,
#         receiver_emails,
#         msg.as_string()
#     )

#     server.quit()

#     print("Email sent successfully.")

#     cursor.close()
#     db.close()

# except Exception as e:
#     print("FAILED:", e)

# ##################################################################################
# ##################################################################################
