"""
Main module of the server file
"""

import json
# Local modules
import config
from __init__ import (
    __title__,
    __version__,
    __url__
)


# Get the application instance
connex_app = config.connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")


# Create a URL route in our application for "/"
@connex_app.route("/")
def root():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:        the application info
    """
    return json.dumps({'name': __title__, 'version': __version__, 'url': __url__})


# Create a URL route in our application for "/status"
@connex_app.route("/status")
def status():
    """
    This function just responds to the browser URL
    localhost:5000/status

    :return:        the application info
    """
    return json.dumps({'status': 'OK'})


if __name__ == "__main__":
    connex_app.run(debug=True)
