from flask import Flask, render_template ,request

app = Flask(__name__)

@app.route('/' ,methods=['GET', 'POST'])
def home():
    if request == "POST": 
        username = request.form.get('username')
        password = request.form.get('password') 
        return f'Username: {username}, Password: {password}'
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)