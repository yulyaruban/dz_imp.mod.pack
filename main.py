from datetime import date
from application.salary import calculate_salary
from application.application.db.people import get_employees



if __name__ == '__main__':
    calculate_salary()
    get_employees()