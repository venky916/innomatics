#step-1
from flask import Flask,render_template,request,Response
import re

#step-2
app=Flask(__name__)

#############################################################
@app.route('/' ,methods=['GET','POST'])
def home():
    if request.method=='POST':
        pattern=request.form.get('pattern')
        string=request.form.get('inp_str')
        matches =re.findall(pattern,string)
        if matches:
            match='\n'.join(matches)
            return render_template('index.html',matches=match,input=string,regex=pattern)
        else:
            return render_template('index.html',matches='No match',input=string,regex=pattern)

    else:
        return render_template('index.html')



####################################################################
#step-4
if __name__=='__main__':
    app.run(debug=True)