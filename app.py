from flask import Flask, render_template, request
import re
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/match', methods=['POST'])
def match():
    test_string = request.json['test_string']
    regex_pattern = request.json['regex_pattern']
    matches = re.findall(regex_pattern, test_string)
    return json.dumps(matches)  


@app.route('/valid_email', methods=['GET', 'POST'])
def validate_email():
    if request.method == 'POST':

        email = request.form.get('email')

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if email and re.match(pattern, email):
            valid = True
        else:
            valid = False

        return render_template('result.html', email=email, valid=valid)
    else:
        return render_template('result.html')



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)



       



