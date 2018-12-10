import db
import log_main
import logging
import traceback

log_main.initialize_logger("Project")


def insert_data():
    try:
        query = "INSERT INTO PROJECT (Pname, Pnumber, Plocation, Controlling_department) VALUES (%s, %s, %s, %s)"

        # 1
        data = ('EntityAnnot', 4, 'Houston', 5)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 2
        data = ('Analysis', 5, 'Sacramento', 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 3
        data = ('EventManagement', 6, 'Sacramento', 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 4
        data = ('FoodDistribution', 7, 'Sacramento', 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 5
        data = ('Computerization', 10, 'Stafford', 4)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 6
        data = ('ConfigMgmt', 11, 'Atlanta', 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 7
        data = ('DataMining', 13, 'Sacramento', 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 8
        data = ('Reorganization', 20, 'Houston', 1)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 9
        data = ('Benefits', 30, 'Stafford', 4)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 10
        data = ('OperatingSystem', 61, 'Sacramento', 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 11
        data = ('DatabaseSystems', 62, 'Atlanta', 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 12
        data = ('Middleware', 63, 'Atlanta', 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 13
        data = ('Advertizing', 70, 'Arlington', 9)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 14
        data = ('InkjetPrinters', 91, 'Milwaukee', 7)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 15
        data = ('LaserPrinters', 92, 'Milwaukee', 7)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 16
        data = ('HumanResource', 95, 'Arlington', 9)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 17
        data = ('SearchEngine', 22, 'Arlington', 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 18
        data = ('MotherBoard', 29, 'Milwaukee', 7)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in INSERT_DATA: %s', e)


insert_data()
