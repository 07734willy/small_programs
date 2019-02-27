import multiprocessing  

profiles = [{u'firstName': u'Karen', u'age': 20},
           {u'firstName': u'Jon', u'age': 25}] 

def testing(i):
    print "Hey " + str(i["firstName"]) + "!"

def pool_testing():
    pool = multiprocessing.Pool()
    pool.map(testing, profiles)

pool_testing()
