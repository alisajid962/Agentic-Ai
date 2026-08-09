from fastapi.requests import Request
from datetime  import datetime
from starlette.middleware.base import BaseHTTPMiddleware

class response_time_middleware(BaseHTTPMiddleware):
     async def dispatch(self, request: Request, call_next):
        start =datetime.now()
       

        response = await call_next(request)

        response_time = datetime.now()-start
        print(response_time)
        return response


