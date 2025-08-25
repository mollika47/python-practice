import json
import os

file_name = "bank-data.json"

def load_accounts():
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            return json.load(f)
    return []

def save_accounts(accounts):
    with open(file_name, 'w') as f:
        json.dump(accounts, f, indent=4)


class BankSimulator:
    def __init__(self):
        self.accounts = load_accounts()

    def create_account(self, account_no, name, initial_deposit):
        try:
            account_no = int(account_no)
            initial_deposit = int(initial_deposit)

            for acc in self.accounts:
                if acc['Account_no'] == account_no:
                    print(f"Account no: {acc['Account_no']} already exists.")
                    return

            if initial_deposit > 0:
                self.accounts.append({
                    "Account_no": account_no,
                    "Name": name,
                    "Initial Deposit": initial_deposit
                })
                save_accounts(self.accounts)
                print(f"Account created with initial balance: {initial_deposit}.")

            else:
                print("Initial deposit must be greater than 0.")

        except ValueError:
            print("Account number and initial balance must be an integer.")

        except Exception as e:
            print("Something went wrong." , e)

    def deposit(self, account_no, amount):
        try:
            account_no = int(account_no)
            amount = int(amount)
            found = None

            for acc in self.accounts:
                if acc['Account_no'] == account_no:
                    found = acc
                    if 'Current Balance' not in acc:
                        acc['Current Balance'] = acc['Initial Deposit']

                    if amount > 0:
                        acc['Current Balance'] += amount
                        save_accounts(self.accounts)
                        print(f"Deposited {amount}tk. New Balance: {acc['Current Balance']}tk.")
                    else:
                        print("Amount must be greater than 0.")
            if not found:
                print(f"{account_no} Account not found.")

        except ValueError:
            print("Account number and amount must be an integer.")

        except Exception as e:
            print("Something went wrong." , e)

    def withdraw(self, account_no, amount):
        try:
            account_no = int(account_no)
            amount = int(amount)
            found = None

            if amount <= 0:
                print("Amount must be greater than 0.")
                return

            for acc in self.accounts:
                if acc['Account_no'] == account_no:
                    found = acc
                    if 'Current Balance' not in acc:
                        acc['Current Balance'] = acc['Initial Deposit']

                    if acc['Current Balance'] > amount:
                        remaining = acc['Current Balance'] - amount
                        if remaining >= 500:
                            acc['Current Balance'] = remaining
                            save_accounts(self.accounts)
                            print(f"{amount}tk has been withdrawn. \nNew Balance: {remaining}tk.")
                    else:
                        max_withdrawal = acc['Current Balance'] - 500
                        print(f"Not sufficient balance. \nCurrent Balance: {acc['Current Balance']}. \nMax withdrawal: {max_withdrawal}")
            if not found:
                print(f"{account_no} Account not found.")

        except ValueError:
            print("Account number and amount must be an integer.")

        except Exception as e:
            print("Something went wrong." , e)

    def transfer(self, from_acc, to_acc, amount):
        found_from = None
        found_to = None

        try:
            from_acc = int(from_acc)
            to_acc = int(to_acc)
            amount = int(amount)

            if amount <= 0:
                print("Amount must be greater than 0.")
                return

            for acc in self.accounts:
                if acc['Account_no'] == from_acc:
                    found_from = acc
                if acc['Account_no'] == to_acc:
                    found_to = acc

            if not found_from:
                print(f"{from_acc} Account not found.")
                return
            if not found_to:
                print(f"{to_acc} Account not found.")
                return

            if 'Current Balance' not in found_from:
                found_from['Current Balance'] = found_from['Initial Deposit']
            if 'Current Balance' not in found_to:
                found_to['Current Balance'] = found_to['Initial Deposit']

            if found_from['Current Balance'] < amount:
                print("Not sufficient balance.")
                return

            remaining = found_from['Current Balance'] - amount
            if remaining >= 500:
                found_from['Current Balance'] = remaining
                found_to['Current Balance'] += amount
                save_accounts(self.accounts)
                print(f"{amount}tk has been transferred from Account_no: {from_acc} to Account_no: {to_acc}.")
                print(
                    f"Sender: \nAccount_no: {from_acc} \nTransferred amount: {amount}tk. \nNew Balance: {remaining}tk.")
                print(
                    f"Receiver: \nAccount_no: {to_acc} \nTransferred amount: {amount}tk. \nNew Balance: {found_to['Current Balance']}tk.")
            else:
                print("Cannot transfer. Minimum balance of 500tk must remain.")
                return

        except ValueError:
            print("Account numbers and amount must be an integer.")

    def check_balance(self, account_no):
        found = None

        try:
            account_no = int(account_no)

            for acc in self.accounts:
                if acc['Account_no'] == account_no:
                    found = acc
                    if 'Current Balance' in acc:
                        print(f"Account no: {acc['Account_no']} \nName: {acc['Name']} \nCurrent Balance: {acc['Current Balance']}")
                        return
                    if 'Current Balance' not in acc:
                        print(f"Account no: {acc['Account_no']} \nName: {acc['Name']} \nInitial Deposit: {acc['Initial Deposit']} \nNo transaction made yet.")
                        return

            if not found:
                print(f"{account_no} Account not found.")

        except ValueError:
            print("Account number must be an integer.")

if __name__ == "__main__":
    bank = BankSimulator()

    # bank.create_account(1006, "Isabel", 2000)
    # bank.deposit(1002, 50000)
    # bank.withdraw(1002, 5000)
    # bank.transfer(1001, 1004, 2000)
    # bank.check_balance(1003)
