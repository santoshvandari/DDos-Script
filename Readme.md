# SYN Flood DDoS Attack Script with IP Spoofing

This script performs a SYN Flood Distributed Denial of Service (DDoS) attack by sending multiple TCP SYN packets to the target IP with spoofed source IP addresses. The attack is designed to flood the target with incomplete TCP connections, overwhelming the server and potentially making it unresponsive.

**Important:** This script is intended for educational purposes only. Unauthorized use of DDoS tools is illegal and can lead to severe consequences.

## Features

- **IP Spoofing**: Generates random source IP addresses to make the attack harder to mitigate.
- **Random Ports**: Uses random source ports to avoid rate-limiting.
- **Multithreading**: Spawns multiple threads to increase the load on the target server.
- **TCP/IP Header Construction**: Manually constructs IP and TCP headers to simulate a SYN packet with customizable fields.
- **Domain Resolution**: Converts the target domain name into an IP address before launching the attack.

## How the Attack Works

1. **IP Spoofing**: The source IP in the packet is faked, making it difficult for the target to block requests based on the source IP.
2. **SYN Flooding**: Sends a massive number of SYN packets to the target server, initiating the TCP handshake without completing it. This fills up the server's connection queue, preventing legitimate connections from being established.
3. **Random Delays**: Introduces random delays between sending packets to mimic a real user and avoid detection.

## Disclaimer

This tool is for **educational purposes only**. Performing a DDoS attack on a network or system without proper authorization is illegal and can lead to severe legal consequences. You should only use this tool on networks you own or have explicit permission to test.

## Requirements

- Python 3.0 r above
- Raw socket permissions (You might need to run this script with root privileges)
  
## Installation

Clone this repository and install the required dependencies (if any):

```bash
git clone https://github.com/santoshvandari/DDos-Script.git
cd DDos-Script
```

## Usage

Run the Script With Python

```bash
sudo python3 main.py -u <target-url> [-p <target-port>]
```
Arguments
-u, --url (required): The URL of the target website you want to attack.
-p, --port (optional): The target port number (default is port 80, commonly used for HTTP).

## Example
```bash
sudo python3 main.py -u example.com -p 80
```
This will send SYN flood packets to example.com on port 80.

## How to Stop the Attack
You can stop the attack by pressing Ctrl + C.

## Important Notes
This script sends raw TCP packets, so you'll need to run it with root/administrator privileges.
Ensure that your firewall settings allow you to send raw packets.
Do not use this tool maliciously.


## Contributing
We welcome contributions! If you'd like to contribute to this Mero Share IPO Filler Script, please check out our [Contribution Guidelines](Contribution.md).

## Code of Conduct
Please review our [Code of Conduct](CodeOfConduct.md) before participating in this Script.

## License
This project is licensed under the MIT [License](LICENSE).




