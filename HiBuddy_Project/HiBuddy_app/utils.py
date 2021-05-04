from datetime import datetime

def create_emp_code():
    return int(datetime.now().timestamp())
    
print("----------",create_emp_code())