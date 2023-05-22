# Step 1 - To import FLASK
from flask import Flask, request, render_template

# Step 2 - Create the object with a parameter __name__
app = Flask(__name__)


###################################################
# Step 3 - Create an END POINT using routes and bind them with a functionality

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/search', methods=['GET', 'POST'])
def search_fun():
    if request.method == 'POST':
        return "Welcome to the search page using POST Req"
    else:
        return render_template('search.html')


@app.route('/add', methods=['POST', 'GET'])
def add_fun():
    a = request.form.get('var_1')
    b = request.form.get('var_2')
    return str(int(a) + int(b))

###################################################

# Step 4 - Run the app
if __name__ == '__main__':
    app.run(debug=True)