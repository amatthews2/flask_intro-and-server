from flask import Flask

app = Flask(__name__)
# creates flask class which has all functions needed for server
# stored in app
# __name__ is basis of server --> file this is run from
# sets up server for app variable

if __name__ == "__main__":
    app.run
