from flask import Flask,render_template,request
import sqlite3
app=Flask(__name__)
app.config.from_object(__name__)

# routes
# by default
'''
@app.route('/')
def hello_world():
    return "<h1>Hello world</h1>"

@app.route('/login')
def login():
    return "<h1>Login</h1>"

'''

@app.route('/')
def register():
    return render_template('Home.html')

@app.route('/registration',methods=['POST'])
def registration():
    fname=request.form['Fname']
    email=request.form['email']
    mobile=request.form['mobile']
    pass1=request.form['Pass1']
    pass2=request.form['pass2']
    con=sqlite3.connect('sqlregister.db')
    cursor=con.cursor()
    cursor.execute('insert or ignore into register values(?,?,?,?,?)',[fname,email,int(mobile),pass1,pass2])
    con.commit()
    return render_template('registration.html')

@app.route('/registration',methods=['POST'])
def login():
    fname = request.form['FName']
    email=request.form['email']
    pass1=request.form['pass1']
    con=sqlite3.connect('sqlregister.db')
    cursor=con.cursor()
    cursor.execute('select * from register where Fname=(?) ,email=(?) and pass1=(?)',[fname,email,pass1])
    con.commit()
    if cursor.fetchone():
        return render_template('Home.html')
    return render_template('Home.html')

@app.route('/login')
def login_form():
    return render_template('login_form')

app.run(debug=True)

