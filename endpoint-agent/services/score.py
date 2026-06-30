def calculate_score(results):

    score = 100

    if not results["firewall"]["enabled"]:
        score -= 25

    if not results["defender"]["enabled"]:
        score -= 20

    if not results["updates"]["updated"]:
        score -= 15

    if len(results["ports"]["open_ports"]) > 5:
        score -= 10

    if score >= 90:
        risk = "Low"

    elif score >= 70:
        risk = "Medium"

    else:
        risk = "High"

    return {
        "security_score": score,
        "risk": risk
    }