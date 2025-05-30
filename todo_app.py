from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional 

app = FastAPI()

todos = {}

class Todo(BaseModel):
    title : str 
    description : Optional[str] = None 
    completed : bool = False 

class UpdateTodo(BaseModel) : 
    title : Optional[str] = None 
    description : Optional[str] = None
    completed : Optional[bool] = None

@app.get("/")
def index():
    return {"message" : "Todo APP"}

@app.get("/get-todos")
def get_todos():
    return todos

@app.get("/get-todo/{todo_id}")
def get_todo_by_id(todo_id : int = Path(... , description = "The ID of todo you want to view." , gt = 0)):
    return todos[todo_id]

@app.post("/create-todo/{todo_id}")
def create_todo(* , todo_id : int , todo : Todo):
    if todo_id in todos : 
        return {"Error" : "Todo already exists."}
    
    todos[todo_id] = todo 
    return todos[todo_id]

@app.put("/update-todo/{todo_id}")
def update_todo(todo_id : int , todo: UpdateTodo):
    if todo_id not in todos : 
        return {"Error" : "Todo does not exist."}
    
    if todo.title is not None : 
        todos[todo_id].title = todo.title
    if todo.description is not None : 
        todos[todo_id].description = todo.description
    if todo.completed is not None : 
        todos[todo_id].completed = todo.completed
    
    return todos[todo_id]

@app.delete("/delete-todo/{todo_id}")
def delete_todo(todo_id : int):
    if todo_id not in todos : 
        return {"Error" : "Todo does not exist."} 
    
    del todos[todo_id]
    return {"Message" : "Todo deleted successfully."}