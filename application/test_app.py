import redis
import time 
from flask import Flask
app = Flask(__name__)
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)

@app.route("/test/<key>")
def testApp(key):
	r = redis.StrictRedis(connection_pool=pool)
	r.set(key, time.time())

	return r.get(key)

if __name__=="__main__":
	app.run(host='0.0.0.0')




