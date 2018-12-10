import db
import log_main
import logging
import traceback

log_main.initialize_logger("Dept_Locations")


def insert_data():
    try:
        query = "INSERT INTO DEPT_LOCATIONS (Dnumber, Dlocation) VALUES (%s, %s)"

        # 1
        data = (1, 'Houston')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 2
        data = (4, 'Stafford')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 3
        data = (5, 'Bellaire')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 4
        data = (5, 'Sugarland')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 5
        data = (5, 'Houston')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 6
        data = (6, 'Atlanta')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 7
        data = (6, 'Sacramento')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 8
        data = (7, 'Milwaukee')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 9
        data = (8, 'Chicago')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 10
        data = (8, 'Dallas')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 11
        data = (8, 'Philadephia')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 12
        data = (8, 'Seattle')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 13
        data = (8, 'Miami')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 14
        data = (9, 'Arlington')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 15
        data = (11, 'Austin')
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in INSERT_DATA: %s', e)


insert_data()
