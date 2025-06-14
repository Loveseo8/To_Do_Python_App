class User:
    def __init__(self, user_id: int, name: str):
        self.id = user_id
        self.name = name

class Project:
    def __init__(self, project_id: int, title: str, user_id: int):
        self.id = project_id
        self.title = title
        self.user_id = user_id

class Task:
    def __init__(self, task_id: int, description: str, project_id: int):
        self.id = task_id
        self.description = description
        self.project_id = project_id
        self.completed = False
