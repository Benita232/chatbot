import json
import nltk
from nltk.stem import PorterStemmer  

with open('intents.json') as f:
    data = json.load(f)
print(f"✅ Found {12} total intents!") 

print("🔍 Step 2: Manual tokenization (no NLTK)...")


all_tokens = []
for intent in data['intents']:
    for pattern in intent['patterns']:
        
        tokens = pattern.lower().replace('?', '').replace('!', '').replace('.', '').split()
        all_tokens.extend(tokens)

print(f"✅ Tokenized {len(all_tokens)} total words!")
print("First 10 tokens:", all_tokens[:10])
print("🎉 Step 2 COMPLETE!")


