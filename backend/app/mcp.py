from typing import Any, Dict, Optional

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

PROMPTS = [
    {"name": "greeting", "description": "Simple greeting prompt"},
]

RESOURCES = [
    {"uri": "resource://example.txt", "name": "Example Resource"},
]

TOOLS = [
    {
        "name": "echo",
        "description": "Echo text back",
        "inputSchema": {"type": "object", "properties": {"text": {"type": "string"}}},
    }
]

router = APIRouter()


class JSONRPCRequest(BaseModel):
    jsonrpc: str
    method: str
    params: Optional[Dict[str, Any]] = None
    id: Optional[int | str] = None


@router.post("/mcp")
async def handle_mcp(request: JSONRPCRequest):
    if request.jsonrpc != "2.0":
        raise HTTPException(status_code=400, detail="Unsupported JSON-RPC version")

    if request.method == "initialize":
        protocol_version = None
        if request.params:
            protocol_version = request.params.get("protocolVersion")
        result = {
            "protocolVersion": protocol_version or "2024-11-05",
            "capabilities": {
                "logging": {},
                "prompts": {"listChanged": True},
                "resources": {"listChanged": True},
                "tools": {"listChanged": True},
            },
            "serverInfo": {"name": "GodotAI", "version": "0.1.0"},
            "instructions": "Welcome to the MCP server",
        }
        return JSONResponse({"jsonrpc": "2.0", "id": request.id, "result": result})

    if request.method == "prompts/list":
        return JSONResponse(
            {"jsonrpc": "2.0", "id": request.id, "result": {"prompts": PROMPTS}}
        )

    if request.method == "resources/list":
        return JSONResponse(
            {"jsonrpc": "2.0", "id": request.id, "result": {"resources": RESOURCES}}
        )

    if request.method == "tools/list":
        return JSONResponse(
            {"jsonrpc": "2.0", "id": request.id, "result": {"tools": TOOLS}}
        )

    raise HTTPException(status_code=404, detail="Method not supported")
