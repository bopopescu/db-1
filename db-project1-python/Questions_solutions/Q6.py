import db
import logging
import traceback
import log_main


log_main.initialize_logger("Q6")


def q6_1():
    try:
        query = "DELETE FROM `EMPLOYEE` WHERE SSN=%s"

        data = ('444444400')
        print(db.delete_query(query, data))
        logging.info(str(query) + " " + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in DELETE_DATA: %s', e)
