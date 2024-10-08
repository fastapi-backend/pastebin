from fastapi import APIRouter, HTTPException, status, Request
from model.schemas import UserData
import random
import redis

router = APIRouter()


@router.post("/new/")
async def pastebin(data: UserData, request: Request):
    r = redis.Redis(host='redis_app', port=6379, db=0)
    while True:
        link = random.randint(0, 1000000000000000)
        if not r.get(link):
            r.set(link, data.data, ex=86400)
            return{
                "link": request.url.hostname + f"/pastebin/bin/{link}",
            }
            break


@router.get("/bin/{link}")
async def pastebin(link: int):
    r = redis.Redis(host='redis_app', port=6379, db=0)
    cache = r.get(link)
    if not cache:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Bin not found')
    return{
        "you bin": cache
    }
