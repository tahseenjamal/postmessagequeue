from flask import Flask, abort, request, jsonify
import json, thread, sys, requests
from Queue import Queue
from time import sleep

messageQueue = Queue()

target_url = sys.argv[1]

total_threads = int(sys.argv[2])

app = Flask(__name__)


@app.route('/', methods=['POST']) 
def receive():

    if not request.json:

        abort(400)

    messageQueue.put(request.json)

    return jsonify({'success' : 200})

@app.route('/queue') 
def queuecount():

    return "Total Queue Size = {}".format(messageQueue.qsize())


def printdata():

    while True:

        while not messageQueue.empty():

            print messageQueue.get()

            requests.post(target_url, data = messageQueue.get())

        sleep(0.1)


for loop in range(0, total_threads):

    thread.start_new_thread(printdata,())


if __name__ == '__main__':
    app.run("0.0.0.0", threaded=True, port=8080)




