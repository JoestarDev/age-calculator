import datetime
now=datetime.datetime.now()
def get_valid_year():
    while True:
        birth_year=int(input("Please enter your birthyear: "))
        if (now.year-120)<=birth_year<=now.year:
            return birth_year 
        else:
            print("This year is inconvenient! Please try again")
def get_valid_month(year):
    while True:
        birth_month=int(input("Please enter your birthmonth: "))
        try:
            datetime.date(year,birth_month,1)
            return birth_month
        except ValueError:
            print("This month is inconvenient! Please try again")
def get_valid_day(year,month):
    while True:
        birth_day=int(input("Please enter your birthday: "))
        try:
            datetime.date(year,month,birth_day)
            return datetime.date(year,month,birth_day)
        except ValueError:
            print("This combinaision is inconvinient! Please try again")
birth_year=get_valid_year()
birth_month=get_valid_month(birth_year)
birth_day=get_valid_day(birth_year,birth_month)
age=now.year-birth_day.year
had_birthday=(birth_month,birth_day.day)<=(now.month,now.day)
if not had_birthday:
    age=age-1
if age<18:
    print("Your age is "+str(age)+" and you are a minor")
else:
    print("Your age is "+str(age)+" and you are an adult")   
print("Thank you for your information")
input("Press enter to exit")
    
