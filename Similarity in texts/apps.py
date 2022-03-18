from django.apps import AppConfig
import pickle
import os


word_embed = None
def startup():
    # This file has the information on every common word and its embeddings.
    save_data = open(r"polls/word_embeddings_smaller.pickle", "rb")
    global word_embed
    word_embed = pickle.load(save_data)
    # print(word_embed['the'])
    save_data.close()


class PollsConfig(AppConfig):
    name = 'polls'
    verbose_name = "My Application"

    def ready(self):
        if os.environ.get('RUN_MAIN'):
            startup()
