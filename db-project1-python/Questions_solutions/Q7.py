import db
import logging
import traceback
import log_main


log_main.initialize_logger("Q7")


def q7_1():
    try:
        query = "INSERT INTO `EMPLOYEE` (SSN, Fname, Minit, Lname, Address, Sex, Birth_date, Salary, Supervisor, " \
                "Department) VALUES (%s, %s, %s, %s, %s, %s, STR_TO_DATE(%s, '%d-%b-%Y'), %s, %s, %s)"
        data = ('1234567890', 'Dhruvi', 'R', 'Rajput', '4 ABC Street, XYZ Town 12345', 'F', '11-AUG-2012', 55000,
                '333445555', 5)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in INSERT_DATA: %s', e)


def q7_2():
    try:
        query = "INSERT INTO `WORKS_ON` (Essn, Pno, Hours) VALUES (%s, %s, %s)"
        data = ('1234567890', 4, 10.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in INSERT_DATA: %s', e)


def q7_3():
    try:
        query = "INSERT INTO `PROJECT` (Pname, Pnumber, Plocation, Controlling_department) VALUES (%s, %s, %s, %s)"
        data = ('TEST', 15, 'Dallas', 5)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in INSERT_DATA: %s', e)
