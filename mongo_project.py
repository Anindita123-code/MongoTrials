import os
import pymongo

if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDb"
COLLECTION = "celebrities"


def Mongo_Connect(url):
    try:
        conn = pymongo.MongoClient(url)
        # print("connected to mongo")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Not Connected to mongo:%s" % e)


def show_menu():
    print("-- MENU --")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")
    option = input("Select an option:")
    return option


def get_record():
    print("")
    fname = input("Enter first name >")
    lname = input("Enter last name >")
    try:
        doc = coll.find_one({"fname": fname.lower(), "lname": lname.lower()})
    except:
        print("error accessing the database")

    if not doc:
        print("")
        print("No matching records found")
    return doc


def add_record():
    print("")
    fname = input("Enter first name >")
    lname = input("Enter last name >")
    dob = input("Enter Date of Birth >")
    hair_color = input("Enter Hair Color >")

    new_doc = {
            "fname": fname.lower(),
            "lname": lname.lower(),
            "dob": dob,
            "hair_color": hair_color}
    try:
        coll.insert(new_doc)
        print("")
        print("Document Inserted")
    except:
        print("Error Accessing the database")


def find_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + " : " + v.capitalize())


def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")
                if update_doc[k] == "":
                    update_doc[k] = v

        try:
            coll.update_one(doc, {"$set": update_doc})
            print("")
            print("Document updated")
        except:
            print("Document not updated. \n Error accessing the database")


def delete_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())

        print("")
        confirmation = input("Is this the document you want to delete? \n (Y / N) >")
        print("")
        if confirmation.lower() == "y":
            try:
                coll.remove(doc)
                print("Document Deleted")
                print("")
            except:
                print("Error Accessing the database")
        else:
            print("Document not deleted")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("invalid option")
        print("")


conn = Mongo_Connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()
