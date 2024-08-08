from fastapi import FastAPI, Request
import time
from dotenv import load_dotenv
load_dotenv()
from .router import search, user, auth
# from .router import elections, user, post, auth, search, members, departments
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, Response
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

description = """
Gov Glance API an aggregate of government news and data! 

## Items

You can **read items**.

## Users

You will be able to:

* **Create an Account ** .
* **Bearer Token Last a Year, to renew your bearer token just sign in onces more in the login tab**.

"""


app = FastAPI(
    title= "Gov Glance API",
    description= description,
    summary= "Government News and Data at a Glance!",
    version= "1.0.0",
    contact= {
        "name" : "Gov Glance Team",
        "email": "contact@govglance.org"
    }) 

app.mount("/static", StaticFiles(directory="static"), name="static")

# @app.get("/docs", response_class=HTMLResponse)
# def custom_swagger_ui():
#     return HTMLResponse(content=open("static/swagger-ui.html", "r").read(), status_code=200)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(search.router)
# app.include_router(members.router)
# app.include_router(departments.router)
# app.include_router(elections.router)



@app.get("/", response_class=HTMLResponse)
def root():
    return HTMLResponse(content=open("templates/index.html", "r").read(), status_code=200)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    print("Time took to process the request and return response is {} sec".format(time.time() - start_time))
    return response