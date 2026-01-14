from fastapi import APIRouter, HTTPException
from schemas import IPRequest
from services import resolve_ip_and_send

router = APIRouter()


@router.post("/resolve-ip")
def resolve_ip(request: IPRequest):
    try:
        data = resolve_ip_and_send(request.ip)
        return {"status": "ok", "data": data }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
