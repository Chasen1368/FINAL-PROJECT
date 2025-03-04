import os
import pytest
import sqlite3
import project

# 使用临时数据库进行测试
TEST_DB_PATH = 'test_data.db'

def setup_function():
    """
    每个测试前初始化数据库
    """
    project.init_database(TEST_DB_PATH)

def teardown_function():
    """
    每个测试后删除测试数据库
    """
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)

def test_add_question():
    """
    测试添加问题功能
    """
    question_id = project.add_question("这是一个测试问题", TEST_DB_PATH)
    assert question_id > 0

    conn = sqlite3.connect(TEST_DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM questions WHERE id = ?', (question_id,))
    question = cursor.fetchone()
    assert question is not None
    assert question[1] == "这是一个测试问题"
    conn.close()

def test_add_empty_question_raises_error():
    """
    测试添加空问题是否抛出异常
    """
    with pytest.raises(ValueError):
        project.add_question("", TEST_DB_PATH)
    with pytest.raises(ValueError):
        project.add_question("   ", TEST_DB_PATH)

def test_reply_question():
    """
    测试回复问题功能
    """
    question_id = project.add_question("这是一个测试问题", TEST_DB_PATH)
    result = project.reply_question(question_id, "这是一个测试回复", TEST_DB_PATH)
    assert result is True

    conn = sqlite3.connect(TEST_DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT answer, is_answered FROM questions WHERE id = ?', (question_id,))
    _, is_answered = cursor.fetchone()
    assert is_answered == 1
    conn.close()

def test_reply_empty_answer_raises_error():
    """
    测试回复空内容是否抛出异常
    """
    question_id = project.add_question("这是一个测试问题", TEST_DB_PATH)
    with pytest.raises(ValueError):
        project.reply_question(question_id, "", TEST_DB_PATH)

def test_get_questions():
    """
    测试获取问题列表功能
    """
    project.add_question("问题1", TEST_DB_PATH)
    project.add_question("问题2", TEST_DB_PATH)
    
    questions = project.get_questions(db_path=TEST_DB_PATH)
    assert len(questions) == 2

def test_delete_question():
    """
    测试删除问题功能
    """
    question_id = project.add_question("这是一个测试问题", TEST_DB_PATH)
    result = project.delete_question(question_id, TEST_DB_PATH)
    assert result is True

    questions = project.get_questions(db_path=TEST_DB_PATH)
    assert len(questions) == 0

def test_admin_login():
    """
    测试管理员登录功能
    """
    assert project.admin_login('admin123') is True
    assert project.admin_login('wrong_password') is False