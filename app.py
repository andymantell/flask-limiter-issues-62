import os
from flask import Flask, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)
app.config['RATELIMIT_HEADERS_ENABLED'] = True
app.config['RATELIMIT_STORAGE_URL'] = os.environ['REDIS_URL']


limiter = Limiter(
    app,
    key_func=get_remote_address
)


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/rate-limited-route")
@limiter.limit("5 per minute")
def rate_limited_route():
    return "Rawr"

if __name__ == "__main__":
    app.run()
