from fastapi import FastAPI, Query

app = FastAPI(debug=True)

@app.get("/")
def read_root():
    return {"Hello World"}

@app.get("/greet/{name}/")
def read_greeting(name:str):
    return {"message":f"Greeting:{name}"}

@app.get("/greet/")
def read_greeting(operation: str = Query(None, description="Your name:")):
    return {"message":f"Greeting:{operation}"}


@app.get("/calculate/")
def calculate(
    num1: float = Query(None, description="Number1:"),
    operation: str = Query(None, description="Operation(-/+):"),
    num2: float = Query(None, description="Number2:")
            ):
    if operation == "-":
        division=num1-num2
        return {"message": f"{division}"}
    elif operation =="+":
        plus=num1+num2
        return{"message": f"{plus}"}
    else:
        return False
    