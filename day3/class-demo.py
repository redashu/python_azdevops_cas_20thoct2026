class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print("Employee:", self.name)
        print("Salary:", self.salary)

    def calculate_bonus(self):
        return self.salary * 0.10


def main():
    emp = Employee("Amit", 50000)

    emp.display_details()

    bonus = emp.calculate_bonus()
    print("Bonus:", bonus)


if __name__ == "__main__":
    main()