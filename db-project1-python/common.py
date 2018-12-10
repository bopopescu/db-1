with open('/home/abhishek/Documents/DataFiles/WORKS_ON.txt') as f:
    contents = f.readlines()
    i = 0
    for content in contents:
        i += 1
        print('\n# ' + str(i) + ' \ndata = (' + content.strip() +
              ') \nprint(db.insert_query(query, data)) \nlogging.info(str(query) + " " + str(data))')

# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in contents]

# with open('/home/abhishek/Documents/DataFiles/EMPLOYEE.txt') as f:
#     contents = f.readlines()
#     i = 0
#     for content in contents:
#         i += 1
#         content = content.split(',')
#         ssn = content[3]
#         super_ = content[-2]
#         print('\n# ' + str(i) + ' \ndata = (' + super_.strip() + ', ' + ssn.strip() +
#               ') \nprint(db.update_query(query, data)) \nlogging.info(str(query) + " " + str(data))')
#
# # you may also want to remove whitespace characters like `\n` at the end of each line
# content = [x.strip() for x in contents]
