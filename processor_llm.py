from dotenv import load_dotenv
from groq import Groq
load_dotenv()  # Load environment variables from .env file

groq = Groq()


def classify_log_message_with_llm(log_message):
    """
    Classifies a log message using a language model and returns the target label.
    If no pattern matches, returns 'other'.
    """
    prompt = f"""Classify the following log message into one of these categories: ['Workflow error', 'Deprecation warning'].
    If it does not fit any of these categories, classify it as 'Unclassified'.
    Only respond with the category name. No preamble.
    Log message: {log_message}"""

    chat_completion = groq.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    
    response = chat_completion.choices[0].message.content.strip().lower()
    return response



if __name__ == "__main__":
    logs = [
        "Case escalation rule execution failed for ticket ID 980745 because of a assigned support staff not responding.",
        "The 'oldFunction' will be removed in future releases. Please use 'newFunction' instead.",
        "Random log message with no specific pattern."
    ]
    
    for log in logs:
        print(f"Log Message: {log}")
        print(f"Classification: {classify_log_message_with_llm(log)}")