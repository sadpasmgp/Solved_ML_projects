# Importing necessary libraries

from nltk.corpus import stopwords
import re
import numpy as np


def Cleaning(text):
  def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


  def replaceUrls(data):
      #Removing URLs with a regular expression
      url_pattern = re.compile(r'https?://\S+|www\.\S+')
      data = url_pattern.sub(r'', data)
      return data

  def removeEmail(data):
      # Remove Emails
      data = re.sub('\S*@\S*\s?', '', data)
      return data

  def misc(data):
      # Remove new line characters
      data = re.sub(r'\.+', ".", data)
      data = re.sub('\s+', ' ', data)
      # Remove distracting single quotes
      data = re.sub("\'", "", data)
      return data

  sentence = cleanhtml(text)
  sentence = replaceUrls(sentence)
  sentence = removeEmail(sentence)
  sentence = misc(sentence)
  sentence = re.sub(r'[^a-zA-Z]', ' ', sentence)
  sentence = re.sub(' +', ' ', sentence)
  sentence = sentence.lower()

  return sentence


# nltk.download('stopwords')


stopwords_list = stopwords.words('english')
def removeStopwords(sentence):
  words = sentence.split(" ")
  filtered_sentence = [word for word in words if not word in stopwords_list]
  ans = ' '.join([i for i in filtered_sentence if len(i) >= 2])

  return ans


# We will go for cosine_similarity
def cosine_similarity(A, B):
    """
    Input:
        A: a numpy array which corresponds to a word vector
        B: A numpy array which corresponds to a word vector
    Output:
        cos: numerical number representing the cosine similarity between A and B.
    """
    dot = round(np.dot(A, B), 3)
    norma = round(np.sqrt(np.dot(A, A)), 3)
    normb = round(np.sqrt(np.dot(B, B)), 3)
    print(dot)
    print(norma, normb)
    cos = round(dot / (norma * normb), 3)

    return cos