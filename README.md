# Synchronized Music Player

A networked music player that allows multiple clients to play the same song in perfect synchronization. Search for songs on YouTube Music and stream them across multiple connected devices on the same network.

## Features

- **Multi-Client Support**: Connect multiple devices to a central server
- **Synchronized Playback**: All connected clients play the same song at the same time
- **YouTube Music Search**: Search for and play any song from YouTube Music
- **Pause/Resume Control**: Control playback across all connected clients
- **Network-Based**: Works across devices on the same WiFi network

## Project Structure

- `startServer.py` - Entry point for the server
- `server.py` - Server implementation that manages client connections and broadcasts play commands
- `main.py` - Client application with command-line interface
- `client.py` - Client socket implementation that connects to the server
- `getStreamUrl.py` - Retrieves streaming URLs from YouTube Music using yt-dlp
- `searchsong.py` - Searches YouTube Music for songs

## Requirements

- Python 3.x
- `mpv` - Music/video player library
- `mpv-2.dll` - Must be present in your project root directory

### Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Download and place `mpv-2.dll` in your project root directory

## Usage

### Starting the Server

Run the server on the machine that will host the music player:

```bash
python startServer.py
```

The server will display its IP address. Share this IP with other clients.

### Starting Clients

On each client device, run:

```bash
python main.py
```

When prompted, enter the server's IP address.

### Commands

Once connected, use the following commands in the client:

- `!play` - Search for and play a song
  - Enter the song name when prompted
  - The song will start playing on all connected clients
- `!p` - Pause or resume playback on all clients
- `!q` - Exit the client

## How It Works

1. **Server Connection**: Each client connects to the server at the specified IP address and port (5050)
2. **Song Search**: When a song is requested, the client searches YouTube Music for the best match
3. **Stream Retrieval**: The streaming URL is obtained using yt-dlp
4. **Broadcast**: The server sends the song to all connected clients with a synchronized timestamp
5. **Playback**: All clients download and play the song at the exact same time
6. **Synchronization**: Timestamps ensure all clients start playback simultaneously

## Network Requirements

- All devices must be on the same WiFi network
- Server must be accessible on port 5050 (default)
- Internet connection required to search and stream from YouTube

## Notes

- The first client to connect will start the server connection process
- Use device IPs on the same local network for best results
- Ensure firewall settings allow port 5050 communication
- Song synchronization accuracy depends on network latency and client processing power
