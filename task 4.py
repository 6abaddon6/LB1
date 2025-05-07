class TaskManager:
    def __init__(self, initial_tasks=None):
        """
        Ініціалізує об'єкт системи управління задачами.

        Args:
            initial_tasks (dict, optional): Початковий словник задач,
                де ключі - назви задач, а значення - їх статус
                ("виконано", "в процесі", "очікує"). За замовчуванням None.
        """
        if initial_tasks is None:
            self.tasks = {}
        else:
            self.tasks = initial_tasks.copy()

    def add_task(self, task_name, status="очікує"):
        """
        Додає нову задачу до системи.

        Args:
            task_name (str): Назва нової задачі.
            status (str, optional): Початковий статус задачі
                ("виконано", "в процесі", "очікує"). За замовчуванням "очікує".
        """
        if task_name in self.tasks:
            print(f"Увага: Задача '{task_name}' вже існує.")
        else:
            if status in ["виконано", "в процесі", "очікує"]:
                self.tasks[task_name] = status
                print(f"Задача '{task_name}' додана зі статусом '{status}'.")
            else:
                print(f"Помилка: Неправильний статус '{status}'. Допустимі статуси: 'виконано', 'в процесі', 'очікує'.")

    def remove_task(self, task_name):
        """
        Видаляє задачу із системи.

        Args:
            task_name (str): Назва задачі для видалення.
        """
        if task_name in self.tasks:
            del self.tasks[task_name]
            print(f"Задача '{task_name}' видалена.")
        else:
            print(f"Помилка: Задача '{task_name}' не знайдена.")

    def change_task_status(self, task_name, new_status):
        """
        Змінює статус існуючої задачі.

        Args:
            task_name (str): Назва задачі, статус якої потрібно змінити.
            new_status (str): Новий статус задачі ("виконано", "в процесі", "очікує").
        """
        if task_name in self.tasks:
            if new_status in ["виконано", "в процесі", "очікує"]:
                self.tasks[task_name] = new_status
                print(f"Статус задачі '{task_name}' змінено на '{new_status}'.")
            else:
                print(f"Помилка: Неправильний статус '{new_status}'. Допустимі статуси: 'виконано', 'в процесі', 'очікує'.")
        else:
            print(f"Помилка: Задача '{task_name}' не знайдена.")

    def get_pending_tasks(self):
        """
        Повертає список задач, які мають статус "очікує".

        Returns:
            list: Список назв задач зі статусом "очікує".
        """
        pending_tasks = [task for task, status in self.tasks.items() if status == "очікує"]
        return pending_tasks

    def display_tasks(self):
        """
        Виводить на екран поточний список задач та їх статуси.
        """
        print("\nПоточний список задач:")
        if self.tasks:
            for task, status in self.tasks.items():
                print(f"- {task}: {status}")
        else:
            print("Список задач порожній.")

# Приклад використання:
task_manager = TaskManager({"Прибрати кімнату": "виконано", "Написати звіт": "в процесі"})

task_manager.display_tasks()

# Додавання задач
task_manager.add_task("Купити продукти")
task_manager.add_task("Зателефонувати клієнту", "в процесі")
task_manager.add_task("Підготувати презентацію", "очікує")
task_manager.display_tasks()

# Видалення задачі
task_manager.remove_task("Купити продукти")
task_manager.display_tasks()

# Зміна статусу задачі
task_manager.change_task_status("Написати звіт", "виконано")
task_manager.change_task_status("Підготувати презентацію", "в процесі")
task_manager.display_tasks()

# Отримання списку задач, що очікують
pending_tasks_list = task_manager.get_pending_tasks()
print("\nЗадачі, що очікують:", pending_tasks_list)

# Спроба додати задачу з неправильним статусом
task_manager.add_task("Прочитати книгу", "новий")

# Спроба змінити статус неіснуючої задачі
task_manager.change_task_status("Полити квіти", "виконано")