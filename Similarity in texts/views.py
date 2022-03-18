from django.shortcuts import render
import numpy as np
from .apps import word_embed
from .utils import Cleaning, removeStopwords, cosine_similarity

def index_func(request):
    # print(word_embed['the'])
    similarity = 0
    if request.method == 'POST':
        text1 = request.POST['text1']
        text2 = request.POST['text2']

        pre_final1 = Cleaning(text1)
        pre_final1 = removeStopwords(pre_final1)
        print(pre_final1)

        pre_final2 = Cleaning(text2)
        pre_final2 = removeStopwords(pre_final2)
        print(pre_final2)

        count1 = 0
        document_embeddings1 = np.zeros(50, dtype=float)
        try:
            for word in pre_final1.split(" "):
                array = np.asarray(word_embed[word], dtype=float)
                document_embeddings1 = np.add(document_embeddings1, array, out=document_embeddings1, casting="unsafe")
        except:
            count1 = count1 + 1

        print("Number of words in text 1:", len(pre_final1.split(" ")))
        print("Unrecognizable word count in text 1:", count1)

        count2 = 0
        document_embeddings2 = np.zeros(50, dtype=float)
        try:
            for word in pre_final2.split(" "):
                array = np.asarray(word_embed[word], dtype=float)
                document_embeddings2 = np.add(document_embeddings2, array, out=document_embeddings2, casting="unsafe")
        except:
            count2 = count2 + 1

        print("Number of words in text 1:", len(pre_final2.split(" ")))
        print("Unrecognizable word count in text 2:", count2)

        similarity = cosine_similarity(document_embeddings1, document_embeddings2)
        print(similarity)

    else:
        pass

    return render(request, 'index.html', {'response': similarity})


# Links to look at, for startup code implementation:
# https://stackoverflow.com/questions/2781383/where-to-put-django-startup-code


