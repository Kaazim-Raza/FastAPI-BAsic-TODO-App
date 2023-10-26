from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


todos = []

#Get all todos

@app.get("/todos")
async def get_todos():
    return {"todos": todos}


#Get single todo

@app.get("/todos/{todo_id}")
async def get_todo(todo_id : int):
    for todo in todos:
        if todo.id  == todo_id:
            return {"todo": todo}
    
    return {"message": "no todos found"}


#Create a todo
@app.post("/todos")
async def create_todos(todo : Todo):
    todos.append(todo)
    return {"message": "Todo has been added"}

#Update a todo

@app.put("/todos/{todo_id}")
async def update_todos(todo_id : int, todo_object : Todo):
    for todo in todos:
        if todo.id  == todo_id:
            todo.id == todo_id
            todo.item == todo_object
            return {"todo": todo}
    
    return {"message": "no todos found to update"}


#Delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todos(todo_id : int):
    for todo in todos:
        if todo.id  == todo_id:
            todos.remove(todo)
            return {"message": "Todo removed"}
    
    return {"message": "no todos found"}
