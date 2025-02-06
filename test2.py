from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

model_name = "michellejieli/emotion_text_classifier"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

label_mapping = {
    0: "sadness",
    1: "joy",
    2: "love",
    3: "anger",
    4: "fear",
    5: "surprise"
}

def classify_emotion(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    probabilities = F.softmax(logits, dim=1)

    predicted_class = torch.argmax(probabilities, dim=1).item()
    confidence_score = probabilities[0, predicted_class].item()

    return label_mapping.get(predicted_class, "Unknown Emotion"), confidence_score

if __name__ == "__main__":
    text = input("Enter a sentence: ")
    emotion, confidence = classify_emotion(text)
    print(f"Predicted Emotion: {emotion} (Confidence: {confidence:.4f})")
