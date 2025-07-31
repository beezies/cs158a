import socket
import ssl
import certifi

hostname = 'www.google.com'
port = 443
buf = 64
context = ssl.create_default_context(cafile=certifi.where())

with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(f"Connected to {hostname} with SSL.")
        request = f"GET / HTTP/1.1\r\nHost: {hostname}\r\nConnection: close\r\n\r\n"
        ssock.sendall(request.encode())
        response = b""
        while True:
            data = ssock.recv(buf)
            if not data:
                break
            response += data
response = response.decode('utf-8')
headers, _, body = response.partition("\r\n\r\n")

with open("response.html", "w") as f:
    f.write(body)

print("Saved response to response.html.")
