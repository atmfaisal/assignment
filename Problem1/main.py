import sqlite3

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

sql_command = """
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS subject;

CREATE TABLE student (
    id INTEGER,
    name VARCHAR,
    current_class INTEGER,
    status INTEGER DEFAULT 1,
    PRIMARY KEY(id));

CREATE TABLE subject (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject VARCHAR,
    no_of_days_taught INTEGER,
    marks INTEGER);

INSERT INTO student(id, name, current_class) VALUES (1, "Abu", 8);
INSERT INTO student(id, name, current_class) VALUES (2, "Toha", 9);
INSERT INTO student(id, name, current_class) VALUES (3, "Muhammad", 10);
INSERT INTO student(id, name, current_class) VALUES (4, "Faisal", 8);
INSERT INTO student(id, name, current_class) VALUES (5, "Rajib", 9);
INSERT INTO student(id, name, current_class) VALUES (6, "Ahmed", 10);
INSERT INTO student(id, name, current_class) VALUES (7, "Hemel", 8);
INSERT INTO student(id, name, current_class) VALUES (8, "Sabbir", 9);

INSERT INTO subject(student_id, subject, no_of_days_taught, marks) VALUES (1, "math", 10, 95);
INSERT INTO subject(student_id, subject, no_of_days_taught, marks) VALUES (1, "english", 20, 90);
INSERT INTO subject(student_id, subject, no_of_days_taught, marks) VALUES (1, "bangla", 30, 85);
INSERT INTO subject(student_id, subject, no_of_days_taught, marks) VALUES (2, "math", 20, 80);
INSERT INTO subject(student_id, subject, no_of_days_taught, marks) VALUES (3, "english", 20, 90);
INSERT INTO subject(student_id, subject, no_of_days_taught, marks) VALUES (4, "bangla", 20, 70);
INSERT INTO subject(student_id, subject, no_of_days_taught, marks) VALUES (5, "math", 20, 90);
INSERT INTO subject(student_id, subject, no_of_days_taught, marks) VALUES (6, "english",20, 80);
INSERT INTO subject(student_id, subject, no_of_days_taught, marks) VALUES (7, "bangla", 20, 90);
INSERT INTO subject(student_id, subject, no_of_days_taught, marks) VALUES (7, "math", 20, 90);
INSERT INTO subject(student_id, subject, no_of_days_taught, marks) VALUES (8, "english", 20, 90);
INSERT INTO subject(student_id, subject, no_of_days_taught, marks) VALUES (8, "bangla", 20, 90);
INSERT INTO subject(student_id, subject, no_of_days_taught, marks) VALUES (8, "math", 20, 90);
"""

cur.executescript(sql_command)
conn.commit()


def __show_operations():
    print()
    operations = ["0 : Exit", "1 : Add a Student", "2 : Edit a Student", "3 : Delete a Student", "4 : See the List of Students Individually", "5 : See Overall Info"]
    for operation in operations:
        print(operation)


def __show_operations_for_edit():
    operations = ["1 : Adding days to the number of days taught", "2 : Adding marks"]
    for operation in operations:
        print(operation)


def __show_operations_for_see():
    operations = ["1 : Specific Class", "2 : Individual Student"]
    for operation in operations:
        print(operation)


def __show_operations_for_overall():
    operations = ["1 : Total Days Taught Across All Class", "2 : Individual Days Taught in Each Class", "3 : Total Earnings", "4 : Individual Earnings of Each Class", "5: Individual Earnings of Each Subject", "6 : Average Marks of All Students"]
    for operation in operations:
        print(operation)


def get_operation_id():
    __show_operations()
    operation_id = input("\nEnter Operation ID: ")
    return operation_id


def get_operation_id_for_edit():
    __show_operations_for_edit()
    operation_id = input("\nEnter Operation ID: ")
    return operation_id


def get_operation_id_for_see():
    __show_operations_for_see()
    operation_id = input("\nEnter Operation ID: ")
    return operation_id


def get_operation_id_for_overall():
    __show_operations_for_overall()
    operation_id = input("\nEnter Operation ID: ")
    return operation_id


def add_a_student():
    current_class = input("Enter Class :: 8, 9 or 10: ")
    name = input("Enter Name: ")
    cur.execute("INSERT INTO student (name, current_class) VALUES (?,?)", (name, current_class))
    conn.commit()
    print("New Student Added\n")
    return


def adding_no_of_days_taught():
    student_id = input("Enter ID:  ")
    sub = input("Enter Subject: 'math','english', 'bangla':  ")
    days = input("Enter Number Days Taught:  ")
    cur.execute("UPDATE subject SET no_of_days_taught=? WHERE id =? and subject=?", (days, student_id, sub))
    if cur.rowcount < 1:
        cur.execute("INSERT INTO subject (student_id, subject, no_of_days_taught) VALUES (?,?,?)", (student_id, sub, days))
    conn.commit()
    return


