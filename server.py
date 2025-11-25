from fastapi import FastAPI

from pydantic import BaseModel

class Message(BaseModel):
    name: str
    msg: str

app = FastAPI()
status = "online"
msgs = {}
msgs[0]="no motd set"
n=0

@app.get("/")
def read_root():
    return {"status": status}

@app.get("/msg")
def get_msg():
    return msgs

@app.post("/send")
def add_msg(data: Message):
    if data.name=="setmotd":
        msgs[0]=data.msg
    elif data.name and data.msg :
        global n
        n=n+1
        msgs[n]=data.name+": "+data.msg
        return {"result": "ok"}
    else:
        return {"result": "bad"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7007)
