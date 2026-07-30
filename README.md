# AWO MCP Demo

## Overview

This project demonstrates how the **Model Context Protocol (MCP)** can be used to expose processed AWO data to AI assistants such as Claude Desktop.

The prototype does **not** replace the existing AWO data pipeline. Instead, it provides a standardized interface between AI assistants and processed organizational data.

The current implementation uses a small CSV dataset as a demonstration. In a production environment, the same MCP server can be connected to the processed AWO database or data lake.

---

## Architecture

```
User
  │
Claude Desktop
  │
MCP Server
  │
Processed Dataset (CSV)
```

Production Architecture

```
User
  │
AI Assistant
  │
MCP Server
  │
Processed AWO Data
  │
Existing AWO Pipeline
(Scraping → Cleaning → Normalization → Deduplication)
```

---

## Features

- MCP server implemented with FastMCP
- Facility search by city
- Facility search by service
- Facility counting
- Claude Desktop integration
- Interactive Python client for testing

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
cd awo-mcp-demo
```

Create and activate a Conda environment.

```bash
conda create -n awo-mcp python=3.11
conda activate awo-mcp
```

Install the required packages.

```bash
pip install -r requirements.txt
```

---

## Running the MCP Server

```bash
python server.py
```

The server starts and waits for incoming MCP requests.

---

## Running the Demo Client

```bash
python client.py
```

---

## Claude Desktop Integration

Install Claude Desktop:

https://claude.ai/download

Add the following MCP server configuration to your Claude Desktop configuration file.

```json
{
  "mcpServers": {
    "awo": {
      "command": "C:\\Users\\<USERNAME>\\miniconda3\\envs\\awo-mcp\\python.exe",
      "args": [
        "D:\\path\\to\\awo-mcp-demo\\server.py"
      ]
    }
  }
}
```

Replace the Python executable path and the `server.py` path with the locations on your own machine.

Restart Claude Desktop after saving the configuration.

---

## Example Questions

- How many AWO facilities are in Berlin?
- Show me all AWO facilities in Berlin.
- Find facilities that provide elderly care.
- Find childcare facilities.

---

## Future Improvements

- Connect to the real processed AWO dataset
- Add additional MCP tools
- Connect to a production database
- Add authentication and authorization
- Improve logging and monitoring
- Containerize the application with Docker

---

## License

MIT License
