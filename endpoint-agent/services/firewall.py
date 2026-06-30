import subprocess


def get_firewall_status():
    """
    Returns Windows Firewall status.
    """

    try:

        result = subprocess.run(
            ["netsh", "advfirewall", "show", "allprofiles"],
            capture_output=True,
            text=True
        )

        output = result.stdout

        if "State ON" in output:

            return {
                "enabled": True,
                "status": "Protected",
                "recommendation": "Windows Firewall is enabled."
            }

        else:

            return {
                "enabled": False,
                "status": "Risk",
                "recommendation": "Enable Windows Firewall."
            }

    except Exception as e:

        return {
            "enabled": False,
            "status": "Unknown",
            "recommendation": str(e)
        }


def enable_firewall():

    subprocess.run(
        [
            "netsh",
            "advfirewall",
            "set",
            "allprofiles",
            "state",
            "on"
        ]
    )

    return {
        "message": "Firewall Enabled"
    }