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
                "status": "Unknown",
                "enabled": False,
                "recommendation": "Unable to retrieve Windows Defender status."
            }

        import json

        data = json.loads(result.stdout)

        enabled = data["AntivirusEnabled"]
        realtime = data["RealTimeProtectionEnabled"]

        return {
            "status": "Protected" if enabled else "Disabled",
            "enabled": enabled,
            "real_time": realtime,
            "recommendation":
                "No action required."
                if enabled
                else "Enable Microsoft Defender."
        }

    except Exception as e:
        return {
            "status": "Unknown",
            "enabled": False,
            "recommendation": str(e)
        }