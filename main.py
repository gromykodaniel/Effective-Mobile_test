from Library import LibraryClass


def main():
    library = LibraryClass()

    while True:

        print("1 - Добавить книгу")
        print("2 - Удалить книгу")
        print("3 - Поиск книги")
        print("4 - Отобразить все книги")
        print("5 - Изменить статус книги")
        print("Любое значение иначе - выход")
        a = input("ЧТо слелать: ")

        try:
            if a == "1":
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = int(input("Введите год издания книги: "))
                library.add_book(title, author, year)

            elif a == "2":
                book_id = int(input("Введите ID книги для удаления: "))
                library.delete_book(book_id)

            elif a == "3":
                key = input("Искать по (title/author/year): ").lower()
                value = input("Введите значение для поиска: ")
                if key in ["title", "author"]:
                    results = library.search_books(key, value)
                elif key == "year":
                    results = library.search_books(key, int(value))
                else:
                    print("Некорректный ключ поиска.")
                    continue
                library.display_books(results)

            elif a == "4":
                library.display_books()

            elif a == "5":
                book_id = int(input("Введите ID книги: "))
                new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
                library.update_status(book_id, new_status)

            else:
                print("Выход")
                break
        except ValueError:
            print("Ошибка ввода")


if __name__ == "__main__":
    main()
