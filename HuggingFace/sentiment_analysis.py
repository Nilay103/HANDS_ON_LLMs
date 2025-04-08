import json
from transformers import pipeline


classifier = pipeline(task="sentiment-analysis")
print(classifier(inputs="What a catch!"))
print(classifier(inputs="Uhh, So frustrating!"))
print(classifier(inputs="Noob, you should focus more"))


classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

print(json.dumps(classifier(inputs="What an annoying person")))
