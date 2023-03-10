import base64
from io import BytesIO
from uuid import uuid4

import qrcode
import uvicorn
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import HTMLResponse
from pysondb import db as pysondb

from html_pages import (
    return_error_html,
    return_input_users_html,
    return_qr_code_html,
    return_users_html,
)

PORT = 8000
URL = f"http://localhost:{PORT}"


def main():
    # Initialize FastAPI
    app = FastAPI()
    database = pysondb.getDb("./users.json")

    @app.post("/generate", response_class=HTMLResponse)
    async def generate_post(
        name: str = Form(...), drg: str = Form(...), piranti: str = Form(...), date: str = Form(...), detail: str = Form(...), photo: UploadFile = File(...)
    ):
        try:
            photo = await photo.read()
            base64_bytes = base64.b64encode(photo)
            base64_string = base64_bytes.decode("utf-8")
            uuid_data = str(uuid4().hex)
            database.add(
                {
                    "uuid": uuid_data,
                    "name": name,
                    "drg": drg,
                    "piranti": piranti,
                    "date": date,
                    "detail": detail,
                    "photo": base64_string,
                }
            )
            data = database.getByQuery({"uuid": uuid_data})[0]
            qrcode_pillow = qrcode.make(f'{URL}/users/{data["uuid"]}')
            im_file = BytesIO()
            qrcode_pillow.save(im_file, format="JPEG")
            im_bytes = im_file.getvalue()
            im_b64 = base64.b64encode(im_bytes).decode("utf-8")
            return return_qr_code_html(im_b64)

        except Exception as e:
            return return_error_html(e)

    @app.get("/generate", response_class=HTMLResponse)
    async def generate_get():
        return return_input_users_html()

    @app.get("/users/{uuid}", response_class=HTMLResponse)
    def get_user(uuid: str):
        try:
            data = database.getByQuery({"uuid": uuid})
            if len(data) != 0:
                return return_users_html(data)
            return return_error_html("User not found")
        except Exception as e:
            return return_error_html(e)

    # Run FastAPI
    uvicorn.run(app, host="0.0.0.0", port=PORT)


if __name__ == "__main__":
    # Create argument parser
    main()
