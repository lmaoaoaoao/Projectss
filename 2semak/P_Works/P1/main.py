import os
import json


# === АБСТРАКЦИЯ: базовые классы ===
class Person:
    """Абстрактный класс человека (абстракция)"""
    def __init__(self, name):
        self._name = name  # инкапсуляция: защищённое поле

    @property
    def name(self):
        return self._name



class Book:
    """Класс книги (инкапсуляция данных)"""
    def __init__(self, title, author, status="доступна"):
        self.__title = title
        self.__author = author
        self.__status = status  # "доступна" или "выдана"

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        if value in ["доступна", "выдана"]:
            self.__status = value

    def to_dict(self):
        return {
            "title": self.__title,
            "author": self.__author,
            "status": self.__status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["status"])



# === НАСЛЕДОВАНИЕ: наследники Person ===
class User(Person):
    """Пользователь библиотеки"""
    def __init__(self, name):
        super().__init__(name)
        self._borrowed_books = []  # список взятых книг

    def borrow_book(self, book):
        if book.status == "доступна":
            book.status = "выдана"
            self._borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self._borrowed_books:
            book.status = "доступна"
            self._borrowed_books.remove(book)
            return True
        return False

    def get_borrowed_books(self):
        return self._borrowed_books

    def to_dict(self):
        return {
            "name": self._name,
            "borrowed_books": [book.to_dict() for book in self._borrowed_books]
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(data["name"])
        user._borrowed_books = [Book.from_dict(b) for b in data["borrowed_books"]]
        return user


class Librarian(Person):
    """Библиотекарь (имеет расширенные права)"""
    def add_book(self, library, title, author):
        book = Book(title, author)
        library.books.append(book)

    def remove_book(self, library, title):
        for book in library.books:
            if book.title == title:
                if book.status == "доступна":
                    library.books.remove(book)
                return True
        return False

    def register_user(self, library, name):
        user = User(name)
        library.users.append(user)

    def list_all_users(self, library):
        return library.users

    def list_all_books(self, library):
        return library.books



# === ПОЛИМОРФИЗМ: единый интерфейс для сохранения ===
class DataManager:
    """Менеджер сохранения/загрузки данных"""
    @staticmethod
    def save_data(library, filename="library_data.json"):
        data = {
            "books": [book.to_dict() for book in library.books],
            "users": [user.to_dict() for user in library.users],
            "librarians": [librarian.name for librarian in library.librarians]
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def load_data(library, filename="library_data.json"):
        if not os.path.exists(filename):
            return  # файл не найден — начинаем с пустых данных

        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        library.books = [Book.from_dict(b) for b in data.get("books", [])]
        library.users = [User.from_dict(u) for u in data.get("users", [])]
        library.librarians = [Librarian(name) for name in data.get("librarians", [])]



# === ОСНОВНОЙ КЛАСС БИБЛИОТЕКИ ===
class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.librarians = [Librarian("Паладин")]  # хотя бы один библиотекарь

    def run(self):
        DataManager.load_data(self)  # загрузка данных при старте

        print("Добро пожаловать в библиотеку!")
        role = input("Выберите роль (1.библиотекарь/2.пользователь): ").strip().lower()

        if role == "1":
            self.librarian_menu()
        elif role == "2":
            self.user_menu()
        else:
            print("Неверная роль.")

        DataManager.save_data(self)  # сохранение данных при выходе
        print("Данные сохранены. До свидания!")

    def librarian_menu(self):
        name = input("Введите ваше имя: ").strip()
        librarian = next((u for u in self.librarians if u.name == name), None)

        if not librarian:
            print("Пользователь не найден. Зарегистрируйтесь через библиотекаря.")
            return

        while True:
            print("\n=== Меню библиотекаря ===")
            print("1. Добавить книгу")
            print("2. Удалить книгу")
            print("3. Зарегистрировать пользователя")
            print("4. Список всех пользователей")
            print("5. Список всех книг")
            print("0. Выход")

            choice = input("Ваш выбор: ").strip()

            if choice == "1":
                title = input("Название книги: ").strip()
                author = input("Автор: ").strip()
                librarian.add_book(self, title, author)
                print("Книга добавлена.")

            elif choice == "2":
                title = input("Название книги для удаления: ").strip()
                if librarian.remove_book(self, title):
                    print("Книга удалена.")
                else:
                    print("Книга не найдена.")

            elif choice == "3":
                name = input("Имя пользователя: ").strip()
                librarian.register_user(self, name)
                print("Пользователь зарегистрирован.")

            elif choice == "4":
                users = librarian.list_all_users(self)
                if users:
                    for u in users:
                        print(f"- {u.name}")
                else:
                    print("Нет пользователей.")

            elif choice == "5":
                books = librarian.list_all_books(self)
                if books:
                    for b in books:
                        print(f"- {b.title} ({b.author}) — {b.status}")
                else:
                    print("Книг нет.")

            elif choice == "0":
                break

            else:
                print("Неверный выбор.")

    def user_menu(self):
        name = input("Введите ваше имя: ").strip()
        user = next((u for u in self.users if u.name == name), None)

        if not user:
            print("Пользователь не найден. Зарегистрируйтесь через библиотекаря.")
            return

        while True:
            print(f"\n=== Меню пользователя ({user.name}) ===")
            print("1. Просмотреть доступные книги")
            print("2. Взять книгу")
            print("3. Вернуть книгу")
            print("4. Мои взятые книги")
            print("0. Выход")

            choice = input("Ваш выбор: ").strip()

            if choice == "1":
                available = [b for b in self.books if b.status == "доступна"]
                if available:
                    for b in available:
                        print(f"- {b.title} ({b.author})")
                else:
                    print("Нет доступных книг.")

            elif choice == "2":
                title = input("Название книги для взятия: ").strip()
                book = next((                book for book in self.books if book.title == title), None)
                if book:
                    if user.borrow_book(book):
                        print(f"Вы взяли книгу '{book.title}'.")
                    else:
                        print(f"Книга '{book.title}' уже выдана.")
                else:
                    print("Книга не найдена.")

            elif choice == "3":
                title = input("Название книги для возврата: ").strip()
                book = next((
                    book for book in user.get_borrowed_books() if book.title == title), None)
                if book:
                    user.return_book(book)
                    print(f"Вы вернули книгу '{book.title}'.")
                else:
                    print("Вы не брали эту книгу или она не найдена.")

            elif choice == "4":
                borrowed = user.get_borrowed_books()
                if borrowed:
                    for b in borrowed:
                        print(f"- {b.title} ({b.author})")
                else:
                    print("Вы не взяли ни одной книги.")

            elif choice == "0":
                break

            else:
                print("Неверный выбор.")



# === ЗАПУСК ПРИЛОЖЕНИЯ ===
if __name__ == "__main__":
    library = Library()
    library.run()
