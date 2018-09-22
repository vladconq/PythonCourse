import psycopg2
import json
from multiprocessing import Process
from multiprocessing import Pool

dict_of_name_departments = {}
answer1, answer2, answer3, answer4, answer5 = 0, 0, 0, 0, 0


def make_dict_of_name_departments():
    conn = psycopg2.connect("host=172.17.0.1 dbname=accounts user=user password=password")
    cur = conn.cursor()
    cur.execute("SELECT department_id, department_name FROM department;")
    rows = cur.fetchall()
    for row in rows:
        dict_of_name_departments[row[0]] = row[1]
    conn.commit()


# TASK 1
def task_1():
    print(1)
    conn = psycopg2.connect("host=172.17.0.1 dbname=accounts user=user password=password")
    cur = conn.cursor()
    global answer1
    cur.execute("""
    SELECT first_name, last_name
    FROM employee
    GROUP BY first_name, last_name
    HAVING COUNT(*)=
        (
        SELECT COUNT(*)
        FROM employee
        GROUP BY first_name, last_name
        HAVING COUNT(*) > 1
        ORDER BY 
          COUNT(*) DESC
        LIMIT 1
        )
    LIMIT 1
    """)

    task = cur.fetchall()
    task = task[0][0] + " " + task[0][1]
    answer1 = task
    conn.commit()
    return answer1


# TASK 2
def task_2():
    print(2)
    conn = psycopg2.connect("host=172.17.0.1 dbname=accounts user=user password=password")
    cur = conn.cursor()
    global answer2
    dict_of_city_departments = {}
    cur.execute("SELECT department_id, department_city FROM department;")
    rows = cur.fetchall()
    for row in rows:
        dict_of_city_departments[row[0]] = row[1]
    cur.execute("""
    ALTER TABLE employee ADD COLUMN IF NOT EXISTS temp_table VARCHAR(255);
    """)
    for id, city in dict_of_city_departments.items():
        cur.execute(
            "UPDATE employee SET temp_table = upper('{}') WHERE employee_department = {};".format(city, id))
    cur.execute("""
    SELECT employee_city, temp_table FROM employee
    WHERE employee_city != temp_table
    """)
    task = len(cur.fetchall())
    cur.execute("ALTER TABLE employee DROP COLUMN temp_table")
    answer2 = task
    conn.commit()
    return answer2


# TASK 3
def task_3():
    print(3)
    conn = psycopg2.connect("host=172.17.0.1 dbname=accounts user=user password=password")
    cur = conn.cursor()
    global answer3
    cur.execute("""
    SELECT first_name
        FROM employee AS e
        WHERE e.boss IS NOT NULL AND e.salary > 
            (SELECT salary FROM employee WHERE e.boss = employee_id);
    """)

    task = len(cur.fetchall())
    answer3 = task
    conn.commit()
    return answer3


# TASK 4
def task_4():
    print(4)
    conn = psycopg2.connect("host=172.17.0.1 dbname=accounts user=user password=password")
    cur = conn.cursor()
    global answer4
    global dict_of_name_departments
    avg_salary = {}
    for id, name in dict_of_name_departments.items():
        cur.execute("SELECT AVG(salary) FROM employee WHERE employee_department='{}'".format(id))
        salary = cur.fetchall()
        avg_salary[name] = salary[0][0]
    task = max(avg_salary, key=avg_salary.get)
    answer4 = task
    conn.commit()
    return answer4


# TASK 5
def task_5():
    print(5)
    conn = psycopg2.connect("host=172.17.0.1 dbname=accounts user=user password=password")
    cur = conn.cursor()
    global answer5
    global dict_of_name_departments
    dict_of_answers = {}
    for id, name in dict_of_name_departments.items():
        cur.execute("""
        SELECT COUNT(employee_department) FROM employee
        WHERE employee_department={}
        """.format(id))
        count = cur.fetchall()[0][0]

        cur.execute("""
            SELECT SUM(salary) FROM
            (SELECT SALARY FROM employee
            WHERE employee_department = {}
            ORDER BY salary
            LIMIT {} / 10) T
        """.format(id, count))
        min_task = cur.fetchall()

        cur.execute("""
            SELECT SUM(salary) FROM
            (SELECT SALARY FROM employee
            WHERE employee_department = {}
            ORDER BY salary DESC
            LIMIT {} / 10) T
        """.format(id, count))
        max_task = cur.fetchall()

        dict_of_answers[name] = float(max_task[0][0]) / float(min_task[0][0])
    value1 = max(dict_of_answers, key=dict_of_answers.get)
    dict_of_answers.pop(value1, None)
    value2 = max(dict_of_answers, key=dict_of_answers.get)
    answer5 = value1, value2
    conn.commit()
    return answer5


if __name__ == "__main__":
    make_dict_of_name_departments()

    with Pool(processes=5) as pool:
        r1 = pool.apply_async(task_1, ())
        r2 = pool.apply_async(task_2, ())
        r3 = pool.apply_async(task_3, ())
        r4 = pool.apply_async(task_4, ())
        r5 = pool.apply_async(task_5, ())

        answer1 = r1.get()
        answer2 = r2.get()
        answer3 = r3.get()
        answer4 = r4.get()
        answer5 = r5.get()

    print(json.dumps({'hw1': answer1, 'hw2': answer2, 'hw3': answer3, 'hw4': answer4, 'hw5': answer5},
                     sort_keys=True,
                     indent=4))
