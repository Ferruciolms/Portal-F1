from core_log.models.log import Log
from core_log.models.log import CREATE, UPDATE, DELETE

from datetime import datetime
import json


def save_log(user, old=None, new=None):
    if new is not None or old is not None:
        new_log = Log(
            date=datetime.now(),
            user=user,
            model_id= new.id if new is not None else old.id
        )
        if old is None:
            print('Create')
            new_log.type = CREATE
            new_log.model = new.__class__.__name__
            new_log.data = create_json_create(new)
        elif new is None:
            print('Delete')
            new_log.type = DELETE
            new_log.model = old.__class__.__name__
            new_log.data = create_json_delete(old)
        else:
            print('Update')
            new_log.type = UPDATE
            new_log.model = new.__class__.__name__
            data = create_json_update(old, new)
            if data is None:
                return
            new_log.data = data
        new_log.save()

def create_json_delete(old):
    data = {}
    for key, value in old.__dict__.items():
        if key != '_state' and key != 'id':
            data[key] = str(value)
    return json.dumps(data)

def create_json_create(new):
    data = {}
    for key, value in new.__dict__.items():
        if key != '_state' and key != 'id':
            data[key] = str(value)
    return json.dumps(data)

def create_json_update(old, new):
    data = {}
    for key, value in old.__dict__.items():
        if key != '_state':
            if value != new.__dict__[key]:
                data[key] = {
                    'old': str(value),
                    'new': str(new.__dict__[key])
                }
    if len(data) == 0:
        return None
    return json.dumps(data)