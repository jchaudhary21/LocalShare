# LocalShare

LocalShare is a utility tool designed for sharing files and small data snippets between devices on the same network.

## Project Overview

LocalShare utilizes Flask to create a local server on a host device. All shared files are temporarily stored on the host device and can be deleted once sharing is complete.

## Requirements
The project has been tested with the following environment:

    1. Python 3.8.10
    2. Flask 3.0.3

## Setup Instructions

1. Clone the project:
   ```bash
   git clone https://github.com/jchaudhary21/LocalShare.git
   ```

2. Install Flask ()
    ```bash
    pip install flask==3.0.3
    ```

3. Open your `.bashrc` file:
   ```bash
   nano ~/.bashrc
   ```

4. Add a function at the bottom of the file:
   ```bash
   LocalShare() {
     # Insert the path to your local-share.bash file here
   }
   ```
![bashrc ss](/assets/bashrc_ss.png)

4. Save the file (Ctrl + S) and exit the editor (Ctrl + X).

5. Source your updated `.bashrc` file:
   ```bash
   source ~/.bashrc
   ```

## Usage

1. Run the `LocalShare` command in your terminal.

2. You'll see a local IP address displayed, formatted as: `192.168.x.xxx:5000`

3. Access this IP address from a web browser on any device connected to the same network.

4. You can now view available files or upload new ones through the web interface.

![bashrc ss](/assets/LocalShare_ss.png)


