from mongoengine import connect


from photo_mongo_wrapper import *

connect("g16-photo-db",
            username="g16-user",
            password="xYyR4FPh4W79YY6vWiDm",
            host="mongo.cloud.rennes.enst-bretagne.fr")

mongo_get_photo_by_name_and_id("asd", 1)