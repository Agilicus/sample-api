# from flask import g
import datetime
import shortuuid


def get_tickets():
    return [
        { "id": shortuuid.uuid(),
          "user": "A Random Person",
          "time": datetime.datetime.utcnow().isoformat()
        },
        { "id": shortuuid.uuid(),
          "user": "A Random Person",
          "time": datetime.datetime.utcnow().isoformat()
        }
    ]


def get_ticket(id):
    return { "id": id,
             "user": "A Random Person",
             "time": datetime.datetime.utcnow().isoformat()
           }

def delete_ticket(id):
    return { "id": id,
             "user": "A Random Person",
             "time": datetime.datetime.utcnow().isoformat()
           }

def put_ticket(body):
    return body

def post_ticket(body):
    return body
