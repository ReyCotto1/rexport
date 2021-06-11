import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'

    username = '33b7d707bf7675'
    password = 'a94bb262792516'

    message = f"<h3>New Feedback Submission</h3>" \
              f"<ul>" \
              f"<li>Customer: {customer}</li>" \
              f"<li>Dealer: {dealer}</li>" \
              f"<li>Rating: {rating}</li>" \
              f"<li>Comments: {comments}</li></ul>"

    sender = "Private Person <from@example.com>"
    receiver = "A Test User <to@example.com>"
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender
    msg['To'] = receiver

    # Send
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(username, password)
        server.sendmail(sender, receiver, msg.as_string())
