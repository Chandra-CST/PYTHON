import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    def __init__(self):
        try:
            if Path(self.database).exists():
                with open(self.database, 'r') as fs:
                    content = fs.read()

                    if content:
                        Bank.data = json.loads(content)
                    else:
                        Bank.data = []

            else:
                with open(self.database, 'w') as fs:
                    json.dump([], fs)

        except Exception as err:
            print(f'An Exception has occurred: {err}')

    def update(self):
        with open(self.database, 'w') as fs:
            json.dump(Bank.data, fs, indent=4)

    @classmethod
    def accountgenerator(cls):
     num = random.choices(string.digits, k = 12)
     return "".join(num)


    def create_account(self):
        info = {
            'First_Name': input('Enter your first name: '),
            'last_Name': input('Enter your last name: '),
            'Age': int(input('Enter your age: ')),
            'Email': input('Enter your Email: '),
            'PIN': input('Enter your 4 digit PIN: '),
            'AccountNO': Bank.accountgenerator(),
            'Balance': 0
        }

        if info['Age'] < 18 or not info['PIN'].isdigit() or len(info['PIN']) != 4:
            print("Sorry, You are not eligible!")

        else:
            Bank.data.append(info)
            self.update()

            print("\nYour Account has been created successfully!\n")

            for key, value in info.items():
                print(f"{key}: {value}")

            print('\nNote down your Account Number carefully.')

    def deposit_money(self):
        limit = int(10000)
        pin = input('Enter your PIN: ')
        for i in Bank.data:
            if i['PIN'] == pin:
                amount = int(input('Enter the amount to deposit: '))
                if amount > limit :
                    print('Only 10000 can be deposited at once!')
                else:
                    i['Balance'] += amount
                    print('Your money has been deposited successfully!')
        self.update()            

                
    

    def withdraw_money(self):
        limit = int(10000)
        pin = input('Enter your pin: ')
        found = False
        for i in Bank.data:
            if i['PIN'] == pin:
                found = True
                withdraw = int(input('Enter the amount you want to withdraw: '))
                if withdraw > i['Balance']:
                    print('Insufficient Balance!')
                elif withdraw > limit :
                    print('Only 10000 can be withdrawn at once!')
                else:
                    i['Balance'] -= withdraw
                    print('Successful!')
                    break
        self.update()            

             

    def account_details(self):
        pin = input('Enter PIN: ')
        for i in Bank.data:
            if i['PIN'] == pin:
                print(f'\n------------ACCOUNT DETAILS------------\n')
                for key, values in i.items():
                    print(f'{key}: {values}')
                return
                

        print('INVALID PIN!')        

        

    def update_account(self):
        pin = input('Enter your PIN: ')
        for i in Bank.data:
                if i['PIN'] == pin:
                  print('Account found, Enter new detils: ')
                  first_name = input('Enter your new first Name: ')
                  last_name = input('Enter your new last Name: ')    
                  new_pin = (input('Enter your new pin:'))
                  e_Mail = input('Enter your new e-mail id: ')

                  if not new_pin.isdigit() or len(new_pin) != 4:
                      print('Invalid Pin')
                      return
                  
                  i['First_Name'] = first_name
                  i['Last_Name'] = last_name
                  i['PIN'] = new_pin
                  i['Email'] = e_Mail



        self.update()     
        print('Account updated successfully!')   
        return

    print('Invalid Pin or account not found!')    

            


    def delete_account(self):
        pin = input('Enter your pin: ')
        for i in Bank.data:
            if i['PIN'] == pin: 
                print('Are you sure you want to delete your account?')
                choice = input('Enter YES or NO: ')
                if choice == 'YES':
                    Bank.data.remove(i)
                    self.update()
                    print('Account deleted successfully!')

                elif choice == 'NO':
                    print('Account deletion cancelled!')

user = Bank()

print("Press 1 for creating an account")
print("Press 2 to deposit money")
print("Press 3 to withdraw money from the account")
print("Press 4 to see account details")
print("Press 5 to update your account")
print("Press 6 to delete your account")

check = int(input("Tell us your response: "))

if check == 1:
    user.create_account()

elif check == 2:
    user.deposit_money()

elif check == 3:
    user.withdraw_money()

elif check == 4:
    user.account_details()

elif check == 5:
    user.update_account()

elif check == 6:
    user.delete_account()

else:
    print("Invalid Input!")
