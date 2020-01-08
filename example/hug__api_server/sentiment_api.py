import hug
import torch
from keras.models import load_model

# intialisation
# fetch tokenizer
# Download vocabulary from S3 and cache.
loaded_tokenizer = torch.hub.load('huggingface/pytorch-transformers', 'tokenizer', 'bert-base-uncased')   

# fetch bert model
loaded_bert_model = torch.hub.load('huggingface/pytorch-transformers', 'model', 'bert-base-uncased') 

# fetch keras model
loaded_keras_model = load_model("trained_sentiment_classifier.h5")

# text --> tokens
def text_tokenization(text, tokenizer_model=loaded_tokenizer):
    tokenized_ids = tokenizer_model.encode(text, add_special_tokens=True)
    return tokenized_ids

    # tokens --> encode vector
def tokens_encoding(tokenized_ids, bert_model=loaded_bert_model):
    input_ids = torch.tensor([tokenized_ids])
    with torch.no_grad():
        # only the pooled vector at position 0: [CLS]
        encoding = bert_model(input_ids)[0][:,0,:].numpy()
    encoding = encoding.reshape((1, 768))
    return encoding

def predict_sentiment(encoding, keras_model=loaded_keras_model):
    sentiment_prob = keras_model.predict(encoding)
    return sentiment_prob

@hug.post("/sentiment")
def sentiment(text):
    token_ids = text_tokenization(text)
    encoding = tokens_encoding(token_ids)
    sentiment_prob = predict_sentiment(encoding)
    return {'sentiment': sentiment_prob}