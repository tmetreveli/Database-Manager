import json
from pymongo import MongoClient


def regions():
    with open("Data\\data.json", "r") as f:
        data = json.load(f)
    return list(data.keys())


class DatabaseManager:
    def __init__(self):
        self.client = MongoClient("localhost", 27017)
        self.database = self.client["Database"]

    def create_table(self):
        pass

    def add_data(self, table_name, **kwargs):
        self.database[table_name].insert_one(kwargs)

    def get_existing_relations(self):
        result = self.database["student_advisor"].find()
        return [(i['student_id'], i['advisor_id'],) for i in result]

    def delete_row(self, table_name, row_id):
        if table_name == "advisor":
            self.database[table_name].delete_one({"advisor_id": row_id})
        else:
            self.database[table_name].delete_one({"student_id": row_id})

    def load_data(self, table_name):
        return self.database[table_name].find()

    def search(self, table_name, name=None, surname=None, age=None, student_id=None, advisor_id=None):
        return self.database[table_name].find_one({"name": name, "surname": surname, "age": age,
                                                   "student_id": student_id, "advisor_id": advisor_id})

    def update(self, table_name, name, surname, age, id):
        if table_name == "students":
            self.database[table_name].update_one({"student_id": id}, {"$set": {"name": name, "surname": surname,
                                                                               "age": age}})
        elif table_name == "advisors":
            self.database[table_name].update_one({"advisor_id": id}, {"$set": {"name": name, "surname": surname,
                                                                               "age": age}})

    def check_bd(self):
        return True if self.database["student_advisor"].count_documents({}) == 0 else False

    def list_advisors_with_students_count(self, order_by):
        pipeline = [
            {
                "$lookup": {
                    "from": "student_advisor",
                    "localField": "advisor_id",
                    "foreignField": "advisor_id",
                    "as": "students"
                }
            },
            {
                "$group": {
                    "_id": "$advisor_id",
                    "name": {"$first": "$name"},
                    "surname": {"$first": "$surname"},
                    "student_count": {"$sum": {"$size": "$students"}}
                }
            },
            {
                "$sort": {"student_count": order_by}
            }
        ]
        return list(self.database["advisors"].aggregate(pipeline))

    def list_students_with_advisors_count(self, order_by):
        pipeline = [
            {
                "$lookup": {
                    "from": "student_advisor",
                    "localField": "student_id",
                    "foreignField": "student_id",
                    "as": "advisors"
                }
            },
            {
                "$group": {
                    "_id": "$student_id",
                    "name": {"$first": "$name"},
                    "surname": {"$first": "$surname"},
                    "advisor_count": {"$sum": {"$size": "$advisors"}}
                }
            },
            {
                "$sort": {"advisor_count": order_by}
            }
        ]
        return list(self.database["students"].aggregate(pipeline))
