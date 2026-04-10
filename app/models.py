from pydantic import BaseModel, Field


class Device(BaseModel):
    name: str = Field(..., description="Device display name")
    mac: str = Field(..., description="MAC address for Wake-on-LAN")
