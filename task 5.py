import hashlib

class UserAuthenticator:
    def __init__(self, initial_users=None):
        """
        Ініціалізує об'єкт для аутентифікації користувачів.

        Args:
            initial_users (dict, optional): Початковий словник користувачів,
                де ключі - логіни, а значення - словники з ключами
                "hashed_password" (захешований пароль) та "full_name" (повне ПІБ).
                За замовчуванням None.
        """
        if initial_users is None:
            self.users = {}
        else:
            self.users = initial_users.copy()

    def register_user(self, login, password, full_name):
        """
        Реєструє нового користувача.

        Args:
            login (str): Логін користувача.
            password (str): Пароль користувача (буде захешований).
            full_name (str): Повне ПІБ користувача.
        """
        if login in self.users:
            print(f"Помилка: Користувач з логіном '{login}' вже існує.")
        else:
            hashed_password = self._hash_password(password)
            self.users[login] = {"hashed_password": hashed_password, "full_name": full_name}
            print(f"Користувач '{login}' успішно зареєстрований.")

    def _hash_password(self, password):
        """
        Хешує пароль за допомогою алгоритму MD5.

        Args:
            password (str): Пароль для хешування.

        Returns:
            str: Захешований пароль у шістнадцятковому форматі.
        """
        hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
        return hashed_password

    def verify_password(self, login):
        """
        Перевіряє введений користувачем пароль.

        Args:
            login (str): Логін користувача.

        Returns:
            bool: True, якщо пароль введено правильно, False - якщо ні або користувача не знайдено.
        """
        if login in self.users:
            entered_password = input(f"Введіть пароль для користувача '{login}': ")
            hashed_entered_password = self._hash_password(entered_password)
            if hashed_entered_password == self.users[login]["hashed_password"]:
                print(f"Аутентифікація успішна для користувача '{login}'.")
                print(f"Повне ім'я: {self.users[login]['full_name']}")
                return True
            else:
                print("Помилка: Неправильний пароль.")
                return False
        else:
            print(f"Помилка: Користувача з логіном '{login}' не знайдено.")
            return False

# Приклад використання:
authenticator = UserAuthenticator()

# Реєстрація користувачів
authenticator.register_user("john_doe", "password123", "Джон Доу")
authenticator.register_user("jane_smith", "securePass", "Джейн Сміт")

# Спроба реєстрації існуючого користувача
authenticator.register_user("john_doe", "anotherPass", "Джон Доу молодший")

print("\nАутентифікація користувачів:")
# Перевірка пароля
authenticator.verify_password("john_doe")
authenticator.verify_password("jane_smith")

# Спроба аутентифікації з неправильним паролем
authenticator.verify_password("john_doe")

# Спроба аутентифікації неіснуючого користувача
authenticator.verify_password("peter_pan")