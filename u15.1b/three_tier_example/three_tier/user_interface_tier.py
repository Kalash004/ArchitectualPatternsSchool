class ConsoleUserInterface:

    def __init__(self, line_length):
        self.line_length = line_length
        self.application = None

    def print_line(self, symbol="="):
        print(symbol * self.line_length)

    def print_message(self, message):
        self.print_line()
        print(message)

    def print_task_list(self, task_list):
        self.print_line()
        print("Seznam úkolů:")
        i = 0
        for task in task_list:
            i += 1
            print("\t" + str(i) + ". " + task.strip())
        if (i == 0):
            print("\t(žádné úkoly)")

    def new_task_input(self):
        self.print_line()
        new_task = None
        while (new_task == None):
            new_task = input("Zadejte nový úkol: ").strip()
            if (len(new_task) < 1):
                print("Neplatné zadání musíte zadat nějaký text")
                new_task = None
        return new_task

    def remove_first_task(self) -> bool:
        return self.ask_for_removal_premission("Are you sure you want to remove first task")

    def ask_for_removal_premission(self, message) -> bool:
        print(message)
        choice = None
        while choice is None:
            try:
                choice = input("Y/n: ").lower()
                if choice not in ("y", "n", "yes", "no"):
                    raise Exception()
            except:
                choice = 0
                print("Please write Y for yes or N for no")
        return self.check_choice(choice)

    def menu_input(self):
        commands = [
            ("Vypsat seznam", self.application.show_task_list),
            ("Přidat na seznam", self.application.add_task),
            ("Smazat celý seznam", self.application.remove_task_list),
            ("Ukončit program", self.application.terminate),
            ("Show first task", self.application.show_first_task),
            ("Remove first task", self.application.remove_first_task)
        ]

        self.print_line()
        print("Vyberte příkaz:")
        num = 0
        for label, action in commands:
            num += 1
            print("\t" + str(num) + ". " + label)

        choosen_num = None
        while (choosen_num == None):
            choosen_num = input("Zadejte číslo příkazu (1-" + str(len(commands)) + "): ").strip()
            try:
                choosen_num = int(choosen_num)
                if (not 0 < choosen_num <= len(commands)):
                    raise Exception()
            except:
                print("Neplatné zadání musíte zadat číslo mezi 1 až " + str(len(commands)))
                choosen_num = None

        return commands[choosen_num - 1][1]

    def check_choice(self, choice) -> bool:
        return choice[0] == "y"

    def remove_tasks(self) -> bool:
        return self.ask_for_removal_premission("Are you sure you want to remove all tasks")
