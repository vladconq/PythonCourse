import psycopg2


def make_dict_of_departments():
    cur.execute("SELECT department_id, department_name FROM department;")
    rows = cur.fetchall()
    for row in rows:
        dict_of_departments[row[0]] = row[1]


dict_of_departments = {}

conn = psycopg2.connect("host=172.17.0.1 dbname=accounts user=user password=password")
cur = conn.cursor()

# INSERT DEPARTMENT.CSV
with open('DEPTS.csv', 'r') as f:
    next(f)
    cur.copy_from(f, 'department', columns=('department_name', 'department_city'), sep=',')

# INSERT EMPLOYEE.CSV
with open('EMPLOYEE.csv', 'r') as f:
    next(f)
    cur.copy_from(f, 'employee', columns=('employee_id', 'first_name', 'last_name', 'employee_department_temp',
                                          'employee_city', 'boss', 'salary'), sep=',')

# BOSS CAN CONTAIN EMPTY VALUES
cur.execute("""
UPDATE employee SET boss = NULL WHERE boss='';
ALTER TABLE employee ALTER COLUMN boss TYPE integer USING (trim(boss)::integer);
""")

# ADD NEW COLUMN WITH EMPLOYEE_DEPARTMENT
cur.execute("ALTER TABLE employee ADD COLUMN employee_department INTEGER NULL;")

# MAKE NEW COLUMN WITH EMPLOYEE_DEPARTMENT
make_dict_of_departments()
for id, depart in dict_of_departments.items():
    cur.execute(
        "UPDATE employee SET employee_department = {} WHERE employee_department_temp = '{}';".format(id, depart))

# DROP OLD COLUMN EMPLOYEE_DEPARTMENT_TEMP
cur.execute("ALTER TABLE employee DROP COLUMN employee_department_temp")

cur.execute("""
ALTER TABLE employee
ADD CONSTRAINT employee_boss_fkey
    FOREIGN KEY (boss)
    REFERENCES employee(employee_id);
""")

cur.execute("""
ALTER TABLE employee
ADD CONSTRAINT employee_employee_department_fkey
    FOREIGN KEY (employee_department)
    REFERENCES department(department_id);
""")

conn.commit()
