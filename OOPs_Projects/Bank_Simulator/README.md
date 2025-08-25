# Bank Simulator

## Main Entities:
- **Account**:
  - name
  - account_no
  - balance
- **BankSystem**: handles all accounts

---

## Key Functions:
- **create_account(name, account_no, initial_deposit)**  
  ➤ Adds a new user account
- **deposit(account_no, amount)**  
  ➤ Adds money to the account
- **withdraw(account_no, amount)**  
  ➤ Deducts money if sufficient balance
- **transfer(from_account, to_account, amount)**  
  ➤ Transfers money between accounts
- **check_balance(account_no)**  
  ➤ Displays current balance

---

## Expected Output:
- Transaction messages
- balance statements
- error handling for insufficient funds
