from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('login.html')

@app.route('/hi/<name>')
def hi(name):
   return 'Hi %s~' % name

@app.route('/n/<int:no>')
def showno(no):
   return 'Your no. is %d' % no

@app.route('/r/<float:rno>')
def showrno(rno):
   return 'Your rno. is %f' % rno


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      #print("DBG>> In POST path!")
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name
   
if __name__ == '__main__':
   app.run()
