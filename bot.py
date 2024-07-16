import socket

def main():
    host = '172.18.1.121'  # Replace with the server's IP address
    port = 12345
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        print("Connected to main program")
    except socket.gaierror as e:
        print(f"Address-related error connecting to server: {e}")
    except socket.error as e:
        print(f"Connection error: {e}")
        return

    try:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            print(f"New input: {data.decode('utf-8')}")
    except KeyboardInterrupt:
        print("\nBot shutting down...")
    finally:
        sock.close()

if __name__ == "__main__":
    main()
