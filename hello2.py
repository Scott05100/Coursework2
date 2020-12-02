from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def root():
    return render_template('hello.html')


@app.route("/AboutTheTutors/")
def AboutTheTutors():
    return render_template('AboutTheTutors.html')
    
@app.route("/Account/")
def Account():
    return render_template('Account.html')

@app.route("/AboutTheSubjects/")
def AboutTheSubjects():
    return render_template('AboutTheSubjects.html')

@app.route("/Account/LogIn/")
def Login():
    return render_template('LogIn.html')

@app.route("/Account/SignUp/")
def SignUp():
    return render_template('SignUp.html')

@app.route("/Account/LogIn/MyAccount/")
def MyAccount():
    return render_template('MyAccount.html')

@app.route("/Account/LogIn/MyAccount/RequestATutor/")
def RequestATutor():
    return render_template('RequestATutor.html')

@app.route("/Account/LogIn/MyAccount/EditAccountDetails/")
def EditAccountDetails():
    return render_template('EditAccount.html')

@app.route("/Account/LogIn/MyAccount/ViewMyMeetings/")
def ViewMyMeetings():
    return render_template('ViewMyMeetings.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

