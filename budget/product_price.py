import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope=['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']

cred=ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client=gspread.authorize(cred)
sheet=client.open('ProductPrice').sheet1
stuff=sheet.get_all_records()
print(stuff)