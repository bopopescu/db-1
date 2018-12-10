import db
import log_main
import logging
import traceback

log_main.initialize_logger("Employee")


def insert_data():
    try:
        query = "INSERT INTO EMPLOYEE (Fname, Minit, Lname, SSN, Birth_date, Address, Sex, Salary, Department) " \
                "VALUE (%s, %s, %s, %s, STR_TO_DATE(%s,'%d-%b-%Y'), %s, %s, %s, %s)"

        # 1
        data = ('James', 'E', 'Jordan', '888665151', '10-NOV-1927', '450 Stone,Houston,TX', 'M', 55000, 1)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 2
        data = ('Frank', 'T', 'Wong', '333445555', '08-DEC-1945', '638 Voss,Houston,TX', 'M', 40000, 5)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 3
        data = ('Jennifer', 'S', 'Wallace', '987654321', '20-JUN-1931', '291 Berry,Bellaire,TX', 'F', 43000, 4)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 4
        data = ('Jared', 'D', 'James', '111111100', '10-OCT-1966', '123 Peachtr,Atlanta,GA', 'M', 85000, 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 5
        data = ('Alex', 'D', 'Freed', '444444400', '09-OCT-1950', '4333 Pillsbury,Milwaukee,WI', 'M', 89000, 7)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 6
        data = ('John', 'C', 'James', '555555500', '30-JUN-1975', '766 Bloomington,Sacramento,CA', 'M', 81000, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 7
        data = ('John', 'B', 'Smith', '123456789', '09-Jan-1955', '731 Fondren,Houston,TX', 'M', 30000, 5)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 8
        data = ('Alicia', 'J', 'Zelaya', '999887777', '19-JUL-1958', '3321 Castle,Spring,TX', 'F', 25000, 4)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 9
        data = ('Ramesh', 'K', 'Narayan', '666884444', '15-SEP-1952', '971 Fire Oak,Humble,TX', 'M', 38000, 5)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 10
        data = ('Joyce', 'A', 'English', '453453453', '31-JUL-1962', '5631 Rice Oak,Houston,TX', 'F', 25000, 5)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 11
        data = ('Ahmad', 'V', 'Jabbar', '987987987', '29-MAR-1959', '980 Dallas,Houston,TX', 'M', 25000, 4)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 12
        data = ('Jon', 'C', 'Jones', '111111101', '14-NOV-1967', '111 Allgood,Atlanta,GA', 'M', 45000, 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 14
        data = ('Justin', None, 'Mark', '111111102', '12-JAN-1966', '2342 May,Atlanta,GA', 'M', 40000, 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 15
        data = ('Brad', 'C', 'Knight', '111111103', '13-FEB-1968', '176 Main St.,Atlanta,GA', 'M', 44000, 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 16
        data = ('Evan', 'E', 'Wallis', '222222200', '16-JAN-1958', '134 Pelham,Milwaukee,WI', 'M', 92000, 7)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 17
        data = ('Josh', 'U', 'Zell', '222222201', '22-MAY-1954', '266 McGrady,Milwaukee,WI', 'M', 56000, 7)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 18
        data = ('Andy', 'C', 'Vile', '222222202', '21-JUN-1944', '1967 Jordan,Milwaukee,WI', 'M', 53000, 7)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 19
        data = ('Tom', 'G', 'Brand', '222222203', '16-DEC-1966', '112 Third St,Milwaukee,WI', 'M', 62500, 7)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 19
        data = ('Jenny', 'F', 'Vos', '222222204', '11-NOV-1967', '263 Mayberry,Milwaukee,WI', 'F', 61000, 7)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 20
        data = ('Chris', 'A', 'Carter', '222222205', '21-MAR-1960', '565 Jordan,Milwaukee,WI', 'F', 43000, 7)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 21
        data = ('Kim', 'C', 'Grace', '333333300', '23-OCT-1970', '667 Mills Ave,Sacramento,CA', 'F', 79000, 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 22
        data = ('Jeff', 'H', 'Chase', '333333301', '07-JAN-1970', '15 Bradbury,Sacramento,CA', 'M', 44000, 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 23
        data = ('Bonnie', 'S', 'Bays', '444444401', '19-JUN-1956', '111 Hollow,Milwaukee,WI', 'F', 70000, 7)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 24
        data = ('Alec', 'C', 'Best', '444444402', '18-JUN-1966', '233 Solid,Milwaukee,WI', 'M', 60000, 7)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 25
        data = ('Sam', 'S', 'Snedden', '444444403', '31-JUL-1977', '97 Windy St,Milwaukee,WI', 'M', 48000, 7)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 26
        data = ('Nandita', 'K', 'Ball', '555555501', '16-APR-1969', '222 Howard,Sacramento,CA', 'M', 62000, 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 27
        data = ('Bob', 'B', 'Bender', '666666600', '17-APR-1968', '8794 Garfield,Chicago,IL', 'M', 96000, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 28
        data = ('Jill', 'J', 'Jarvis', '666666601', '14-JAN-1966', '6234 Lincoln,Chicago,IL', 'F', 36000, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 29
        data = ('Kate', 'W', 'King', '666666602', '16-APR-1966', '1976 Boone Trace,Chicago,IL', 'F', 44000, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 30
        data = ('Lyle', 'G', 'Leslie', '666666603', '09-JUN-1963', '417 Hancock Ave,Chicago,IL', 'M', 41000, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 31
        data = ('Billie', 'J', 'King', '666666604', '01-JAN-1960', '556 Washington,Chicago,IL', 'F', 38000, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 32
        data = ('Megan', 'G', 'Jones', '254937381', '02-MAR-1961', '528 Stone CT,Chicago,IL', 'F', 62000, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 33
        data = ('Jon', 'A', 'Kramer', '666666605', '22-AUG-1964', '1988 Windy Creek,Seattle,WA', 'M', 41500, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 34
        data = ('Ray', 'H', 'King', '666666606', '16-AUG-1949', '213 Delk Road,Seattle,WA', 'M', 44500, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 35
        data = ('Gerald', 'D', 'Small', '666666607', '15-MAY-1962', '122 Ball Street,Dallas,TX', 'M', 29000, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 36
        data = ('Arnold', 'A', 'Head', '666666608', '19-MAY-1967', '233 Spring St,Dallas,TX', 'M', 33000, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 37
        data = ('Helga', 'C', 'Pataki', '666666609', '11-MAR-1969', '101 Holyoke St,Dallas,TX', 'F', 32000, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 38
        data = ('Naveen', 'B', 'Drew', '666666610', '23-MAY-1970', '198 Elm St,Philadelphia,PA', 'M', 34000, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 39
        data = ('Carl', 'E', 'Reedy', '666666611', '21-JUN-1977', '213 Ball St,Philadelphia,PA', 'M', 32000, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 40
        data = ('Sammy', 'G', 'Hall', '666666612', '11-JAN-1970', '433 Main Street,Miami,FL', 'M', 37000, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 41
        data = ('Red', 'A', 'Bacher', '666666613', '21-MAY-1980', '196 Elm Street,Miami,FL', 'M', 33500, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 42
        data = ('Roy', 'C', 'Lewallen', '999999999', '02-MAR-1977', '14 Wynncrest Street,Dallas,TX', 'M', 75500, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 43
        data = ('John', 'T', 'Ed', '222333444', '18-FEB-1981', '4505 West St,Rochester,NY', 'M', 30000, 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 44
        data = ('Jennifer', 'A', 'Joy', '223344667', '19-MAY-1976', '1204 Main St,Miami,FL', 'F', 45000, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 45
        data = ('Kim', 'G', 'Ted', '444222666', '15-APR-1968', '3648 Tree Cir,Austin,TX', 'M', 50000, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 46
        data = ('Juan', 'G', 'Linda', '112244668', '23-JUN-1965', '1210 Apple St,Austin,TX', 'F', 55000, 9)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 47
        data = ('Jose', 'H', 'Barbara', '343434344', '28-FEB-1955', '905 East St,Kleen,TX', 'F', 35000, 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 48
        data = ('willie', 'D', 'Mary', '234234234', '20-DEC-1961', '101 South St,Arlington,TX', 'F', 12000, 9)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 49
        data = ('Erin', 'A', 'Maxfield', '242535609', '22-DEC-1971', '123 Copper St,Arlington,TX', 'F', 72000, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 50
        data = ('Sunil', 'D', 'Gupta', '110110110', '01-FEB-2001', '4312 Bowen Rd,Arlington,TX', 'M', 80000, 3)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 51
        data = ('Penny', 'G', 'Wolowitz', '673466642', '21-JAN-1974', '42 South Blvd,Miami,FL', 'F', 17000, 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 52
        data = ('Michael', 'A', 'Morgan', '636669233', '11-MAY-1984', '26 Sunset Blvd,Miami,FL', 'M', 73500, 5)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 53
        data = ('Sheldon', 'C', 'Cucuou', '849934919', '22-MAR-1974', '11 Hollywood Blvd,Dallas,TX', 'M', 35500, 8)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 54
        data = ('Debra', 'T', 'Hall', '202843824', '11-MAR-1983', '45 NY St,Rochester,NY', 'F', 30000, 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 55
        data = ('Jisha', 'A', 'Carpenter', '292740167', '29-MAY-1985', '194 Beachdr,Miami,FL', 'F', 15000, 1)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 56
        data = ('Gregory', 'G', 'Laurie', '444212096', '15-SEP-1969', '78 Tree Cir,Houston,TX', 'M', 90000, 7)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 57
        data = ('Lisa', 'G', 'House', '101248268', '29-JUN-1975', '12 Maple St,Austin,TX', 'F', 85000, 7)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 58
        data = ('Leonard', 'H', 'Moody', '349273344', '09-FEB-1973', '908 Greek Row,Austin,TX', 'M', 45000, 7)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 59
        data = ('Jake', 'D', 'Sheen', '245239264', '25-DEC-1954', '20 North Co,Arlington,TX', 'M', 52000, 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 60
        data = ('Wilson', 'A', 'Holmes', '242916639', '02-JUN-1971', '21 South Co,Arlington,TX', 'M', 72500, 4)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 61
        data = ('Cameron', 'D', 'Thirteen', '111422203', '04-MAY-2001', '22 Univ Blvd,Arlington,TX', 'F', 80000, 4)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 62
        data = ('Joseph', 'K', 'Kirkish', '913323708', '04-MAR-1996', '22 UT Blvd,Austin,TX', 'M', 95000, 7)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 63
        data = ('Andrea', 'M', 'Sondrini', '614370310', '30-DEC-1996', '1450 Worthington St,Houston,TX', 'F', 65000, 5)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 64
        data = ('Cindy', 'K', 'Burklow', '432765098', '23-FEB-1984', '2015 Neil Ave,Miami,FL', 'F', 45000, 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 65
        data = ('Zach', 'A', 'Geller', '913353347', '15-AUG-1990', '333 PikeWay,Seattle,WA', 'M', 55000, 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 66
        data = ('Alex', 'C', 'Yu', '001614905', '17-OCT-1980', '626 Mary St,Dallas,TX', 'M', 50000, 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 67
        data = ('Richard', 'T', 'Koelbel', '214370999', '3-APR-1976', '50 Elk St,Chicago,IL', 'M', 85000, 4)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 68
        data = ('Christina', 'S', 'Hisel', '241625699', '5-JUL-1986', '37 Church Row,Rochester,NY', 'F', 45000, 6)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 69
        data = ('Percy', 'M', 'Liang', '398172999', '12-JUN-1991', '14 Maple St,Austin,TX', 'M', 55000, 9)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

        # 70
        data = ('James', 'U', 'Miller', '906218888', '27-MAY-1978', '13 Fifth St,Seattle,WA', 'M', 75000, 5)
        print(db.insert_query(query, data))
        logging.info(str(query) + ' ' + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in INSERT_DATA: %s', e)


def update_data():
    try:
        query = "UPDATE EMPLOYEE SET Supervisor=%s WHERE SSN=%s"
        null = None

        # 1
        data = (null, '888665151')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 2
        data = ('888665555', '333445555')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 3
        data = ('888665555', '987654321')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 4
        data = (null, '111111100')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 5
        data = (null, '444444400')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 6
        data = (null, '555555500')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 7
        data = ('333445555', '123456789')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 8
        data = ('987654321', '999887777')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 9
        data = ('333445555', '666884444')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 10
        data = ('333445555', '453453453')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 11
        data = ('987654321', '987987987')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 12
        data = ('111111100', '111111101')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 13
        data = ('111111100', '111111102')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 14
        data = ('111111100', '111111103')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 15
        data = (null, '222222200')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 16
        data = ('222222200', '222222201')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 17
        data = ('222222200', '222222202')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 18
        data = ('222222200', '222222203')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 19
        data = ('222222201', '222222204')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 20
        data = ('222222201', '222222205')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 21
        data = (null, '333333300')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 22
        data = ('333333300', '333333301')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 23
        data = ('444444400', '444444401')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 24
        data = ('444444400', '444444402')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 25
        data = ('444444400', '444444403')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 26
        data = ('555555500', '555555501')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 27
        data = (null, '666666600')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 28
        data = ('666666600', '666666601')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 29
        data = ('666666600', '666666602')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 30
        data = ('666666601', '666666603')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 31
        data = ('666666603', '666666604')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 32
        data = ('666666600', '254937381')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 33
        data = ('666666603', '666666605')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 34
        data = ('666666604', '666666606')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 35
        data = ('666666602', '666666607')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 36
        data = ('666666602', '666666608')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 37
        data = ('666666602', '666666609')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 38
        data = ('666666607', '666666610')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 39
        data = ('666666610', '666666611')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 40
        data = ('666666611', '666666612')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 41
        data = ('666666612', '666666613')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 42
        data = ('666666600', '999999999')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 43
        data = ('555555501', '222333444')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 44
        data = ('666666613', '223344667')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 45
        data = ('999999999', '444222666')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 46
        data = (null, '112244668')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 47
        data = ('444444400', '343434344')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 48
        data = ('112244668', '234234234')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 49
        data = ('555555500', '242535609')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 50
        data = ('111111100', '110110110')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 51
        data = ('222333444', '673466642')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 52
        data = ('666666612', '636669233')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 53
        data = ('888665555', '849934919')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 54
        data = ('555555501', '202843824')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 55
        data = ('666666613', '292740167')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 56
        data = ('444444400', '444212096')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 57
        data = (null, '101248268')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 58
        data = ('444444400', '349273344')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 59
        data = ('112244668', '245239264')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 60
        data = ('555555500', '242916639')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 61
        data = ('987987987', '111422203')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 62
        data = (null, '913323708')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 63
        data = ('444444401', '614370310')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 64
        data = ('444444402', '432765098')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 65
        data = ('444444403', '913353347')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 66
        data = ('444444400', '001614905')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 67
        data = ('999999999', '214370999')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 68
        data = ('123456789', '241625699')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 69
        data = (null, '398172999')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

        # 70
        data = ('999999999', '906218888')
        print(db.update_query(query, data))
        logging.info(str(query) + " " + str(data))

    except Exception as e:
        traceback.print_exc()
        logging.error('Error in UPDATE_DATA: %s', e)


# insert_data()
update_data()
