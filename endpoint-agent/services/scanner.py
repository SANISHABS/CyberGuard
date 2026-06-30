from services.firewall import get_firewall_status
from services.defender import get_defender_status
from services.updates import get_update_status
from services.ports import scan_ports
from services.score import calculate_score


def run_scan():

    firewall = get_firewall_status()
    defender = get_defender_status()
    updates = get_update_status()
    ports = scan_ports()

    results = {
        "firewall": firewall,
        "defender": defender,
        "updates": updates,
        "ports": ports
    }

    score = calculate_score(results)

    return {
        "scan": results,
        "score": score
    }