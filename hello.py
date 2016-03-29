from flask import Flask, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up for flask
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

# set up for gspread
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
gc = gspread.authorize(credentials)

@app.route('/')
def hello_world():
    sh = gc.open("Charged Question Responses")
    worksheet = sh.get_worksheet(0)
    val = worksheet.acell('A1').value
    return val

if __name__ == '__main__':
    app.run()