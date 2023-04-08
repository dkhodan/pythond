from fastapi import FastAPI
import redis

app = FastAPI()
r = redis.Redis(host="redis", port=6379)

import debugpy
debugpy.listen(("0.0.0.0", 5678))

@app.get("/")
def read_root():
    return {"Hello World. Check if updated. Now updated from the container."}

@app.get("/hits")
def read_root():
    r.incr("hits")
    return {"hits: ": r.get("hits")}