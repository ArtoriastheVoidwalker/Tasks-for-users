#!/bin/bash
python - << EOF
from base.db import database
from routers import app


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

EOF

