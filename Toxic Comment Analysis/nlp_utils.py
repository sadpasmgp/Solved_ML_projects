import nltk
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer
from nltk.corpus import stopwords
import string
import re

CONTRACTION_MAP = {
"ain't": "is not",
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he would",
"he'd've": "he would have",
"he'll": "he will",
"he'll've": "he he will have",
"he's": "he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how is",
"I'd": "I would",
"I'd've": "I would have",
"I'll": "I will",
"I'll've": "I will have",
"I'm": "I am",
"I've": "I have",
"i'd": "i would",
"i'd've": "i would have",
"i'll": "i will",
"i'll've": "i will have",
"i'm": "i am",
"i've": "i have",
"isn't": "is not",
"it'd": "it would",
"it'd've": "it would have",
"it'll": "it will",
"it'll've": "it will have",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she would",
"she'd've": "she would have",
"she'll": "she will",
"she'll've": "she will have",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so as",
"that'd": "that would",
"that'd've": "that would have",
"that's": "that is",
"there'd": "there would",
"there'd've": "there would have",
"there's": "there is",
"they'd": "they would",
"they'd've": "they would have",
"they'll": "they will",
"they'll've": "they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we would",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what will",
"what'll've": "what will have",
"what're": "what are",
"what's": "what is",
"what've": "what have",
"when's": "when is",
"when've": "when have",
"where'd": "where did",
"where's": "where is",
"where've": "where have",
"who'll": "who will",
"who'll've": "who will have",
"who's": "who is",
"who've": "who have",
"why's": "why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you would",
"you'd've": "you would have",
"you'll": "you will",
"you'll've": "you will have",
"you're": "you are",
"you've": "you have"
}

# removing contractions
conm = CONTRACTION_MAP
def contraction_remove(sample_text):
    for key,value in conm.items():
        sample_text = re.sub(r"{}".format(key),'{}'.format(value),sample_text)
        
    return sample_text

# word tokenization
special = string.punctuation
def w_tokenization(sentence):
    # convert into lower case
    sentence = sentence.lower()
    # contraction
    sentence = contraction_remove(sentence)
    # 
    tokens = nltk.word_tokenize(sentence) # word tokens
    # step-1: compare
    without_special = []
    for word in tokens:
        if word not in special:
            without_special.append(word)

    return without_special

# stemming
def stemming(sentence):
    tokens = w_tokenization(sentence)
    stem_words = []
    for w in tokens:
        stem_words.append(snow.stem(w))

    return " ".join(stem_words)

# lemmatization
lemma = WordNetLemmatizer() # initilizing word net
def lemmatization_sentence(sentence):#,stopwords,stop=True):
    # computing parts of speech
    tokens = w_tokenization(sentence)
    tag_list = pos_tag(tokens,tagset=None)
    lema_sent =[] # initizaing empty list

    for token,pos_token in tag_list:
        #if token not in stopwords:

        if pos_token.startswith('V'): # verb
            pos_val = 'v'
        elif pos_token.startswith('J'): # adjective
            pos_val = 'a'
        elif pos_token.startswith('R'): # adverb
            pos_val = 'r'
        else:# any parts of speech except verb, adjective, adverb
            pos_val = 'n'

        lema_token = lemma.lemmatize(token,pos_val) # computing lematization
        lema_sent.append(lema_token) # append values in list
    return " ".join(lema_sent)