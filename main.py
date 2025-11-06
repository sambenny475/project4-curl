from fastapi import FastAPI, Request
import uvicorn
from calc_func import result

app = FastAPI()


@app.get("/")
def get_answer():
    return {"message": "Use POST to send an expression"}


@app.post("/")
async def submit_form(request: Request):
    data = await request.json()
    expression = data["expression"]

    number = []
    operator = []
    num = ""

    for char in expression:
        if char.isdigit():
            num += char
        else:
            if num != "":
                number.append(num)
                num = ""
            if char in "+-*/":
                operator.append(char)

    if num != "":
        number.append(num)

    output = result(number, operator)
    return {"result": output}
