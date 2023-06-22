from flask import Flask, redirect, url_for, render_template, request, session, flash
import requests
import json

# from flask_sqlalchemy import SQLAlchemy
# import os
# os.system("pip install Flask-SQLAlchemy")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pythonwork'



# class UserInfo(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(80), nullable=False)
#     lastname = db.Column(db.String(80), nullable=False)
#     number = db.Column(db.Float, nullable=False)
#
#     def __str__(self):
#         return f'სახელი -  {self.title}, გვარი - {self.author}, ნომერი - {self.price}'


# with app.app_context():
#     db.create_all()
    # b1 = UserInfo(name='shrek', lastname='shrekker', number=679123432)
    # db.session.add(b1)
    # db.session.commit()
    # b7 = UserInfo.query.first()
    # print(b7)
    # all = UserInfo.query.all()
    # b6 = UserInfo.query.get(5)
    # db.session.delete(b6)
    # db.session.commit()
    # idk = UserInfo.query.filter_by(name='shrek').all()
    # for each in all:
    #     print(each)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/product', methods=['POST', 'GET'])
def product():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
        return redirect(url_for('user'))

    return render_template('product.html')



@app.route('/user')
def user():

    return render_template('user.html')


@app.route('/<name>/<age>')
def userage(name, age):
    return f'Hello {name}, your age is {age}'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return 'you are logged out'
@app.route('/youshallnotpass')
def youshouldnthavedonethat():
    return render_template('youshouldnthavedonethat.html')
@app.route('/delivery')
def delivery():
    return render_template('delivery.html')

# response = requests.get(f'https://api.adviceslip.com/advice')
# result = response.json()
# text = response.text
# with open('advice.json', 'w') as file:
#     file.write(response.text)
#     json.dump(result, file, indent=4)
# s = text.split(" ")
# print(s)
# for i in range(len(s)):
#     l = s[5::1]
    





if __name__ == "__main__":
    app.run(debug=True)