def adding_marks():
    student_id = input("Enter ID:  ")
    sub = input("Enter Subject: 'math','english', 'bangla':  ")
    mark = input("Enter Marks:  ")
    cur.execute("UPDATE subject SET marks=? WHERE id =? and subject=?", (mark, student_id, sub))
    if cur.rowcount < 1:
        cur.execute("INSERT INTO subject (student_id, subject, marks) VALUES (?,?,?)", (student_id, sub, mark))
    conn.commit()
    return


def edit_a_student():
    operation_id = get_operation_id_for_edit()
    if operation_id == '1':
        adding_no_of_days_taught()
    elif operation_id == '2':
        adding_marks()
    else:
        print("Invalid Operation ID! Try Again...")
        edit_a_student()


def delete_a_student():
    cur.execute("SELECT id, name, current_class FROM student WHERE status=1 ")
    col = list(map(lambda x: x[0], cur.description))
    print(col)
    stu_data = cur.fetchall()
    print(*stu_data, sep='\n')
    user_input = input("Enter ID Which You Want to Delete: ")
    cur.execute("UPDATE student SET status=0 WHERE id =?", user_input)
    conn.commit()
    return


def specific_class():
    user_input = input("Choose a Specific Class 8, 9 or 10: ")
    cur.execute("SELECT name, SUM(no_of_days_taught), AVG(marks) FROM student stu INNER JOIN subject sub ON stu.id=sub.student_id and current_class=? GROUP BY stu.id", user_input)
    specific = cur.fetchall()
    print(*specific, sep='\n')
    return


def individual_student():
    cur.execute("SELECT id, name, current_class FROM student WHERE status='1'")
    col = list(map(lambda x: x[0], cur.description))
    print(col)
    stu_data = cur.fetchall()
    print(*stu_data, sep='\n')
    user_input = input("Enter an ID: ")
    cur.execute("SELECT * FROM subject WHERE student_id=?", user_input)
    col = list(map(lambda x: x[0], cur.description))
    print(col)
    stu_data = cur.fetchall()
    print(*stu_data, sep='\n')
    return


def see_the_list_of_students_individually():
    operation_id = get_operation_id_for_see()
    if operation_id == '1':
        specific_class()
    elif operation_id == '2':
        individual_student()
    else:
        print("Invalid Operation ID! Try Again...")
        edit_a_student()


def total_days_taught_across_all_class():
    cur.execute("SELECT SUM(no_of_days_taught) FROM subject")
    total_days = cur.fetchone()
    print(*total_days, sep='\n')


def individual_days_taught_in_each_class():
    cur.execute("SELECT current_class, SUM(no_of_days_taught) FROM student stu INNER JOIN subject sub ON stu.id=sub.student_id GROUP BY current_class")
    total_days = cur.fetchall()
    print(*total_days, sep='\n')


def total_earnings():
    cur.execute("SELECT SUM(no_of_days_taught) FROM subject")
    total_earning = cur.fetchone()
    print("The total earnings: ")
    print(*total_earning, sep='\n')


def individual_earnings_of_each_class():
    cur.execute("SELECT current_class, SUM(no_of_days_taught) FROM student stu INNER JOIN subject sub ON stu.id=sub.student_id GROUP BY current_class")
    earnings = cur.fetchall()
    print(*earnings, sep='\n')


def individual_earnings_of_each_subject():
    cur.execute("SELECT subject, SUM(no_of_days_taught) FROM subject GROUP BY subject")
    earnings = cur.fetchall()
    print(*earnings, sep='\n')


def average_marks_of_all_students():
    cur.execute("SELECT  ROUND(AVG(marks),2) FROM subject")
    avg_marks = cur.fetchone()
    print(*avg_marks, sep='\n')


def see_overall_info():
    operation_id = get_operation_id_for_overall()
    if operation_id == '1':
        total_days_taught_across_all_class()
    elif operation_id == '2':
        individual_days_taught_in_each_class()
    elif operation_id == '3':
        total_earnings()
    elif operation_id == '4':
        individual_earnings_of_each_class()
    elif operation_id == '5':
        individual_earnings_of_each_subject()
    elif operation_id == '6':
        average_marks_of_all_students()
    else:
        print("Invalid Operation ID! Try Again...")
        see_overall_info()


if __name__ == '__main__':
    while True:
        user_operation = get_operation_id()
        if user_operation == '0':
            break
        elif user_operation == '1':
            add_a_student()
        elif user_operation == '2':
            edit_a_student()
        elif user_operation == '3':
            delete_a_student()
        elif user_operation == '4':
            see_the_list_of_students_individually()
        elif user_operation == '5':
            see_overall_info()
        else:
            print("Invalid Operation ID! Try Again...\n")
