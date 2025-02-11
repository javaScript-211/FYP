# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


class EmotionDetector2:
    def __init__(self, model_name="Sungjin228/roberta-finetuned-sem_eval-english"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.emotion_labels = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 
                               'caring', 'confusion', 'curiosity', 'desire', 'disappointment', 
                               'disapproval', 'disgust', 'embarrassment', 'excitement', 
                               'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 
                               'optimism', 'pride', 'realization', 'relief', 'remorse', 
                               'sadness', 'surprise', 'neutral']

    def detect_emotion(self, text, top_n=3):
        inputs = self.tokenizer(text, return_tensors="pt")

        with torch.no_grad():
            outputs = self.model(**inputs)

        results = outputs.logits
        probResult = torch.softmax(results, dim=-1)[0] 
        
        sortedProb, sortedValue = torch.sort(probResult, descending=True)
    
        if top_n:
            sortedProb = sortedProb[:top_n]
            sortedValue = sortedValue[:top_n]
            emotions = []
            probabilities = []

            for prob, idx in zip(sortedProb, sortedValue):
                emotions.append(self.emotion_labels[idx.item()])
                probabilities.append(prob.item())
                
        return (emotions[0], probabilities[0]), (emotions[1], probabilities[1]), (emotions[2], probabilities[2])
    


text = "I believe that the module is not the best. The content does not expand on topics that they mentioned. It felt very surface level and wasted time "
n=3
emote = EmotionDetector2()
emotions1, emotions2, emotions3 = emote.detect_emotion(text,n)
print(emotions1, emotions2, emotions3)