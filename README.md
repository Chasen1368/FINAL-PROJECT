# FINAL-PROJECT
# 匿名提问箱

## 视频演示
TODO: 添加视频URL

## 项目描述
这是一个简单的匿名提问箱应用程序，允许用户匿名提交问题，并由管理员进行回复。项目使用SQLite作为数据存储，并提供了简单的数据库操作功能。

## 主要特性
- 匿名问题提交
- 管理员回复问题
- 问题列表查看
- 问题删除
- 管理员登录验证

## 项目文件结构
- `project.py`: 主项目文件，包含核心功能函数
  * `init_database()`: 初始化数据库
  * `add_question()`: 添加新问题
  * `reply_question()`: 回复问题
  * `get_questions()`: 获取问题列表
  * `delete_question()`: 删除问题
  * `admin_login()`: 管理员登录验证
  * `main()`: 应用程序入口

- `test_project.py`: 包含项目功能的单元测试
  * 测试问题添加、回复、获取、删除等功能
  * 使用pytest进行测试

- `requirements.txt`: 项目依赖列表

## 技术栈
- Python
- SQLite
- pytest

## 安装与运行
1. 克隆项目
2. 安装依赖: `pip install -r requirements.txt`
3. 运行应用: `python project.py`
4. 运行测试: `pytest test_project.py`

## 设计考虑
- 使用SQLite作为轻量级数据存储
- 提供简单的管理员认证
- 实现基本的CRUD操作
- 编写全面的单元测试

## 未来改进方向
- 增加更安全的管理员认证
- 支持分页显示问题
- 添加前端界面
- 增加更多错误处理

## 许可
TODO: 添加许可信息

## 作者
[您的姓名]