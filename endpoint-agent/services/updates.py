import subprocess


def get_update_status():
    try:
        command = [
            "powershell",
            "-Command",
            "Get-Service wuauserv | Select-Object Status | ConvertTo-Json"
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode != 0:
            return {
                "module": "Windows Update",
                "status": "Unknown",
                "recommendation": "Unable to retrieve update status."
            }

        if "Running" in result.stdout:
            status = "Updated"
            recommendation = "No action required."
        else:
            status = "Check Updates"
            recommendation = "Enable Windows Update service."

        return {
            "module": "Windows Update",
            "status": status,
            "recommendation": recommendation
        }

    except Exception as e:
        return {
            "module": "Windows Update",
            "status": "Error",
            "recommendation": str(e)
        }