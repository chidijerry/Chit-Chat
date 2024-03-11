from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)







@app.route('/signup', methods=["GET","POST"])
def sign():
	if (request.method == "POST"):
		return redirect(url_for('login'))
	else:
		return render_template('signup.html')




@app.route('/login', methods=["GET","POST"])
def login():
	if (request.method == "POST"):
		return render_template('home.html')
	else:
		return render_template('login.html')






@app.route('/create', methods=["POST"])
def create():
	return render_template('create.html')



@app.route('/join', methods=["POST"])
def join():
	return render_template('join.html')



@app.route('/chat', methods=["POST"])
def chat():
	return render_template('chat.html')



@app.route('/logout', methods=["POST"])
def logout():
	return redirect(url_for('login'))




if __name__ == ('__main__'):
	app.run(debug=True)