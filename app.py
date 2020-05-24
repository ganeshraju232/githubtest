from flask import Flask
import smtplib,os

app=Flask(__name__)
@app.route("/")
def index():
   return render_template("index.html")
@app.route("/register",methods=["POST"])
def register():
   name=request.form.get("name")
   email=request.form.get("email")
   if not name or not email:  
      return "it is a failure"
   message="ÿou are tegistered"
   server=smtplib.SMTP("smtp.gmail.com",500)
   server.starttls()
   server.login("ganeshraju232.net",os.getenv("PASSWORD"))
   server.sendmail("ganeshraju232.net",email,message)
   return render_template("success.html")

