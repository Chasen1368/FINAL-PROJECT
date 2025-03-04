import sqlite3
from typing import List, Dict, Optional

def init_database(db_path: str = 'data.db') -> None:
    """
    初始化数据库，创建questions表
    
    Args:
        db_path (str): 数据库文件路径，默认为 'data.db'
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT,
            is_answered BOOLEAN DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def add_question(question: str, db_path: str = 'data.db') -> int:
    """
    添加一个新的匿名问题
    
    Args:
        question (str): 要添加的问题内容
        db_path (str): 数据库文件路径，默认为 'data.db'
    
    Returns:
        int: 新添加问题的ID
    """
    if not question or len(question.strip()) == 0:
        raise ValueError("问题不能为空")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO questions (question) VALUES (?)', (question,))
    question_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return question_id

def reply_question(question_id: int, answer: str, db_path: str = 'data.db') -> bool:
    """
    为指定问题添加回复
    
    Args:
        question_id (int): 问题ID
        answer (str): 回复内容
        db_path (str): 数据库文件路径，默认为 'data.db'
    
    Returns:
        bool: 是否成功回复
    """
    if not answer or len(answer.strip()) == 0:
        raise ValueError("回复不能为空")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE questions 
        SET answer = ?, is_answered = 1 
        WHERE id = ?
    ''', (answer, question_id))
    success = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return success

def get_questions(only_unanswered: bool = False, db_path: str = 'data.db') -> List[Dict]:
    """
    获取问题列表
    
    Args:
        only_unanswered (bool): 是否只获取未回复的问题
        db_path (str): 数据库文件路径，默认为 'data.db'
    
    Returns:
        List[Dict]: 问题列表
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    if only_unanswered:
        cursor.execute('SELECT * FROM questions WHERE is_answered = 0 ORDER BY created_at DESC')
    else:
        cursor.execute('SELECT * FROM questions ORDER BY created_at DESC')
    
    questions = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return questions

def delete_question(question_id: int, db_path: str = 'data.db') -> bool:
    """
    删除指定问题
    
    Args:
        question_id (int): 问题ID
        db_path (str): 数据库文件路径，默认为 'data.db'
    
    Returns:
        bool: 是否成功删除
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM questions WHERE id = ?', (question_id,))
    success = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return success

def admin_login(password: str) -> bool:
    """
    简单的管理员登录验证
    
    Args:
        password (str): 管理员密码
    
    Returns:
        bool: 是否登录成功
    """
    # 这里使用固定密码，实际应用中应使用更安全的认证方式
    return password == 'admin123'

def main():
    """
    主函数，初始化数据库
    """
    init_database()
    print("匿名提问箱应用已准备就绪")

if __name__ == '__main__':
    main()