from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from repository import Repository

app = FastAPI()
repo = Repository()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "users": repo.get_users(),
        "projects": repo.get_projects(),
        "tasks": repo.get_tasks()
    })


@app.post("/users/")
def create_user(name: str = Form(...)):
    print(f"Received user name: {name}")
    repo.create_user(name)
    return RedirectResponse("/", status_code=303)


@app.post("/projects/")
def create_project(title: str = Form(...), user_id: int = Form(...)):
    repo.create_project(title, user_id)
    return RedirectResponse("/", status_code=303)


@app.post("/tasks/")
def create_task(description: str = Form(...), project_id: int = Form(...)):
    repo.create_task(description, project_id)
    return RedirectResponse("/", status_code=303)


@app.post("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    repo.complete_task(task_id)
    return RedirectResponse("/", status_code=303)


@app.post("/tasks/{task_id}/delete")
def delete_task(task_id: int):
    repo.delete_task(task_id)
    return RedirectResponse("/", status_code=303)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)


@app.post("/projects/{project_id}/delete")
def delete_project(project_id: int):
    repo.delete_project(project_id)
    return RedirectResponse("/", status_code=303)
