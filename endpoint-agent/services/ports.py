import socket

# Common ports and associated services
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
    port_results = []

    try:
        for port, service in COMMON_PORTS.items():

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            try:
                result = sock.connect_ex((host, port))

                if result == 0:

                    risk = "Low"
                    recommendation = "No action required."

                    # High-risk ports
                    if port == 445:
                        risk = "High"
                        recommendation = "Disable SMB if not required."

                    elif port == 3389:
                        risk = "Medium"
                        recommendation = (
                            "Disable Remote Desktop if not required."
                        )

                    elif port in [21, 23]:
                        risk = "Medium"
                        recommendation = (
                            "Avoid insecure protocols if possible."
                        )

                    port_results.append({
                        "port": port,
                        "service": service,
                        "status": "Open",
                        "risk": risk,
                        "recommendation": recommendation
                    })

            except Exception:
                continue

            finally:
                sock.close()

        return {
            "host": host,
            "total_open_ports": len(port_results),
            "ports": port_results
        }

    except Exception as e:

        return {
            "host": host,
            "total_open_ports": 0,
            "ports": [],
            "error": str(e)
        }