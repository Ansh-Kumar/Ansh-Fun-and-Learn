import sqlite3
import random

conn = sqlite3.connect('bankinfo.db')
cur= conn.cursor()



def create_table():
                cur.execute(' CREATE TABLE IF NOT EXISTS account(First_name TEXT, Last_name TEXT, Number TEXT, Amount REAL) ')

create_table()
print ("Hello Random Person")

new_or_old_account = input("Are you new to this bank or are you already registered? Input either n for new or o for old ")

if new_or_old_account == 'n':
                first_name = input("What is you first name? ")
                last_name = input("What is you last name? ")
                Number = input("What is your phone number? ")
                amount = int(input("How much money are you going to deposit (it has to be more than $100)? (do not put a dollar sign) "))
                if amount <= 100:
                                amount = input("Please try it again: ")
                else:             
                                print ("Your account has been saved") 
                                
                def data_entry():
                                cur.execute("INSERT INTO account(First_name, Last_name, Number, Amount)  VALUES (?, ?, ?, ?)",
                                          (first_name, last_name, Number, amount))
                                conn.commit()
                data_entry()





elif new_or_old_account == 'o':
                checknum = input("What was the first name you had inputed? ")
                cur.execute("SELECT * FROM account WHERE First_name =  ?",(checknum,))
                rec = cur.fetchone()
                amt = rec[3]
                d_w = input("Do you want to withdraw or deposit money? (d for deposit, w for withdrawl)")
                d_w = d_w.lower()
                if d_w == 'd' or 'deposit':
                                amount_deposit = input("How much money would you like to deposit?")
                                amt = int(amt)
                                amount_deposit = int(amount_deposit)
                                cur.execute('UPDATE account SET amount = (?)', (amt+amount_deposit))
