from employee import get_employee

from salary import (
    calculate_overtime,
    calculate_reward,
    calculate_gross_salary,
    calculate_epf,
    calculate_socso,
    calculate_net_salary
)

from report import print_report


def main():
    employee_data = get_employee()

    (
        name,
        employee_id,
        basic_salary,
        allowance,
        overtime_hours,
        years_worked
    ) = employee_data

    overtime_pay = calculate_overtime(overtime_hours)
    reward = calculate_reward(years_worked)

    gross_salary = calculate_gross_salary(
        basic_salary,
        allowance,
        overtime_pay,
        reward
    )

    epf = calculate_epf(gross_salary)
    socso = calculate_socso(gross_salary)

    net_salary = calculate_net_salary(
        gross_salary,
        epf,
        socso
    )

    print_report(
        name,
        employee_id,
        basic_salary,
        allowance,
        overtime_hours,
        overtime_pay,
        years_worked,
        reward,
        gross_salary,
        epf,
        socso,
        net_salary
    )


if __name__ == "__main__":
    main()