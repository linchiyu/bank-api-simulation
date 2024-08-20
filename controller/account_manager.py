from typing import Optional

from model.account import Account

class AccountManager:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id: str) -> Account:
        if self.get_account(account_id) is not None:
            raise ValueError("Account already exists")
        account = Account(account_id, 0)
        self.accounts[account_id] = account
        return account

    def get_balance(self, account_id: str) -> float:
        """
        Retrieve the balance of the account with the specified account_id.

        Args:
            account_id (int): The ID of the account to retrieve the balance of.

        Returns:
            float: The balance of the account with the specified account_id.
        """
        # Retrieve the account from the dictionary using the account_id
        account = self.get_account(account_id)
        if account is None:
            raise ValueError("Account not found")
        return account.get_balance()

    def get_account(self, account_id: str) -> Account:
        """
        Retrieve the account with the specified account_id.

        Args:
            account_id (int): The ID of the account to retrieve.

        Returns:
            Account: The account with the specified account_id, or None if it does not exist.
        """
        # Retrieve the account from the dictionary using the account_id
        return self.accounts.get(account_id)

    def deposit(self, account_id: str, amount: float) -> Account:
        """
        Deposits the specified amount into the account balance.

        Args:
            account_id (int): The ID of the account to deposit into.
            amount (float): The amount to deposit into the account.

        Returns:
            Account: The updated account after the deposit.
        """
        # Retrieve the account from the dictionary using the account_id
        account = self.get_account(account_id)
        if account is None:
            account = self.create_account(account_id)

        # Deposit the amount into the account balance
        account.deposit(amount)

        # Return the updated account
        return account

    def withdraw(self, account_id: str, amount: float) -> Optional[Account]:
        """
        Withdraws the specified amount from the account balance.

        Args:
            account_id (int): The ID of the account to withdraw from.
            amount (float): The amount to withdraw from the account.

        Returns:
            Account: The updated account after the withdrawal, or None if the account does not exist.
        """
        # Retrieve the account from the dictionary using the account_id
        account = self.get_account(account_id)

        # If the account does not exist, return None
        if account is None:
            return None

        # Withdraw the specified amount from the account balance
        account.withdraw(amount)

        # Return the updated account
        return account

    def reset(self) -> None:
        """
        Resets the account manager by clearing all existing accounts.

        This method is used to reset the account manager to its initial state.
        All existing accounts are deleted and the account manager is reset
        to an empty state.
        """
        # Clear the dictionary of accounts
        self.accounts = {}

