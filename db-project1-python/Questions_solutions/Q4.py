import db
import logging
import traceback
import log_main


log_main.initialize_logger("Q4")


def q4_1():
    try:
        query = "INSERT INTO `DEPARTMENT`(`Dname`, `Dnumber`, `Manager_ssn`, `Manager_start_date`) " \
                "VALUES (%s, %s, %s, STR_TO_DATE(%s, '%d-%b-%Y'))"
        data = ('Services', 1, '123456789', '11-AUG-2012')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in INSERT_DATA: %s', e)


def q4_2():
    try:
        query = "INSERT INTO `DEPARTMENT`(`Dname`, `Dnumber`, `Manager_ssn`, `Manager_start_date`) " \
                "VALUES (%s, %s, %s, STR_TO_DATE(%s, '%d-%b-%Y'))"
        data = ('Purchasing', 3, '990110110', '02-FEB-2013')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in INSERT_DATA: %s', e)


def q4_3():
    try:
        query = "INSERT INTO `DEPARTMENT`(`Dname`, `Dnumber`, `Manager_ssn`, `Manager_start_date`) " \
                "VALUES (%s, %s, %s, STR_TO_DATE(%s, '%d-%b-%Y'))"
        data = ('Customers', 12, '333445555', '14-JAN-2013')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in INSERT_DATA: %s', e)


def q4_4():
    try:
        query = "UPDATE DEPT_LOCATIONS SET Dnumber=%s WHERE Dlocation=%s"

        data = (9, 'Seattle')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in INSERT_DATA: %s', e)


def q4_5():
    try:
        query = "UPDATE EMPLOYEE SET Salary=%s WHERE SSN=%s"

        data = (55000, '444444444')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in INSERT_DATA: %s', e)


def q4_6():
    try:
        query = "INSERT INTO `EMPLOYEE` (Fname, Minit, Lname, SSN, Birth_date, Address, Sex, Salary, Supervisor, " \
                "Department) VALUES (%s, %s, %s, %s, STR_TO_DATE(%s, '%d-%b-%Y'), %s, %s, %s, %s, %s)"
        data = ('Jane', 'B', 'Smith', '666666606', '01-MAR-1980', '3556 W Second Street,Miami,FL', 'F', 85000,
                '666666603', 5)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in INSERT_DATA: %s', e)


def q4_7():
    try:
        query = "UPDATE WORKS_ON SET Hours=%s WHERE Pno=%s AND Essn=%s"

        data = (25, 1, '666884444')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in INSERT_DATA: %s', e)


def q4_8():
    try:
        query = "DELETE FROM EMPLOYEE WHERE SSN=%s"

        data = ('432765098')
        print(db.delete_query(query, data))
        logging.info(str(query) + " " + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in DELETE_DATA: %s', e)


def q4_9():
    try:
        query = "DELETE FROM DEPARTMENT WHERE Dnumber=%s"

        data = (9)
        print(db.delete_query(query, data))
        logging.info(str(query) + " " + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in DELETE_DATA: %s', e)


def q4_10():
    try:
        query = "DELETE FROM DEPENDENT WHERE Essn=%s"

        data = ('666666608')
        print(db.delete_query(query, data))
        logging.info(str(query) + " " + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in DELETE_DATA: %s', e)
