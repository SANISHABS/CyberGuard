import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "Remote Desktop",
    8000: "CyberGuard",
    8080: "HTTP Alternate"
}

def scan_ports(host="127.0.0.1"):
    results = []

    for port, service in COMMON_PORTS.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((host, port))

        if result == 0:

            risk = "Low"
            recommendation = "No action required."

            if port == 445:
                risk = "High"
                recommendation = "Disable SMB if not required."

            elif port == 3389:
                risk = "Medium"
                recommendation = "Disable Remote Desktop if not required."

            results.append({
                "port": port,
                "service": service,
                "status": "Open",
                "risk": risk,
                "recommendation": recommendation
            })

        sock.close()

    return results