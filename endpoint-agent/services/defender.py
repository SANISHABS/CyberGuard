import subprocess


def get_defender_status():
    try:
        command = [
            "powershell",
            "-Command",
            "Get-MpComputerStatus | Select-Object AntivirusEnabled,RealTimeProtectionEnabled | ConvertTo-Json"
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return {
                "module": "Windows Defender",
                "status": "Unknown",
                "enabled": False,
                "real_time": False,
                "recommendation": "Unable to retrieve Windows Defender status."
            }

        import json
        data = json.loads(result.stdout)

        enabled = data.get("AntivirusEnabled", False)
        real_time = data.get("RealTimeProtectionEnabled", False)

        if enabled and real_time:
            status = "Protected"
            recommendation = "No action required."
        else:
            status = "At Risk"
            recommendation = "Enable Windows Defender and Real-Time Protection."

        return {
            "module": "Windows Defender",
            "status": status,
            "enabled": enabled,
            "real_time": real_time,
            "recommendation": recommendation
        }

    except Exception as e:
        return {
            "module": "Windows Defender",
            "status": "Error",
            "enabled": False,
            "real_time": False,
            "recommendation": str(e)
        }