import socket

AS_IP = "127.0.0.1"
AS_PORT = 53533

# registration_request = "TYPE=A\nNAME=freelancepromarket.com\nVALUE=IP_ADDRESS\nTTL=10"
registration_request = "TYPE=A\nNAME=fibonacci.com"

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    udp_socket.sendto(registration_request.encode(), (AS_IP, AS_PORT))

    response, address = udp_socket.recvfrom(1024)
    print(response.decode())

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the UDP socket
    udp_socket.close()
