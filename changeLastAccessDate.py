import os
import time
from datetime import datetime

def has_access(folder_path):
    try:
        os.listdir(folder_path)
        return True
    except PermissionError:
        return False
def change_access_date():
   while True:
       folder_path = input("Enter the folder_path: ")
       if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
           print("Error: Please provide the existing folder_path")
       elif not has_access(folder_path):
           print("Error: Access to the folder is restricted. Unable to perform the operation.")
           return
       else:
           break
   while True:
       new_date = input("Enter the new access date (YYYY-MM-DD): ")
       try:
           new_date = str(new_date)
           new_date = datetime.strptime(new_date, "%Y-%m-%d")
       except ValueError:
           print("Error: Invalid date format. Please use YYYY-MM-DD.")
           continue
       current_date = datetime.now()
       if new_date > current_date:
           print("Error: New access date should be equal or less than today's date.")
       else:
           break
   last_access_date_5yrs = time.time() - (1 * 365 * 24 * 60 * 60)
   new_access_timestamp = time.mktime(new_date.timetuple())
   for root, dirs, files in os.walk(folder_path):
       for file_name in files:
           file_path = os.path.join(root, file_name)
           access_time = os.path.getatime(file_path)
           if access_time < last_access_date_5yrs:
               os.utime(file_path, (new_access_timestamp, os.path.getmtime(file_path)))
               print(f"Last accessed date changed to {new_date}")
           else:
               print('Recently accessed')
if __name__ == "__main__":
   change_access_date()
   input("Press enter to close the program")