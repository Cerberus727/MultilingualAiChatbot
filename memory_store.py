from typing import List, Tuple
from collections import deque
import sqlite3
class SQLiteMemoryStore:
    def __init__(self, db_path="chat_memory.db"):
        self.conn=sqlite3.connect(db_path)
        self.cursor=self.conn.cursor()
    def add(self, user_id:str, role:str,message:str):
        self.cursor.execute(
            "INSERT INTO chat_history(user_id,role,message) VALUES (?,?,?)",
            (user_id,role,message)
        )
        self.conn.commit()
    def get_memory(self,user_id:str,limit:int =20)-> List[Tuple[str,str]]:
        self.cursor.execute(
            "SELECT role,message FROM chat_history WHERE user_id=? order by id DESC LIMIT?",(user_id,limit)
        )
        rows=self.cursor.fetchall()
        return list(reversed(rows))
    def search(self, user_id:str,query:str)->List[str]:
        self.cursor.execute(
            "SELECT message FROM chat_history WHERE user_id=? AND message LIKE ?",
            (user_id, f"%{query}")
        )
        return [row[0] for row in self.cursor.fetchall()]
    def clear_history(self, user_id: str):
        cursor=self.conn.cursor()
        cursor.execute("DELETE FROM chat_history WHERE user_id = ?", (user_id,))
        self.conn.commit()
