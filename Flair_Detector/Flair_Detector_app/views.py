from django.shortcuts import render
from .forms import *
from keras.models import load_model
import numpy as np
import nltk
import re
import pickle
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
import nltk
from .models import *
import os
nltk.download('stopwords')
from nltk.corpus import stopwords

stop = set(stopwords.words('english'))
from keras.preprocessing.sequence import pad_sequences


# Create your views here.


def remove_noise_test(x):
    with open('./tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    text = [" ".join(x.lower() for x in x[0].split())]
    text = [" ".join(x.strip() for x in text[0].split())]
    text = [" ".join(x for x in text[0].split() if x not in stop)]
    text = [re.sub(r"\[.*?\]", "", text[0])]
    text = [re.sub('[^a-zA-Z0-9\s]', '', text[0])]
    lm = WordNetLemmatizer()
    text = [lm.lemmatize(text[0])]
    text = tokenizer.texts_to_sequences(x)
    text = pad_sequences(text, maxlen=50, dtype='int32', value=0)
    return text


def check_flair(title):
    model = load_model('./best_model.hdf5')

    classes = np.array(
        ['AMA', 'AskIndia', 'Business/Finance', 'Food', 'Photography', 'Policy/Economy', 'Politics', 'Scheduled',
         'Science/Technology', 'Sports'], dtype=object)
    x = [title]

    text = remove_noise_test(x)

    ans = model.predict(text, batch_size=1, verbose=2)
    return classes[ans[0].argmax()]


def index(request):
    form = get_title()
    if request.method == "POST":
        form = get_title(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            import praw
            reddit = praw.Reddit(client_id='Use yours', client_secret='Use yours',
                                 user_agent='Use yours')

            submission = reddit.submission(url=link)

            flair = check_flair(str(submission.title))
            return render(request, 'index.html', {'form': form, 'title': str(submission.title), 'mess': flair})
    return render(request, 'index.html', {'form': form, 'title': None, 'mess': None})

class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            filepath = dict(file_serializer.data)['files']
            txt_file = open(f".{filepath}", 'r')
            lines = txt_file.readlines()
            import praw
            reddit = praw.Reddit(client_id='Use yours', client_secret='Use yours',
                                 user_agent='Use yours')

            output = {}

            for line in lines:
                sub = reddit.submission(url=line)

                flair = check_flair(str(sub.title))
                output[line] = flair

            objs = File.objects.all()
            objs = [i for i in objs]
            objs[-1].delete()
            txt_file.close()
            os.remove(f".{dict(file_serializer.data)['files']}")
            return Response(output, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
