from sentence_transformers import SentenceTransformer
import joblib

# Generate embeddings for the log messages (assuming the column is named 'log_message')
model = SentenceTransformer('all-MiniLM-L6-v2')
classifier_model = joblib.load('models/logistic_regression_model.joblib')


def classify_log_message_with_bert(log_message):
    """
    Classifies a log message using BERT embeddings and returns the target label.
    If no pattern matches, returns 'other'.
    """
    
    embeddings = model.encode([log_message])
    predicted_label = classifier_model.predict(embeddings)
    probabilities = classifier_model.predict_proba(embeddings)[0]
    if max(probabilities) < 0.5:
        return 'Unclassified'
    # print(f"Probabilities: {probabilities}")
    return predicted_label[0]


if __name__ == "__main__":
    logs = [
        "User User123 logged in.",
        "http status 500: Internal Server Error",
        "Email service failed transmission to the user.",
        "Unauthorized access attempt detected.",
        "Account experienced multiple failed login attempts.",
        "Random log message with no specific pattern."
    ]
    
    for log in logs:
        print(f"Log Message: {log}")
        print(f"Classification: {classify_log_message_with_bert(log)}")



     