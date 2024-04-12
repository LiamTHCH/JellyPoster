# JellyPoster
## Jellyfin Poster Display
### Overview

Jellyfin Poster Display is a small Python program designed to work seamlessly with Jellyfin media server. It fetches the poster image of the content being played on specified devices and displays it in real-time. This tool enhances the viewing experience by providing visual cues about the currently playing content.
Features

    Real-time Poster Display: Automatically fetches and displays the poster image of the content currently being played on specified Jellyfin devices.

    Customizable: Users can specify the Jellyfin server URL, API key, and target devices to monitor.

### Requirements

    Python 3.x
    Jellyfin media server with API access enabled
    Requests library

### Installation

    Clone this repository to your local machine.
    Install the required dependencies by running:

```    bash
    pip install -r requirements.txt
```
## Usage

    Create a .env file in the root directory of the project.
    Populate the .env file with the following variables:

   ``` plaintext

JELLYFIN_URL="https://your_jellyfin_server_url"
API_KEY="your_jellyfin_api_key"
CLIENT_IP="your_client_ip"
```
Modify the CLIENT_IP variable to match the IP address of the device where you want to run the script.
Run the server script by executing:

bash

python server.py

Sit back and enjoy as the program displays the posters of the content being played on your specified devices.
