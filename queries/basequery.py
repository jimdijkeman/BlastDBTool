class BaseQuery:
    def __init__(self, table, cursor) -> None:
        self.table = table
        self.cursor = cursor

    def get_all(self, query: str = ""):
        self.cursor.execute(f'SELECT * FROM {self.table} {query}')
        return self.cursor.fetchall()

    def get_by_id(self, record_id):
        self.cursor.execute(f'SELECT * FROM {self.table} WHERE id = {record_id}')
        return self.cursor.fetchone()
