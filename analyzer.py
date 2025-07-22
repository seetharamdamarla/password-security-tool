from zxcvbn import zxcvbn

def analyze_password_strength(password):
    if not password:
        return "No password provided."

    result = zxcvbn(password)
    score = result.get('score', 0)
    guesses = result.get('guesses', 'N/A')
    crack_time = result['crack_times_display'].get('offline_slow_hashing_1e4_per_second', 'N/A')
    feedback = result.get('feedback', {})
    entropy = result.get('entropy')  # May be None

    score_meaning = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Strong",
        4: "Very Strong"
    }

    result_text = f"""
Password: {password}
Score: {score}/4 ({score_meaning.get(score, 'Unknown')})
Estimated Crack Time: {crack_time}
Guesses Needed: {guesses}
"""

    if entropy is not None:
        result_text += f"Entropy: {entropy:.2f} bits\n"

    if feedback.get('warning'):
        result_text += f"Warning: {feedback['warning']}\n"
    if feedback.get('suggestions'):
        result_text += f"Suggestions: {', '.join(feedback['suggestions'])}\n"

    return result_text.strip()
