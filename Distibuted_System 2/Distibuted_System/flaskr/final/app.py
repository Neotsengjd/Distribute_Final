from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        student_id = request.form['studentId']
        selected_option = request.form['selectedOption']
        flash(f'學號: {student_id}, 選項: {selected_option}', 'success')
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
