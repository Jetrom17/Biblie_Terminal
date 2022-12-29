import os
from colorama import init, Fore, Style
os.system("pip install colorama")
def menu():

    print("""
 ________  ___  ________  ___       _______      
|\   __  \|\  \|\   __  \|\  \     |\  ___ \     
\ \  \|\ /\ \  \ \  \|\ /\ \  \    \ \   __/|    
 \ \   __  \ \  \ \   __  \ \  \    \ \  \_|/__  
  \ \  \|\  \ \  \ \  \|\  \ \  \____\ \  \_|\ \ 
   \ \_______\ \__\ \_______\ \_______\ \_______\
    \|_______|\|__|\|_______|\|_______|\|_______|  
========================================
Por: Jetrom
Github: Jetrom17
Version 1.0
----
🤖 Queira contribuir: https://github.com/Jetrom17/TabNews_Terminal.git
----
==========================================
00. E-mail para sugestões
==========================================
1. Biblia Sagrada pt-br
2. Holy Bible en
999. Baixar ferramenta "links"
==========================================
x. SAIR
==========================================
""")

loop = True

while loop:
    menu()
    what = input("#: ")
    if what == "00":
        print("================================")
        print("Você terá meu contato via e-mail. Meu provedor não é Google e nem Protonmail.")
        print("----------------")
        hm = input("Tem certeza que queres meu contato via e-mail? (y/n): ")
        print("================================")
        if hm == "y":
            print("========================================================")
            repo = input("Opa! Antes te dá meu e-mail, posso atualizar e dá upgrade em seu repositório, se disponível? (y,n): ")
            if repo == "y":
                print("========================================================")
                os.system("apt update -y")
                os.system("apt upgrade -y")
                os.system("clear")
                print(Fore.GREEN + "📩 Jetrom@mail2tor.com")
                print("========================================")
                print("[+] Repositórios supostamente atualizados")
                print("[+] Dado upgrade")
                print('''
 .----------------. 
| .--------------. |
| |      _       | |
| |     | |      | |
| |  ___| |___   | |
| | |___   ___|  | |
| |     | |      | |
| |     |_|      | |
| |              | |
| '--------------' |
 '----------------'                 
''')
                print("Agora você tem super bible!")
                print("========================================")
            else:
                rmenu = input("Cancelado, voltar ao menu? (y/n): ")
                if rmenu == "y":
                    menu()
    elif what == "1":
        os.system("less AA.txt")
        rmenu = input("Voltar ao menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "2":
        os.system("less ACV.txt")
        rmenu = input("Voltar ao menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "999":
        os.system("apt install links -y")
        rmenu = input("Voltar ao menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "x":
        print("Tchau!")
        break
