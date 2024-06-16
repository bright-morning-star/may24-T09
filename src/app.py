from flask import Flask, request, render_template

app = Flask(__name__)


# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_input = dict(request.form)
        print(form_input)
        return render_template('index.html', )
    #return render_template('index.html')