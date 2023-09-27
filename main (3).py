
This site uses cookies to deliver our services and to show you relevant ads. By using our site, you acknowledge that you have read and understood our Privacy Policy. Your use of w3resource Services, is subject to these policies More info

w3resource
Java Inheritance Programming - BankAccount class with methods called deposit() and withdraw()
Last update on May 06 2023 12:55:46 (UTC/GMT +8 hours)

Java Inheritance: Exercise-5 with Solution
Write a Java program to create a class known as "BankAccount" with methods called deposit() and withdraw(). Create a subclass called SavingsAccount that overrides the withdraw() method to prevent withdrawals if the account balance falls below one hundred.

Sample Solution:

Java Code:

// BankAccount.java
// Parent class BankAccount
public class BankAccount {
    private String accountNumber;
    private double balance;

    public BankAccount(String accountNumber, double balance) {
        this.accountNumber = accountNumber;
        this.balance = balance;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public void withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
        } else {
            System.out.println("Insufficient balance");
        }
    }

    public double getBalance() {
        return balance;
    }
}

// SavingsAccount.java
// Child class SavingsAccount
public class SavingsAccount extends BankAccount {
    public SavingsAccount(String accountNumber, double balance) {
        super(accountNumber, balance);
    }

    @Override
    public void withdraw(double amount) {
        if (getBalance() - amount < 100) {
            System.out.println("Minimum balance of $100 required!");
        } else {
            super.withdraw(amount);
        }
    }
}