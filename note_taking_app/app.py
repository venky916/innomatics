from flask import Flask, render_template, request,session,redirect,url_for

app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/', methods=['GET','POST'])
def index():
    if 'notes' not in session:
        session['notes'] = []

    if request.method == "POST":
        note = request.form.get("note")
        get_note=str(note).strip(' ')
        
        if len(get_note)!=0:
            note_list = session["notes"]
            note_list.append(get_note)
            session["notes"] = note_list
            print(session)
            return redirect(url_for('index'))
        
    return render_template("home.html", notes=session["notes"])
    

if __name__ == '__main__':
    app.run(debug=True)
