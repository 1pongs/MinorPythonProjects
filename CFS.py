print("Script started")
import gspread
from oauth2client.service_account import ServiceAccountCredentials
print("Libraries imported successfully")
# Define the scope
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
# Add your JSON key file
print("Setting up credentials")
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
# Authorize the client
print("Authorizing client")
client = gspread.authorize(creds)
# Open the spreadsheet by its name or by key
print("Opening spreadsheet")
spreadsheet = client.open('CFS V2025.3')  # Ensure you replace this with the actual name or key
# Access a specific worksheet
print("Accessing worksheet")
worksheet = spreadsheet.sheet1  # Adjust accordingly if you use a different sheet or name
# Read, write, update operations
print("Reading cell A1")
print(worksheet.cell(1, 1).value)  # Read the value of cell A1
print("Updating cell A1")
worksheet.update_cell(1, 1, 'Hello World!')  # Write 'Hello World!' to cell A1
print("Script completed successfully")
