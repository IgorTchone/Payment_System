# -*- coding: utf-8 -*-
"""Payment_System

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/103WRFtwE4lcdhg8iCrN6rNg-HXhpb33B
"""

class PaymentMethod:
    def processPayment(self):
        print("Processing payment")


class CreditCard(PaymentMethod):
    def processPayment(self):
        print("-----------------------------------------------")
        print("Processing payment with credit card")
        print("-----------------------------------------------")


class PayPal(PaymentMethod):
    def processPayment(self):
        print("------------------------------------")
        print("Processing payment with PayPal")
        print("------------------------------------")


class Main:
    @staticmethod
    def main():
        print("Choose a payment method: ")
        print("1 - Credit card")
        print("2 - PayPal")
        choice = input()

        if choice == "1":
            payment_method = CreditCard()
            payment_method.processPayment()
        elif choice == "2":
            payment_method = PayPal()
            payment_method.processPayment()
        else:
            print("---------------")
            print("Invalid option")
            print("---------------")


Main.main()