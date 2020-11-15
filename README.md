# CBC-AES-MAC Demo

## Setup

1. Clone the code
1. Create a virtual environment. Execute inside the project folder:
    ```sh
    python3 -m venv venv
    ```
1. Install the dependencies.
    ```sh
    pip3 install -r requirements.txt
    ```
1. Run the program:
    * Server:
    ```sh
    ./run_server.sh
    ```
    * Client:
    ```sh
    python3 client.py <message-for-encryption>
    ```