from tinydb import TinyDB, Query
from tinydb.database import Document

class DB:
    def __init__(self, path) -> None:
        self.db = TinyDB(path, indent=4, separators=(',', ': '))
        self.query = Query()
        self.user = self.db.table('user')

    """
    user data baea sexema
    chat_id:{
        'first_name': 'first_name',
        'username': 'username',
        'phone_number': 'phone_number',
        'chat_id': 'chat_id',
    }
    """

    def add_user(self, chat_id, username, first_name=None, phone_number=None):
        self.user.insert(Document({
            'username': username,
            'first_name': first_name,
            'chat_id': chat_id,
            'phone_number': phone_number
            }, doc_id=chat_id))
        
    def get_user(self, chat_id):
        return self.user.get(doc_id=chat_id)
    
    def update_user(self, chat_id, firstname=None, phone_number=None):
        if firstname:
            self.user.update({'first_name': firstname}, doc_ids=[chat_id])
        if phone_number:
            self.user.update({'phone_number': phone_number}, doc_ids=[chat_id])

# test DB
db = DB('db.json')
# print(db.add_user(2, 'username', ))

