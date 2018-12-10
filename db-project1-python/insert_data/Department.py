import db
import log_main
import logging
import traceback

log_main.initialize_logger("Department")


def insert_data():
    try:
        query = "INSERT INTO DEPARTMENT (Dname, Dnumber) VALUES (%s, %s)"

        # 1
        data = ('Research', 5)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 2
        data = ('Administration', 4)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 3
        data = ('Headquarters', 1)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 4
        data = ('Software', 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 5
        data = ('Hardware', 7)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 6
        data = ('Sales', 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 7
        data = ('HR', 9)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 8
        data = ('Networking', 3)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 9
        data = ('QA', 11)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in INSERT_DATA: %s', e)


def update_data():
    try:
        query = "UPDATE DEPARTMENT SET Manager_ssn=%s, Manager_start_date=STR_TO_DATE(%s,'%d-%b-%Y') WHERE Dnumber=%s"

        # 1
        data = ('333445555', '22-MAY-1978', 5)
        print(db.update_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 2
        data = ('987654321', '01-JAN-1985', 4)
        print(db.update_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 3
        data = ('888665555', '19-JUN-1971', 1)
        print(db.update_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 4
        data = ('111111100', '15-MAY-1999', 6)
        print(db.update_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 5
        data = ('444444400', '15-MAY-1998', 7)
        print(db.update_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 6
        data = ('555555500', '01-JAN-1997', 8)
        print(db.update_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 7
        data = ('112244668', '01-FEB-1989', 9)
        print(db.update_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 8
        data = ('110110110', '15-MAY-2009', 3)
        print(db.update_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 9
        data = ('913323708', '2-FEB-2010', 11)
        print(db.update_query(query, data))
        logging.info(str(query) + ' ' + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in UPDATE_DATA: %s', e)


# insert_data()
update_data()
