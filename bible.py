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
🤖 Queira contribuir: https://github.com/Jetrom17/Biblie_Terminal
----
==========================================
00. E-mail para sugestões
==========================================
1. Bíblia pt-br (offline)
2. Bible4u
3. Bible en (offline)
4. A Bíblia Digital (API)
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
        os.system("links https://bible4u.app/bible.html")
        rmenu = input("Voltar ao menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "3":
        os.system("less ACV.txt")
        rmenu = input("Voltar ao menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "4":
        print("https://www.abibliadigital.com.br/")
        print("")
        print('''
        Get Books - returns list of 66 bible books

Endpoint: GET https://www.abibliadigital.com.br/api/books

Authenticated:

No - Limit rate of 20 requests per hour
Yes - Unlimited
[
  {
    "abbrev": {"pt":"gn","en":"gn"},
    "author":"Moisés",
    "chapters":50,
    "group":"Pentateuco",
    "name":"Gênesis",
    "testament":"VT"
  },
  {
    "abbrev": {"pt":"ex","en":"ex"},
    "author":"Moisés",
    "chapters":40,
    "group":"Pentateuco",
    "name":"Êxodo",
    "testament":"VT"
  },
  ...
]
        ''')
        break
        print
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
        print("Tchau! 👋")
        break
