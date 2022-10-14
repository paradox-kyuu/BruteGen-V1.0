import random
import sys
import time
import pyfiglet
from colorama import Fore,Style
import os
from rich.progress import Progress

all_col= [Style.BRIGHT+Fore.RED,Style.BRIGHT+Fore.CYAN,Style.BRIGHT+Fore.LIGHTCYAN_EX, Style.BRIGHT+Fore.LIGHTBLUE_EX, Style.BRIGHT+Fore.LIGHTCYAN_EX,Style.BRIGHT+Fore.LIGHTMAGENTA_EX,Style.BRIGHT+Fore.LIGHTYELLOW_EX]

ran = random.choice(all_col)



def banner():
    os.system("clear")

    print(ran, pyfiglet.figlet_format("\t\t\t    BRUTEGEN"))
    print(ran + "\t\t        V_1.0\t\n\n")
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX, "\n\t    ", "- " * 3, "BY PARADOX-KYUU ", "- " * 3)
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX, "\n", "- " * 3, " Github: https://github.com/paradox-kyuu ", "- " * 3)
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX, "\n [!] BruteGenV1.0 is a Password Generation Script that compiles different passwords to be bruteforced and saves it to a .txt file. [!]")
   
    

banner()

time.sleep(1)


def exit():
    sys.exit()

print(Style.BRIGHT + Fore.RED, "\n", "=+ " * 3, " [!] ENTER ANY RELATED WORDS/DETAILS TO THE VICTIM TO ENSURE SUCCESSFUL BRUTEFORCE [!]", "=+ " * 3)
time.sleep(.3)
def program():	
        id = input(ran+"\nEnter the name of victim (No Spaces): ")
        amount = input(ran+"\nEnter the amount of passwords:")
        amount = int(amount)
        comf = input(ran+"\nDo you want to add more information? [y/n]: ")
        if comf == "y":
                pw1 = input(ran+"\nEnter value: ")
                pw2 = input(ran+"\nEnter value: ")
                pw3 = input(ran+"\nEnter value: ")
                pw4 = input(ran+"\nEnter value: ")
                pw5 = input(ran+"\nEnter value: ")
                pw6 = input(ran+"\nEnter value: ")
                pw7 = input(ran+"\nEnter value: ")
                time.sleep(.6)
                with Progress() as progress:
                	task = progress.add_task("\nCompiling passwords into .txt file | ", total=30)
                	while not progress.finished:
                	 progress.update(task, advance=8)
                	 time.sleep(1)
                file = open("passwords.txt", "a+")
                file.write(id + id + "\n")
                file.write(pw3 + id + "\n")
                file.write(id + pw1 + "\n")
                file.write(id + pw4 + "\n")
                file.write(id + pw6 + "\n")
                file.write(id + pw5 + "\n")
                file.write(pw5 + pw3 + "\n")
                file.write(pw5 + pw1 + "\n")
                file.write(pw6 + pw5 + "\n")
                file.write(pw3 + pw6 + "\n")
                file.write(pw3 + pw6 + "\n")
                file.write(pw2 + pw6 + "\n")
                file.write(pw2 + "\n")
                file.write(pw3 + "\n")
                for i in range(amount):
                        r_num = random.randint(0000, 99999)
                        r_num = str(r_num)

                        file.write(id+r_num+"\n")
                        file.write(pw1+r_num+"\n")
                        file.write(pw2+r_num+"\n")
                        file.write(pw3+r_num+"\n")
                        file.write(pw4+r_num+"\n")
                        file.write(pw5+r_num+"\n")
                        file.write(pw6+r_num+"\n")
                        file.write(pw6+r_num+"\n")


                        file.write(r_num+pw6+"\n")
                        file.write( r_num+id +"\n")
                        file.write( r_num+ pw1+"\n")
                        file.write( r_num+ pw2)
                        file.write(r_num+pw3+"\n")
                        file.write( r_num+ pw4+"\n")
                        file.write( r_num+ pw5+"\n")
                        file.write(r_num +pw6 +"\n")
                        file.write(r_num + r_num + "\n")

                        file.write(r_num + pw6+"\n")

                print(ran + "\nSaved in passswords.txt")


        else:

                print(ran + "\n\t\tWait it might take some seconds- - - - - -")
                file = open("passwords.txt", "a+")
                file.write(id + id + "\n")
                for i in range(amount):
                            r_num = random.randint(1000, 9999)
                            r_num = str(r_num)
                            file = open("passwords.txt", "a+")
                            file.write(id + r_num + "\n")
                            file.write(r_num + r_num + "\n")

                            file.write(r_num+id + "\n")

                print(ran + "\nSaved in passswords.txt")

def view():
    file = open("passwords.txt","r")
    read = file.read()
    print(ran + "\n\t\tRESULTS: \n")

    print(all_col[2%6] + read)

cont =" "
while cont != "n" and "no":
    print(Fore.LIGHTYELLOW_EX + "\n\t\t[1] Generate Passwords\n\t\t[2] View Generated passwords\n\t\t[3] About BruteGenV1.0\n\t\t[4] Exit\n ")

    choice = input(ran + "\nEnter your choice: ")
    if choice == "1":
       program()

    elif choice == "2":
       view()
    elif choice == "3":
       print(ran, pyfiglet.figlet_format("\t\t\t    BRUTEGEN"))
       print(ran + "\t\t        V_1.0\t\n\n")
       print(Style.BRIGHT + Fore.LIGHTYELLOW_EX, "\n\t    ", "- " * 3, "BY PARADOX-KYUU ", "- " * 3)
       print("\n\t   CREATORS:\n")
       print(Style.BRIGHT + Fore.LIGHTRED_EX, "\n", "- " * 4, " Github: https://github.com/paradox-kyuu/ ", "- " * 3)
       print(Style.BRIGHT + Fore.LIGHTCYAN_EX, "\n", "- " * 4, " Special Thanks to for the src code : Cyber_Dioxide | https://github.com/Cyber-Dioxide/ ", "- " * 4)	
       
    elif choice == "4":
    	print("\n\t	   EXITTING BRUTEGEN")
    	exit()
    else:
        print(ran + "\nInvalid option")
        exit()
    cont = input(ran + "\nDo you want to continue? [y/n]:")

    if cont == "y":
        os.system("clear")
        banner()

