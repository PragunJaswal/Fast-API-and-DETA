from fastapi import FastAPI

app = FastAPI()

@app.get("/getdata")
async def root():
    return{
        "Hello":"Pragun",
        "Mobile":"854745770"   
           }

# uvicorn main:app --reload   to run locally

# for deta space::

# SCJekHPr_to3o8u7TrLxjrQcQMU7Ts2rgsWX1kvvW  token
# SCJekHPr token id