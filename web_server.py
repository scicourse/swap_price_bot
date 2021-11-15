from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return 'web server is up and running'
def run():
  app.run(host='0.0.0.0', port=8080)
def keep_run():
  t = Thread(target=run)
  t.start()