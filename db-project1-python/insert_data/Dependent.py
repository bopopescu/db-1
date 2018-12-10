import db
import log_main
import logging
import traceback

log_main.initialize_logger("Dependent")


def insert_data():
    try:
        query = "INSERT INTO DEPENDENT (Essn, Dependent_name, Sex, Birth_date, Relationship) " \
                "VALUES (%s, %s, %s, STR_TO_DATE(%s,'%d-%b-%Y'), %s)"

        # 1
        data = ('888665151', 'Mary Alice', 'F', '10-NOV-1924', 'Spouse')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 2
        data = ('444444400', 'Kathy', 'F', '09-OCT-1944', 'Spouse')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 3
        data = ('999887777', 'John Smith', 'M', '19-JUL-1956', 'Spouse')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 4
        data = ('987987987', 'Khadeja Begum', 'F', '29-MAR-1949', 'Spouse')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 5
        data = ('987987987', 'Jalil Ahmad', 'M', '29-MAR-1929', 'Children')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 6
        data = ('222222200', 'Jay Wallis', 'M', '16-JAN-1956', 'Spouse')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 7
        data = ('222222202', 'Mindy Vile', 'F', '21-JUN-1942', 'Spouse')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 8
        data = ('222222202', 'Amenda Vile', 'F', '21-JUN-1914', 'Children')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 9
        data = ('222222204', 'Amy Vos', 'F', '11-NOV-1963', 'Spouse')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 10
        data = ('222222204', 'james Vos', 'M', '11-NOV-1937', 'Children')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 11
        data = ('444444401', 'William Bayes', 'M', '19-JUN-1954', 'Spouse')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 12
        data = ('444444401', 'Amy Bayes', 'F', '18-JUN-1926', 'Children')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 13
        data = ('444444401', 'Tom Bayes', 'M', '20-JUN-1926', 'Children')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 14
        data = ('666666601', 'Mary Jarvice', 'F', '14-JAN-1964', 'Spouse')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 15
        data = ('666666602', 'Bond King', 'M', '16-APR-1964', 'Spouse')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 16
        data = ('666666604', 'Monia King', 'F', '01-JAN-1955', 'Spouse')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 17
        data = ('666666605', 'Aly Kramer', 'F','22-AUG-1961', 'Spouse')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 18
        data = ('666666606', 'Chistina King', 'F', '16-AUG-1948', 'Spouse')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 19
        data = ('666666607', 'Alex Small', 'F','15-MAY-1960', 'Spouse')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 20
        data = ('666666608', 'Katherin Head', 'F', '19-MAY-1964', 'Spouse')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 21
        data = ('666666608', 'Monica Head', 'F', '19-MAY-1937', 'Children')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 22
        data = ('666666608', 'Rachel Head', 'M', '18-MAY-1937', 'Children')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in INSERT_DATA: %s', e)


insert_data()
