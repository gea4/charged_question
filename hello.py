from flask import Flask, render_template, request, session, g, redirect, url_for, abort, flash
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
    responses = worksheet.get_all_values()
    responses = responses[1:]
    responses = [dict(time=row[0], text=row[1], name=row[2]) for row in responses]
    return render_template('show_responses.html', responses=responses)

if __name__ == '__main__':
    app.run()