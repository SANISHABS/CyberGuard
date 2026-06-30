import subprocess

ALLOWED_ACTIONS = {
    "enable_firewall": "netsh advfirewall set allprofiles state on",
}

def execute_action(action: str):
    if action not in ALLOWED_ACTIONS:
        return {
            "success": False,
            "message": "Action not allowed."
        }

    try:
        subprocess.run(
            ALLOWED_ACTIONS[action],
            shell=True,
            check=True
        )

        return {
            "success": True,
            "message": f"{action} executed successfully."
        }

    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }