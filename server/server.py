from flask import Flask, render_template, flash
import forms
import db_operations as dbo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bfb9f13102dc4c807e14ed5975a1471d'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.MarkAttendance()
    if form.validate_on_submit():
        flag= dbo.checkRecord( str(form.name.data), str(form.rollnum.data), str(form.mac.data) )
        #print(flag)
        if(flag):
            #dbo.markAttendance(form.name, form.rollnum)
            return ("Verified")
        else:
            #remember to clear the error table everytime the teacher interface is booted
            dbo.addToError(str(form.name.data), str(form.rollnum.data))
            return("Not Verified")
    return (render_template('index.html', form=form))


if __name__ == '__main__':
    app.debug=True
    app.run()