OVERTIME_RATE = 25
SERVICE_REWARD = 500


def calculate_overtime(overtime_hours):
    return overtime_hours * OVERTIME_RATE


def calculate_reward(years_worked):
    if years_worked > 3:
        return SERVICE_REWARD

    return 0


def calculate_gross_salary(
    basic_salary,
    allowance,
    overtime_pay,
    reward
):
    return basic_salary + allowance + overtime_pay + reward


def calculate_epf(gross_salary):
    return gross_salary * 0.11


def calculate_socso(gross_salary):
    return gross_salary * 0.005


def calculate_net_salary(gross_salary, epf, socso):
    return gross_salary - epf - socso