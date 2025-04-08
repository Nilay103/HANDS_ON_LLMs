# Weather MCP Server

A Model Context Protocol (MCP) server that provides weather information using the National Weather Service (NWS) API. This server exposes tools for fetching weather alerts and forecasts.

## Features

- Get active weather alerts for any US state
- Get detailed weather forecasts for any location using coordinates

## Installation

This project uses `uv` for dependency management. To install:

```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate

# Install dependencies
uv add "mcp[cli]" httpx
```

## Usage

### Running the Server

```bash
uv run weather.py
```

### Available Tools

1. `get_alerts(state: str)`
   - Get active weather alerts for a US state
   - Parameter: Two-letter US state code (e.g., CA, NY)
   - Returns: Formatted list of active alerts with details

2. `get_forecast(latitude: float, longitude: float)`
   - Get weather forecast for a specific location
   - Parameters: 
     - latitude: Location latitude
     - longitude: Location longitude
   - Returns: 5-period weather forecast with temperature, wind, and detailed conditions

## Dependencies

- Python >= 3.13
- httpx >= 0.28.1
- mcp[cli] >= 1.6.0

## API Source

This server uses the National Weather Service (NWS) API to fetch weather data. No API key is required.
