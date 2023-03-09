#!/usr/bin/env python3
from models.base_model import BaseModel
from models.user import User
from models.state import State


user1 = User()
user1.first_name = "Daniel"
user1.last_name = "John"
user1.email = "airbnb@mail.com"
user1.password = "root"
user1 = State()
user1.name = "Lagos"
print(user1)
