import db
import logging
import traceback
import log_main


log_main.initialize_logger("Q3")


def q3_1():
    try:
        query = "SELECT * FROM EMPLOYEE WHERE Lname='Jones' OR Lname='James'"

        result = db.read_query(query)
        print(result)
        logging.info('Query: ' + str(query) + '\nResult: ' + str(result))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in SELECT_DATA: %s', e)


def q3_2():
    try:
        query = "SELECT * FROM EMPLOYEE WHERE Fname='Kim' OR Fname='Wilson'"

        result = db.read_query(query)
        print(result)
        logging.info('Query: ' + str(query) + '\nResult: ' + str(result))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in SELECT_DATA: %s', e)


def q3_3():
    try:
        query = "SELECT e.Name, e.SSN, SUM(w.Hours) FROM EMPLOYEE e, WORKS_ON w WHERE e.SSN = w.Essn GROUP BY w.Essn " \
                "HAVING COUNT(*) > 1"

        result = db.read_query(query)
        print(result)
        logging.info('Query: ' + str(query) + '\nResult: ' + str(result))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in SELECT_DATA: %s', e)


def q3_4():
    try:
        query = "SELECT p.Pname, p.Pnumber, p.Plocation, COUNT(w.Essn) as `Number of Employee` FROM PROJECT p, " \
                "WORKS_ON w WHERE p.Pnumber = w.Pno GROUP BY w.Pno"

        result = db.read_query(query)
        print(result)
        logging.info('Query: ' + str(query) + '\nResult: ' + str(result))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in SELECT_DATA: %s', e)


def q3_5():
    try:
        query = "SELECT e.SSN, e.Fname, e.Lname, p.Pname, p.Pnumber, w.Hours FROM EMPLOYEE e, PROJECT p, WORKS_ON w " \
                "WHERE e.DEPARTMENT = 5 AND SSN IN (SELECT w.Essn FROM WORKS_ON w WHERE w.Pno IN " \
                "(SELECT p.Pnumber FROM PROJECT p WHERE p.Controlling_department = 5 AND p.Plocation = 'Houston')) " \
                "AND e.SSN = w.Essn AND p.Pnumber = w.Pno"

        result = db.read_query(query)
        print(result)
        logging.info('Query: ' + str(query) + '\nResult: ' + str(result))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in SELECT_DATA: %s', e)


def q3_6():
    try:
        query = "SELECT Fname, Lname FROM EMPLOYEE WHERE SSN IN (SELECT Essn FROM WORKS_ON " \
                "GROUP BY Essn HAVING SUM(Hours) > 40)"

        result = db.read_query(query)
        print(result)
        logging.info('Query: ' + str(query) + '\nResult: ' + str(result))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in SELECT_DATA: %s', e)


def q3_7():
    try:
        query = "SELECT e1.Fname, e1.Lname, (SELECT COUNT(SSN) FROM EMPLOYEE e WHERE e.Supervisor=e1.SSN) " \
                "as `Number of employees supervised` FROM EMPLOYEE e1 where e1.SSN IN (SELECT Supervisor " \
                "FROM EMPLOYEE WHERE Supervisor IS NOT NULL)"

        result = db.read_query(query)
        print(result)
        logging.info('Query: ' + str(query) + '\nResult: ' + str(result))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in SELECT_DATA: %s', e)


def q3_8():
    try:
        query = "SELECT e.Name, SUM(Hours) AS `Total Hours` FROM EMPLOYEE e, WORKS_ON w WHERE e.SSN = w.Essn " \
                "GROUP BY w.Essn"

        result = db.read_query(query)
        print(result)
        logging.info('Query: ' + str(query) + '\nResult: ' + str(result))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in SELECT_DATA: %s', e)


def q3_9():
    try:
        query = "SELECT e.Name, COUNT(d.Essn) AS `Total dependents` FROM EMPLOYEE e, DEPENDENT d " \
                "WHERE e.SSN = d.Essn GROUP BY d.Essn HAVING COUNT(d.Essn) > 2"

        result = db.read_query(query)
        print(result)
        logging.info('Query: ' + str(query) + '\nResult: ' + str(result))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in SELECT_DATA: %s', e)


def q3_10():
    try:
        query = "SELECT e.Name, COUNT(d.Essn) AS `Total dependents` FROM EMPLOYEE e, DEPENDENT d " \
                "WHERE e.SSN = d.Essn AND d.Relationship = 'Children' GROUP BY d.Essn HAVING COUNT(d.Essn) > 1"

        result = db.read_query(query)
        print(result)
        logging.info('Query: ' + str(query) + '\nResult: ' + str(result))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in SELECT_DATA: %s', e)


def q3_11():
    try:
        query = "SELECT Fname, Lname FROM EMPLOYEE WHERE Department IN (SELECT Dnumber FROM DEPT_LOCATIONS " \
                "WHERE Dlocation = 'Atlanta')"

        result = db.read_query(query)
        print(result)
        logging.info('Query: ' + str(query) + '\nResult: ' + str(result))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in SELECT_DATA: %s', e)


def q3_12():
    try:
        query = "SELECT d.Dnumber, p.Pnumber, p.Pname FROM DEPT_LOCATIONS d, PROJECT p WHERE d.Dlocation = 'Houston' " \
                "AND p.Controlling_department = d.Dnumber"

        result = db.read_query(query)
        print(result)
        logging.info('Query: ' + str(query) + '\nResult: ' + str(result))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in SELECT_DATA: %s', e)


q3_1()
