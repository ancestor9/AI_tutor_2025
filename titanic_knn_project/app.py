import uvicorn
from views.api_view import app
from run_all import *

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)