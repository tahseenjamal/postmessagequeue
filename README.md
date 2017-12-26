This program cushion the requests and offloads the producer from holding connections if the consumer is slow or cannot take spike load


You can use it before Elastic Search in case your program is writing faster than the throughout rate of ES Instance. This want your producer instance would be off loaded from load


Requirements

pip install requests flask



Run it inside a screen


You can edit the port or route it through nginx


python postmq.py TARGET-URL NUMBER-OF-THREADS



Test CURL format

curl -i -H "Content-Type: application/json" -X POST -d '{"user" : "Tahseen"}' http://localhost:PORT/

Also there is a GET URL for finding out Queue size

curl http://localhost:PORT/queue
