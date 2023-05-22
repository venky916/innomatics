# Step 1 - To import FLASK
from flask import Flask,request

# Step 2 - Create the object with a parameter __name__
app = Flask(__name__)

###################################################
# Step 3 - Create an END POINT using routes and bind them with a functionality
@app.route('/')
def home_page():
    return "Welcome to HOME PAGE"

@app.route('/search')
def search_page():
    return "Welcome to the search page"

@app.route('/add')
def add_page():
    a=request.args.get('a')
    b=request.args.get('b')
    return str(int(a)+int(b))

@app.route('/upper')
def up():
    a=request.args.get('user')
    return a.upper()

@app.route('/squarespage')
def squares():
    a=request.args.get('a')
    st=[]
    for i in range(int(a)):
        st.append(str(i**2))
    return ' | '.join(st)


###################################################

# Step 4 - Run the app
if __name__ == '__main__':
    app.run(debug=True)