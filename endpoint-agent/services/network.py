import socket
import uuid
import subprocess


def get_network_info():
    try:
        # Host Name
        hostname = socket.gethostname()

        # IP Address
        ip_address = socket.gethostbyname(hostname)

        # MAC Address
        mac = ':'.join([
            '{:02X}'.format((uuid.getnode() >> ele) & 0xff)
            for ele in range(0, 48, 8)
        ][::-1])

        # Default Gateway
        gateway = "Not Available"

        try:
            result = subprocess.run(
                ["ipconfig"],
                capture_output=True,
                text=True
            )

            lines = result.stdout.splitlines()

            for i, line in enumerate(lines):

                if "Default Gateway" in line:

                    # Extract value after ':'
                    gw = line.split(":")[-1].strip()

                    # If IPv4 gateway is present in same line
                    if gw and "." in gw:
                        gateway = gw
                        break

                    # Otherwise check the next line
                    if i + 1 < len(lines):
                        next_line = lines[i + 1].strip()

                        if "." in next_line:
                            gateway = next_line
                            break

        except Exception:
            pass

        return {
            "hostname": hostname,
            "ip": ip_address,
            "mac": mac,
            "default_gateway": gateway
        }

    except Exception as e:

        return {
            "hostname": "Unknown",
            "ip": "Unknown",
            "mac": "Unknown",
            "default_gateway": "Unknown",
            "error": str(e)
        }