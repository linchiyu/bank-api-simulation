class Account:
    def __init__(self, id: str, balance: float):
        """
        Initializes an Account object.

        Args:
            id (int): The account ID.
            balance (float): The initial account balance.
        """
        # Assign the account ID
        self.id: str = id

        # Assign the initial account balance
        self.balance: float = balance

    def get_balance(self) -> float:
        """
        Retrieves the current balance of the account.

        This method returns the current balance of the account.

        Returns:
            float: The current balance of the account.
        """
        # Return the current balance
        return self.balance

    def deposit(self, amount: float) -> float:
        """
        Deposits the specified amount into the account balance.

        Args:
            amount (float): The amount to be deposited into the account.

        Returns:
            float: The updated account balance after the deposit.
        """
        # Add the deposit amount to the current balance
        self.balance += amount

        # Return the updated account balance
        return self.balance

    def withdraw(self, amount: float) -> float:
        """
        Withdraws the specified amount from the account balance.

        Args:
            amount (float): The amount to be withdrawn from the account.

        Returns:
            float: The updated account balance after the withdrawal.
        """
        # Subtract the withdrawal amount from the account balance
        self.balance -= amount

        # Return the updated account balance
        return self.balance