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
- Implemented Tools

Three core tools were implemented to demonstrate the server's querying capabilities:

  - `count_facilities(city)`: Returns the total number of facilities in a specified city.
  - `search_facilities(city)`: Returns a detailed list of facilities located in a given city.
  - `find_facilities_by_service(service)`: Returns a list of facilities that offer a specific service.

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

Open a terminal in the project directory and activate the Conda environment.

```bash
conda activate awo-mcp
python server.py
```

The server will start and wait for incoming MCP requests. This is expected behavior. Leave this terminal open while testing.

---

## Running the Demo Client

Open a **second terminal** in the same project directory.

Activate the Conda environment again.

```bash
conda activate awo-mcp
python client.py
```

The interactive menu will appear:

```text
==============================
      AWO MCP Demo
==============================
1. Count facilities
2. Search by city
3. Search by service
0. Exit
```

Choose an option and enter the requested information. The client will communicate with the MCP server and display the returned results.
for instance:
### Option 1 – Count Facilities

Select **1** and enter a city name (e.g., `Berlin`).

The client calls the MCP tool:

```python
count_facilities(city="Berlin")
```

The server searches the dataset and returns the number of matching facilities.

Example:

```text
City: Berlin

Result
------
2
```

---

---

## Claude Desktop Integration

Instead of using the demo client, you can connect the MCP server directly to Claude Desktop.

### Step 1 – Install Claude Desktop

Download Claude Desktop:

https://claude.ai/download

### Step 2 – Configure the MCP Server

Open the Claude Desktop configuration file and add the following server configuration.

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

Replace:

- `<USERNAME>` with your Windows username.
- `D:\\path\\to\\awo-mcp-demo\\server.py` with the full path to your `server.py` file.

### Step 3 – Restart Claude Desktop

Save the configuration file and restart Claude Desktop.

The MCP server should appear under **Settings → Developer → Local MCP Servers**.

Once connected, Claude can automatically use the available MCP tools.

Example questions:

- How many AWO facilities are in Berlin?
- Show me all AWO facilities in Berlin.
- Find facilities that provide elderly care.
- 
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
