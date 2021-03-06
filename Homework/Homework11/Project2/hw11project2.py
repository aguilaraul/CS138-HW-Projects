#
# author    Raul Aguilar
# date      July 6, 2020
#
# CS 138 1535 Homework 11 Project 2
# Write a program that simulates an automatic teller machine.
#
from atminterface import ATMInterface
from atm import ATM

def main():
    inter = ATMInterface()
    atm = ATM(inter)
    atm.run()


main()
