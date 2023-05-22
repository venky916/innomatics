from flask import Flask, render_template, request

app = Flask(__name__)

################################################
# Route 1
@app.route('/')
def home_fun():
    return render_template('index.html')

@app.route('/about')
def about_fun():
    return render_template('about.html')

# Route 2
@app.route('/thankyou', methods=['POST'])
def thankyou_fun():
    user_name = request.form.get('user_name')
    age = int(request.form.get('age'))
    return render_template('thankyou.html', user=user_name, age=age)


###############################################

if __name__ == '__main__':
    app.run(debug=True)