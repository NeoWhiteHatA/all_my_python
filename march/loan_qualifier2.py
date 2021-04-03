MIN_SALARY = 30000.0#MIN PAYMENT IN YEARS
MIN_YEARS = 2#MIN SKILL IN YOUR JOB

salary = float(input())
years_job = int(input())

if salary >= MIN_SALARY and years_job >= MIN_YEARS:
    print('So good')
else:
    print('Bad')