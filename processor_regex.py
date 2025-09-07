import re

def classify_log_message_with_regex(log_message):
    """
    Classifies a log message using regex patterns and returns the target label.
    If no pattern matches, returns 'other'.
    """
    patterns = [
        (r'User User\d+ logged (in|out).', 'User Action'),
        (r'http status|wsgi\.server', 'HTTP Status'),
        (r'email service|failed transmission', 'Critical Error'),
        (r'unauthorized access|failed login|account experienced multiple failed', 'Security Alert'),
    ]
    for pattern, label in patterns:
        if re.search(pattern, log_message, re.IGNORECASE):
            return label
    return None



if __name__ == "__main__":
    test_messages = [
        "User User123 logged in successfully.",
        "http status 500: Internal Server Error",
        "Email service failed transmission to the user.",
    ]
    for msg in test_messages:
        print(f"Log Message: {msg}")
        print(f"Classification: {classify_log_message_with_regex(msg)}")        