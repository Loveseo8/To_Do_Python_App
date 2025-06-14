from models import User, Project, Task

class Repository:
    def __init__(self):
        self.users = {}
        self.projects = {}
        self.tasks = {}
        self.user_counter = 1
        self.project_counter = 1
        self.task_counter = 1

    def get_users(self):
        return list(self.users.values())

    def get_projects(self):
        return list(self.projects.values())

    def get_tasks(self):
        return list(self.tasks.values())

    def create_user(self, name: str):
        user = User(self.user_counter, name)
        self.users[self.user_counter] = user
        self.user_counter += 1
        return user

    def create_project(self, title: str, user_id: int):
        if user_id not in self.users:
            raise ValueError("User not found")
        project = Project(self.project_counter, title, user_id)
        self.projects[self.project_counter] = project
        self.project_counter += 1
        return project

    def create_task(self, description: str, project_id: int):
        if project_id not in self.projects:
            raise ValueError("Project not found")
        task = Task(self.task_counter, description, project_id)
        self.tasks[self.task_counter] = task
        self.task_counter += 1
        return task

    def complete_task(self, task_id: int):
        if task_id not in self.tasks:
            raise ValueError("Task not found")
        self.tasks[task_id].completed = True
        return self.tasks[task_id]

    def delete_task(self, task_id: int):
        return self.tasks.pop(task_id, None)

    def delete_project(self, project_id: int):
        for tid in [tid for tid, t in self.tasks.items() if t.project_id == project_id]:
            self.tasks.pop(tid)
        return self.projects.pop(project_id, None)

repo = Repository()
