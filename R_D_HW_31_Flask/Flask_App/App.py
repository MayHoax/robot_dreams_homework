from flask import Flask, logging
import logging
from logging.config import dictConfig


app = Flask(__name__)
logger = logging.getLogger('First_logger_ever')



@app.route('/hello')
def hello():
    app.logger.info('/hello requested')
    return "Hello, world!"


if __name__ == '__main__':
    app.run(debug=True)