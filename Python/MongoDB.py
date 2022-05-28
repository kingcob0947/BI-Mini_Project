
#.....Inser multiple documents:-
# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["python"]
# mycol = mydb["content"]
# mylist = [
#     {"Name":"sandy", "Language":"C", "company":"wipro"},
#     {"Name":"devid", "Language":"C++","company":"google"},
#     {"Name":"sandy", "Language":"java", "company":"amazon"},
#     {"Name":"sandy", "Language":"R", "company":"microsoft"},
#     {"Name":"sandy", "Language":"php", "company":"capgemini"},
#     {"Name":"sandy", "Language":"sql", "company":"cognizent"},
#     {"Name":"sandy", "Language":"python", "company":"hcl"},
#     {"Name":"sandy", "Language":"C", "company":"accenture"},
#     {"Name":"sandy", "Language":"css", "company":"facebook"}
# ]
# for x in mycol.find():
#     print(x)

#.... delete the documents:-
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["python"]
mycol = mydb["content"]

for x in mycol.find():
    print(x)