from re import T
import time
import master
import concurrent.futures
from flask import Flask, render_template, request
from kazoo.client import KazooClient
from kazoo.exceptions import KazooException, LockTimeout
from kazoo.handlers.threading import KazooTimeoutError

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
        zk = KazooClient(hosts='127.0.0.1:2181')
        zk.start(timeout=10)
        path = f"/data/ticket/{ticket}/quantity"
        quantity, _ = zk.get(path)
        if int(quantity.decode()) < 1:
            return render_template('fail.html')

        global future_list

        if len(future_list) < 3 and first_use:
            first_use = False
            print("{} -> Starting a new service...".format(buyer))
            future = executor.submit(master.main, ticket, buyer)
            future_list.append(future)
            while True:
                if future.done():
                    success = future.result()
                    future_list.remove(future)
                    if success:
                        return render_template('success.html')
                    else:
                        return render_template('fail.html') 
        else:           
            print("{} -> Waiting for a available server...".format(buyer))
            time.sleep(5)
    
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
