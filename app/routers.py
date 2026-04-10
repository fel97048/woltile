import json
from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from .models import Device
from .wol import send_wol

router = APIRouter()
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "devices.json"


def load_devices() -> list[Device]:
    try:
        with CONFIG_PATH.open("r", encoding="utf-8") as f:
            raw_devices = json.load(f)
        return [Device(**item) for item in raw_devices]
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Device configuration not found")
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to load devices: {exc}")


@router.get("/api/devices")
def get_devices():
    devices = load_devices()
    return [device.dict() for device in devices]


@router.post("/api/wake")
def wake_device(payload: dict):
    mac = payload.get("mac")
    if not mac:
        raise HTTPException(status_code=400, detail="MAC address is required")

    try:
        send_wol(mac)
        return JSONResponse({"success": True, "message": "Wake-on-LAN packet sent."})
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
