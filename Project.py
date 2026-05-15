import json
from pathlib import Path

class BANK:
    database = 'data.json'
    data = []

    def __init__(self):
        try:
            if Path(self.database).exists(): 
                with open(self.database) as fs:
                    self.data = json.loads(fs.read())
            else:
                print("No such file exists!")
        except Exception as err:
            print(f'An Exception has occured as {err}')        


    def update(self):
        with open(self.database, "w") as fs:
            fs.write(json.dumps(self.data))


    def createaccount(self):
        info = {
            'Name': input('Enter your name:'),
            'age': int(input('Enter your age:')),
            'Email': input('Enter your Email:'),
            'PIN': int(input('Enter your PIN:')),
            'accountNO': '12345',
            'Balance': 0
        }
        if info['age'] < 18 or len(str(info['PIN'])) != 4:
            print("Sorry, You are not eligible!")
        else:
            print("Your Account has been created successfully!")

            for i in info:
                print(f"{i}: {info[i]}")
                print('Note down your Account Number')

            self.data.append(info)
            self.update()

        try:
            with open(self.database, 'w') as fs:
                json.dump(self.data, fs, indent=4)
        except Exception as err:
            print(f'Failed to save account: {err}')

user = BANK()
print("Press 1 for creating an account")
print("Press 2 to depposit money")
print("Press 3 to withdraw money from the account")
print("Press 4 for account's details")
print("Press 5 to update your account")
print("Press 6 to delete your account")

check = int(input("Tell us your response:-"))

if check == 1:
    user.createaccount()
