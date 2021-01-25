import requests
import json
import mysql.connector


'''Connect MySql database'''
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="mydatabase"
)

mycursor = mydb.cursor()

'''Create db, table and columns'''
# mycursor.execute("CREATE DATABASE VeganCafes")
# mycursor.execute("CREATE TABLE Cafe (id INT AUTO_INCREMENT PRIMARY KEY, name CHAR(255), phone CHAR(255), tags CHAR(255), adress CHAR(255))")
# mycursor.execute("ALTER TABLE Cafe ADD location CHAR(255), ADD mailindex CHAR(255), ADD raiting CHAR(255)")


'''Parsing yelp.com with api'''
api_key = '_zWrUBFSP9RxRxFLXXn-2-Bol-W3MpXuWiMNGqIhTAoBsVx6RUHjw4YKd78wXJTZD6C4sZeFK1ZzmnGjA9Qmxpi70K3E424uNlR0spcaLND2BupwoA_SGh3v0KgOYHYx'
headers = {'Authorization': 'Bearer %s' % api_key}

url = 'https://api.yelp.com/v3/businesses/search'
params = {'term': 'Vegan Cafe', 'location': 'San Francisco', 'limit': 50}

req = requests.get(url, params=params, headers=headers)

parsed = json.loads(req.text)

# print(json.dumps(parsed, indent=4))


businesses = parsed["businesses"]
tracker = 0

for business in businesses:
    detail_url = f'https://api.yelp.com/v3/businesses/{business["id"]}'
    detail_req = requests.get(detail_url, params=params, headers=headers)
    detail_parsed = json.loads(detail_req.text)
    # print("Name:", business["name"])
    # print("Phone:", business["phone"])
    # categories = detail_parsed["categories"]
    # for item in categories:
    #     print("Tags:", item["title"])
    # print("Address:", business["location"]['address1'])
    # print("City:", business["location"]['city'])
    # print("Zip code:", business["location"]['zip_code'])
    # print("latitude:", business["coordinates"]['latitude'])
    # print("longitude:", business["coordinates"]['longitude'])
    # print("Rating:", business["rating"])
    #
    # print("\n")

    name = business["name"]
    phone = business["phone"]
    categories = detail_parsed["categories"]
    for item in categories:
        tags = item["title"]
    address = business["location"]['address1']
    city = business["location"]['city']
    zip_code = business["location"]['zip_code']
    latitude = business["coordinates"]['latitude']
    longitude = business["coordinates"]['longitude']
    rating = business["rating"]

    db_input = (name, phone, tags, address, city, zip_code, rating, latitude, longitude)

    sql = "INSERT INTO Cafe (name, phone, tags, adress, location, mailindex, raiting, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

mycursor.executemany(sql, db_input)

mydb.commit()
print(mycursor.rowcount, "was inserted.")
