from processor_regex import classify_log_message_with_regex
from processor_bert import classify_log_message_with_bert
from processor_llm import classify_log_message_with_llm
import pandas as pd

def classify(log_messages):

    labels = []
    for source, message in log_messages:
        classified_label = classify_logs(source, message)
        labels.append(classified_label)
    return labels
        


def classify_logs(source, message):
    if source == "LegacyCRM":
        return classify_log_message_with_llm(message)
    else:
        label = classify_log_message_with_regex(message)
        if label is None:
            label = classify_log_message_with_bert(message)
        return label


def classify_from_csv(csv_file_path):
    df = pd.read_csv(csv_file_path)
    log_messages = list(zip(df['source'], df['log_message'])) # list of tuples (source, log_message)
    df['target_label'] = classify(log_messages)
    df.to_csv('resources/output.csv', index=False)


if __name__ == "__main__":

    classify_from_csv('resources/test.csv')
    # logs = [
    #     ("User Action", "User User123 logged in successfully."),
    #     ("HTTP Status", "http status 500: Internal Server Error"),
    #     ("Critical Error", "Email service failed transmission to the user."),
    #     ("Security Alert", "Unauthorized access attempt detected."),
    #     ("Security Alert", "Account experienced multiple failed login attempts."),
    #     ("LegacyCRM", "Case escalation rule execution failed for ticket ID 980745 because of a assigned support staff not responding."),
    #     ("LegacyCRM", "The 'oldFunction' will be removed in future releases. Please use 'newFunction' instead."),
    #     ("LegacyCRM", "Random log message with no specific pattern."),


    # ]
    
    # # classified_logs = classify(logs)  
    # classified_logs = classify_from_csv('test.csv')
    # # print(classified_logs)
    # for log, classification in zip(logs, classified_logs):
    #     print(f"Log Source: {log[0]}, Log Message: {log[1]}")
    #     print(f"Classification: {classification}")