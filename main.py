from flask import Flask, render_template, request
import smtplib
import os 

MAIL_ADDRESS = os.environ.get('MAIL_ID')
MAIL_APP_PW = os.environ.get('MAIL_PW')
COMPANY_ADDRESS = os.environ.get('COMPANY_ID')
PHONE = os.environ.get('PHONE')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        try:
            with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
                connection.starttls()
                connection.login(user=MAIL_ADDRESS, password=MAIL_APP_PW)
                connection.sendmail(from_addr=MAIL_ADDRESS,
                                    to_addrs=COMPANY_ADDRESS,
                                    msg=f'Subject:Website Contact\n\nName: {name}\nEmail: {email}\nMessage: {message}')
        except Exception as e:
            print(f"An error occurred: {e}")
        
    return render_template('index.html', phone=PHONE, mail=COMPANY_ADDRESS)

if __name__ == '__main__':
    app.run(debug=False, port=5001)


