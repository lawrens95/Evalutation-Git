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

        answer = input("Que voulez-vous faire ?\n")

        if answer == "1":
            print(books)
        elif answer == "2":
            bookName = input("Indiquez le nom du livre que vous souhaitez ajouter: ")
            books.append(bookName)
            print("Votre livre ", bookName, " a été ajouté avec succès.")
        elif answer == "3":
            changeBook = input("Quel est le livre que vous souhaitez modifier ?: ")
            books.remove(changeBook)
            newBook = input("Comment souhaitez-vous le renommer ?: ")
            books.append(newBook)
        elif answer == "4":
            rmBook = input("Quel livre souhaitez-vous supprimer ?: ")
            books.remove(rmBook)
            print("Le livre ", rmBook, "a été supprimé de la bibliothèque avec succès.")
        elif answer == "0":
            exit()

displayMenu()