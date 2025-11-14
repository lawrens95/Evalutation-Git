books = []

def displayMenu():
    while True:
        print("-----------------------------------")
        print("Bienvenue dans votre librairie virtuelle")
        print("-----------------------------------")
        print("1. Lister les livres de votre bibliothèque")
        print("2. Ajouter un nouveau livre")
        print("3. Modifier un livre existant")
        print("4. Supprimer un livre")
        print("0. Quitter")

        answer = input("Que voulez-vous faire ?: \n")

        if answer == "1":
            if len (books) == 0:
                print("\nVotre bibliothèque est vide.")
            else:
                print("\nVoici votre bibliothèque:")
                for i, book in enumerate(books, start=1):
                    print(f"{i}. {book}")
            input("\nAppuyer sur entrée pour revenir au menu...")
        elif answer == "2":
            bookName = input("\nIndiquez le nom du livre que vous souhaitez ajouter: ")
            books.append(bookName)
            print(f'Votre livre "{bookName}" a été ajouté avec succès.')
            input("\nAppuyer sur entrée pour revenir au menu...")
        elif answer == "3":
            changeBook = input("\nQuel est le livre que vous souhaitez modifier ?: ")
            books.remove(changeBook)
            newBook = input("Comment souhaitez-vous le renommer ?: ")
            books.append(newBook)
            print(f'Votre livre "{changeBook}" a été renommé "{newBook}" avec succès')
            input("\nAppuyer sur entrée pour revenir au menu...")
        elif answer == "4":
            rmBook = input("\nQuel livre souhaitez-vous supprimer ?: ")
            books.remove(rmBook)
            print(f'Le livre "{rmBook}" a été supprimé de la bibliothèque avec succès.')
            input("\nAppuyer sur entrée pour revenir au menu...")
        elif answer == "0":
            exit()

displayMenu()