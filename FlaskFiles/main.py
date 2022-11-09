from flask import Flask, render_template, request
app = Flask(__name__)

import socket

host = "/tmp/9Lq7BNBnBycd6nxy.socket"

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.connect((host))

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        sock.sendall(bytes('1', "utf-8"))

    return render_template('pagina.html', status = 0)



@app.route("/botao", methods=['GET'])
def botaoApertado():

    sock.sendall(bytes('O', "utf-8"))
    received = str(sock.recv(1024), "utf-8")

    return {"value": received}

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=False)
 