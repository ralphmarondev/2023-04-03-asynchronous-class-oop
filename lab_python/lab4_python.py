# Ralph Maron Eda
# BSCPE-2A
# 2023-04-03
# Write a program that will check the employees years in service
# and office. The user will input number of years and in service
# and the following offices [it, acct, hr]
def get_salary(service : str, year : int):
    IT = 5000
    ACCT = 6000
    HR = 7500

    if service == "IT":
        return IT if year < 10 else IT * 2
    if service == "ACCT":
        return ACCT if year < 10 else ACCT * 2
    if service == "HR":
        return HR if year < 10 else HR * 2


def main():
    type_of_service = input("Enter type of service [IT, ACCT, HR]: ")
    years_of_service = int(input("Enter year of service: "))

    print(f"Salary: {get_salary(type_of_service.upper(), years_of_service)}")


if __name__ == "__main__":
    main()
