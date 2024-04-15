from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact



class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        firstname = Optional(str, column="firstname")
        lastname = Optional(str, column="lastname")
        deprecated = Optional(datetime, column="deprecated")

    # Инициализируем базу данных
    def __init__(self, host, name, user, password):
        self.db.bind(provider='mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)


    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    # Получение списка групп
    @db_session
    def get_group_list(self):
        return list(select(g for g in ORMFixture.ORMGroup))



