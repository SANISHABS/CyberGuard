from services.defender import get_defender_status
from services.ports import scan_ports
from services.actions import execute_action
from pydantic import BaseModel
from services.scanner import run_scan
from fastapi import FastAPI

from services.firewall import (
    get_firewall_status,
    enable_firewall
)

app = FastAPI(
    title="CyberGuard Endpoint Agent",
    version="1.0"
)

class ActionRequest(BaseModel):
    action: str

@app.get("/")
def home():
    return {
        "message": "Welcome to CyberGuard"
    }


@app.get("/health")
def health():
    return {
        "status": "running"
    }


@app.get("/firewall")
def firewall():

    return get_firewall_status()


@app.post("/firewall/enable")
def firewall_enable():

    return enable_firewall()

@app.get("/scan")
def scan():

    return run_scan()

@app.post("/action")
def perform_action(request: ActionRequest):
    return execute_action(request.action)

@app.get("/ports")
def get_ports():
    return {
        "ports": scan_ports()
    }
    
@app.get("/defender")
def defender():
    return get_defender_status()