from flask import Flask, render_template, request
app = Flask(__name__)

import socket

host = "/tmp/9Lq7BNBnBycd6nxy.socket"

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.connect((host))

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print("post")
        if request.form['command'] == 'Forward':

            sock.sendall(bytes('1', "utf-8"))

        elif request.form['command'] == 'Backward':

            sock.sendall(bytes('2', "utf-8"))

        elif request.form['command'] == 'Right':

            sock.sendall(bytes('3', "utf-8"))

        elif request.form['command'] == 'Left':

            sock.sendall(bytes('4', "utf-8"))
        
        elif request.form['command'] == 'TiltL':

            sock.sendall(bytes('9', "utf-8"))

        elif request.form['command'] == 'TiltR':

            sock.sendall(bytes('10', "utf-8"))

        elif request.form['command'] == 'TiltF':

            sock.sendall(bytes('11', "utf-8"))

        elif request.form['command'] == 'TiltB':

            sock.sendall(bytes('12', "utf-8"))

        elif request.form['command'] == 'Stop':

            sock.sendall(bytes('7', "utf-8"))

        elif request.form['command'] == 'Speed':

            sock.sendall(bytes('8', "utf-8"))

        elif request.form['command'] == 'TurnR':

            sock.sendall(bytes('5', "utf-8"))

        elif request.form['command'] == 'TurnL':

            sock.sendall(bytes('6', "utf-8"))

        elif request.form['command'] == 'Dance':

            sock.sendall(bytes('16', "utf-8"))

    return render_template('pagina.html')



@app.route("/esp_route", methods=['GET'])
def esp_route():
    DATA = request.get_json(force=True)
    respDir = DATA['move']
    
    if   respDir == 'Forward':   sock.sendall(bytes('1', "utf-8"))
    elif respDir == 'Backward':  sock.sendall(bytes('2', "utf-8"))
    elif respDir == 'Right':     sock.sendall(bytes('3', "utf-8"))
    elif respDir == 'Left':      sock.sendall(bytes('4', "utf-8"))
    elif respDir == 'TiltL':     sock.sendall(bytes('9', "utf-8"))
    elif respDir == 'TiltR':     sock.sendall(bytes('10', "utf-8"))
    elif respDir == 'TiltF':     sock.sendall(bytes('11', "utf-8"))
    elif respDir == 'TiltB':     sock.sendall(bytes('12', "utf-8"))
    elif respDir == 'Stop':      sock.sendall(bytes('7', "utf-8"))
    elif respDir == 'Speed':     sock.sendall(bytes('8', "utf-8"))
    elif respDir == 'TurnR':     sock.sendall(bytes('5', "utf-8"))
    elif respDir == 'TurnL':     sock.sendall(bytes('6', "utf-8"))
    elif respDir == 'Dance':     sock.sendall(bytes('16', "utf-8"))
    else: return "error", 500
    
    return "OK", 200

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=False)
 
