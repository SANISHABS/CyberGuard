def calculate_security_score(firewall_enabled,
                             defender_enabled,
                             updates_ok):

    score = 0

    # Firewall = 40 points
    if firewall_enabled:
        score += 40

    # Defender = 40 points
    if defender_enabled:
        score += 40

    # Windows Updates = 20 points
    if updates_ok:
        score += 20

    # Risk level
    if score >= 80:
        risk = "Low"
    elif score >= 50:
        risk = "Medium"
    else:
        risk = "High"

    return {
        "security_score": score,
        "risk": risk
    }