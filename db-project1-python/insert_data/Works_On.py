import db
import log_main
import logging
import traceback

log_main.initialize_logger("Works_On")


def insert_data():
    try:
        query = "INSERT INTO WORKS_ON (Essn, Pno, Hours) VALUES (%s, %s, %s)"

        # 1
        data = ('123456789', 5, 32.5)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 2
        data = ('123456789', 6, 7.5)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 3
        data = ('666884444', 7, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 4
        data = ('453453453', 5, 20.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 5
        data = ('453453453', 6, 20.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 6
        data = ('333445555', 7, 10.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 7
        data = ('333445555', 7, 10.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 8
        data = ('333445555', 10, 10.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 9
        data = ('333445555', 20, 10.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 10
        data = ('242535609', 70, 20.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 11
        data = ('242535609', 62, 20.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 12
        data = ('999887777', 30, 30.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 13
        data = ('999887777', 10, 10.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 14
        data = ('987987987', 10, 35.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 15
        data = ('987987987', 30, 5.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 16
        data = ('987654321', 30, 20.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 17
        data = ('987654321', 20, 15.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 18
        data = ('888665555', 20, 5.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 19
        data = ('111111100', 61, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 20
        data = ('111111101', 61, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 21
        data = ('111111102', 61, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 22
        data = ('111111103', 61, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 23
        data = ('222222200', 62, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 24
        data = ('222222201', 62, 48.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 25
        data = ('222222202', 62, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 26
        data = ('222222203', 62, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 27
        data = ('222222204', 62, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 28
        data = ('222222205', 62, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 29
        data = ('333333300', 63, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 30
        data = ('333333301', 63, 46.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 31
        data = ('444444400', 91, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 32
        data = ('444444401', 91, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 33
        data = ('444444402', 91, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 34
        data = ('444444403', 91, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 35
        data = ('555555500', 92, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 36
        data = ('555555501', 92, 44.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 37
        data = ('666666601', 91, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 38
        data = ('666666603', 91, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 39
        data = ('666666604', 91, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 40
        data = ('666666605', 92, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 41
        data = ('666666606', 91, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 42
        data = ('666666607', 61, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 43
        data = ('666666608', 62, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 44
        data = ('666666609', 63, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 45
        data = ('666666610', 61, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 46
        data = ('666666611', 61, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 47
        data = ('666666612', 61, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 48
        data = ('666666613', 61, 30.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 49
        data = ('666666613', 62, 10.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 50
        data = ('666666613', 63, 10.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 51
        data = ('999999999', 5, 2.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 52
        data = ('999999999', 6, 2.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 53
        data = ('999999999', 7, 4.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 54
        data = ('999999999', 10, 4.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 55
        data = ('999999999', 20, 4.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 56
        data = ('999999999', 30, 4.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 57
        data = ('999999999', 61, 4.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 58
        data = ('999999999', 62, 4.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 59
        data = ('999999999', 63, 4.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 60
        data = ('999999999', 70, 2.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 61
        data = ('999999999', 91, 2.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 62
        data = ('999999999', 92, 1.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 63
        data = ('999999999', 95, 3.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 64
        data = ('254937381', 70, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 65
        data = ('222333444', 91, 10.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 66
        data = ('223344667', 63, 20.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 67
        data = ('444222666', 62, 25.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 68
        data = ('112244668', 95, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 69
        data = ('343434344', 63, 40.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 70
        data = ('234234234', 95, 35.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 71
        data = ('913323708', 92, 33.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 72
        data = ('636669233', 4, 11.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 73
        data = ('614370310', 3, 45.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 74
        data = ('849934919', 95, 23.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 75
        data = ('432765098', 63, 25.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 76
        data = ('444212096', 63, 25.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 77
        data = ('913353347', 22, 30.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 78
        data = ('292740167', 5, 25.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 79
        data = ('202843824', 11, 20.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 80
        data = ('673466642', 22, 4.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 81
        data = ('101248268', 29, 10.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 82
        data = ('245239264', 11, 25.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 83
        data = ('242916639', 4, 5.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 84
        data = ('906218888', 29, 15.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 85
        data = ('001614905', 13, 18.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 86
        data = ('245239264', 10, 25.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 87
        data = ('349273344', 29, 15.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 88
        data = ('242916639', 11, 20.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 89
        data = ('214370999', 10, 35.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 90
        data = ('111422203', 4, 45.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 91
        data = ('398172999', 70, 10.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 92
        data = ('241625699', 61, 4.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 93
        data = ('245239264', 5, 5.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 94
        data = ('349273344', 6, 10.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 95
        data = ('242916639', 7, 10.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 96
        data = ('214370999', 5, 4.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 97
        data = ('111422203', 6, 5.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 98
        data = ('398172999', 7, 10.0)
        print(db.insert_query(query, data))
        logging.info(str(query) + " " + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in INSERT_DATA: %s', e)


insert_data()
