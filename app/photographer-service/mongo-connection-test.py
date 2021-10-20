from mongoengine import connect


from photographer_mongo_wrapper import *

connect("g16-photographer-db",
            username="g16-user",
            password="xYyR4FPh4W79YY6vWiDm",
            host="mongo.cloud.rennes.enst-bretagne.fr")

print(mongo_get_photographers(0, 1))