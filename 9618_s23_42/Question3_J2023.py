class Employee:
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle, PayYear2022):
        self.__HourlyPay = HourlyPay            # REAL
        self.__EmployeeNumber = EmployeeNumber  # STRING
        self.__JobTitle = JobTitle              # STRING
        self.__PayYear2022 = []                 # ARRAY[0:51] OF REAL

        for i in range(0, 52):
            self.__PayYear2022[i] = 0.0

Employee1 = Employee(1.1,'r','t',0.0)