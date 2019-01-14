import gspread
from oauth2client.service_account import ServiceAccountCredentials

def main(name):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret_sheet.json', scope)

    gc = gspread.authorize(credentials)

    gsheet = gc.open('MemberList').sheet1
    findPersonValue = gsheet.find(name)
    print(findPersonValue)
    personPaidStatus = gsheet.cell(findPersonValue.row, 2).value
    print(personPaidStatus)
    return personPaidStatus

def sign_in(name, date):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret_sheet.json', scope)
    gc = gspread.authorize(credentials)
    gsheet = gc.open('MemberSignIn').sheet1
    gsheet.append_row([name, 'Sign In', date])

def register(name, date):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret_sheet.json', scope)
    gc = gspread.authorize(credentials)
    gsheet = gc.open('MemberSignIn').sheet1
    gsheet.append_row([name, 'Register', date])

def one_day(name, date):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret_sheet.json', scope)
    gc = gspread.authorize(credentials)
    gsheet = gc.open('MemberSignIn').sheet1
    gsheet.append_row([name, 'One Day', date])