from flask import Flask, render_template, request

app = Flask(__name__)

################################################
# Route 1
@app.route('/')
def home_fun():
    return render_template('index.html')

# Route 2
@app.route('/thankyou', methods=['POST'])
def thankyou_fun():
    user = request.form.get('user_name')
    return render_template('thankyou.html', user_name=user)


###############################################

if __name__ == '__main__':
    app.run(debug=True)