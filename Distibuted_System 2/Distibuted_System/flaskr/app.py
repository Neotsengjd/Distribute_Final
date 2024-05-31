from re import T
import time
import service
import concurrent.futures
from flask import Flask, render_template, request


future_list = []
executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)

app = Flask(__name__, template_folder='templates')

### login
@app.route('/', methods = ['GET', 'POST'])
def login():
    return render_template('index.html')




@app.route('/button-press', methods=['POST'])
def button_press(): 
    buyer = request.form.get('studentId')
    ticket = request.form.get('selectedOption')
    first_use = True
    while True:
        global future_list
        running_futures = [f for f in future_list if not f.done()]
        if len(running_futures) < 3 and first_use:
            first_use = False
            print("Starting a new service...")
            future = executor.submit(service.main, ticket, buyer)
            future_list.append(future)
        else:
            print("Waiting for a available server...")
            time.sleep(5)
    
        completed_futures = [f for f in future_list if f.done()]

        for future in completed_futures:
            success = future.result()
            if success:
                return render_template('firstPage.html') # Got ticket
            else:
                return render_template('firstPage.html') # No ticket
            future_list.remove(future)
            
    
        
if __name__ == '__main__':
    app.run(debug=True)
    
