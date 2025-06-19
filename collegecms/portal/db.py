from pymongo import MongoClient
mongo=MongoClient("localhost:27017")
db=mongo.college
students=db.students
faculty=db.faculty
admin=db.admin

# Insert sample student
students.insert_one({
    "email": "student1@gmail.com",
    "name": "Student One",
    "password": "12345678",
    "role": "student"
})

# Insert sample faculty
faculty.insert_one({
    "email": "faculty1@gmail.com",
    "name": "Faculty One",
    "password": "abcdef12",
    "role": "faculty"
})

admin.insert_one({
  "email": "admin@gmail.com",
  "password": "admin123",
  "role": "admin"
})
