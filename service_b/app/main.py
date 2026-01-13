from fastapi import FastAPI , HTTPException
import uvicorn
from schemas import Location
from storage.crud import DbOperations

db = DbOperations()
app = FastAPI()


@app.post("/add_location")
def add_location(location: Location):
    try:
        if db.add_location(location.model_dump()):
            return {"The location has been successfully added":True}
        else:
            return {"The location already exists in the system":False}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500)


@app.get("/get_all_location")
def get_all():
    try:
        return db.get_all_location()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500)






if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)