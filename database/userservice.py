from database import get_db
from database.models import *
from datetime import datetime

def register_user_db(name: str, phone_number: str):
    db = next(get_db())
    new_user = User(name=name, phone_number=phone_number,
                    reg_date=datetime.now())
    db.add(new_user)
    db.commit()
    return new_user.id
def check_user(name, phone_number):
    db = next(get_db())
    check = db.query(User).filter_by(name=name).first()
    check_by_name = db.query(User).filter_by(name=name).first()
    check_by_phone = db.query(User).filter_by(phone_number=phone_number).first()
    if check:
        return True
    elif check_by_name:
        return "Имя занято"
    elif check_by_phone:
        return "Номер занят"
    id = register_user_db(name, phone_number)
    return id
