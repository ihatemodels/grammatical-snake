import sqlite3


class Database:
    GET_TABLES = "SELECT name FROM sqlite_master WHERE type='table';"
    connection = sqlite3.connect("./grammar.db")

    def __init__(self):

        self.cursor = self.connection.cursor()
        self.is_valid_database = False
        self._validate()

    def _validate(self):

        tables = self.cursor.execute(self.GET_TABLES).fetchall()

        for table in tables:
            if "bulgarian_rules" in table:
                self.is_valid_database = True

        if not self.is_valid_database:
            raise Exception("bulgarian_rules table not found in database.")

    def make_request(self, query) -> list:

        return self.cursor.execute(query).fetchall()

    def _get_rule_by_id(self, identifier: int) -> str:
        rows = self.make_request(f"SELECT rule FROM bulgarian_rules WHERE id={identifier}")
        return str(rows[0][0])


class Reader(Database):

    def __init__(self):
        super().__init__()

        self.bulgarian_id_key_hashmap = {}
        self.bulgarian_id_name_hashmap = {}

        rows = self.make_request("SELECT id, key, name FROM bulgarian_rules;")

        for row in rows:
            self.bulgarian_id_key_hashmap[row[0]] = row[1].split(',')
            self.bulgarian_id_name_hashmap[row[0]] = row[2]

    def get_rule_by_id(self, identifier: int) -> str:

        if identifier not in self.bulgarian_id_key_hashmap.keys():
            print(f"Unknown rule identifier: {identifier}")
            return ""

        return self._get_rule_by_id(identifier)

    def get_name_by_id(self, identifier: int) -> str:
        if identifier not in self.bulgarian_id_name_hashmap.keys():
            return ""

        return self.bulgarian_id_name_hashmap[identifier]

    def menu(self):
        pass