import pymysql as my

#root password is something you set when you install mysql on your system
#the default may be blank; I use python123 for testing
dbconn = my.connect (host='127.0.0.1',port=3306,user='root', password='python123',  db='students')
 
#print(dbconn)
cursor = dbconn.cursor()
query = "SELECT ID, FirstName, LastName, Type, Password FROM user"
cursor.execute(query)
#the following line shows the schema descriptions of the headers of the data retrieved in the cursor object from the database using the query
print(cursor.description)


users = []

for (ID, FirstName, LastName, Type, Password) in cursor:
    print("{} {} {} ({}) found. Password is {}.".format(ID, FirstName, LastName, Type, Password))
    thisuser = [ID,FirstName,LastName,Type,Password]
    users.append(thisuser)
cursor.close()
cursor = dbconn.cursor()
query = "SELECT * FROM grades"
cursor.execute(query)
grades = []
for GradeID, Grade,Comment,UserID in cursor:
    thisgrade = [GradeID,Grade,Comment,UserID]
    grades.append(thisgrade)
dbconn.close()

print(users)

print(users[1][1],users[1][2])

print(grades)

print(str(grades[0][1])+" is of type "+str(type(grades[0][1])))
