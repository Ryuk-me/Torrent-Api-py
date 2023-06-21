from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


def error_handler(status_code, json_message):
    return JSONResponse(
        status_code=status_code,
        content=jsonable_encoder(json_message),
    )
