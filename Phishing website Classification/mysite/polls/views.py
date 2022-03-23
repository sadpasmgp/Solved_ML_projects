from django.shortcuts import render, redirect
import pandas as pd
import pickle

def index_func(request):
    res = 0
    if request.method == 'POST':
        name = request.POST['name']
        NumDots = request.POST['NumDots']
        PathLevel = request.POST['PathLevel']
        NumDash = request.POST['NumDash']
        NumSensitiveWords= request.POST['NumSensitiveWords']
        PctExtHyperlinks = request.POST['PctExtHyperlinks']
        PctExtResourceUrls= request.POST['PctExtResourceUrls']
        InsecureForms = request.POST['InsecureForms']
        tooLong = request.POST['PctNullSelfRedirectHyperlinks']
        freq = request.POST['FrequentDomainNameMismatch']
        SubmitInfoToEmail = request.POST['SubmitInfoToEmail']
        IframeOrFrame = request.POST['IframeOrFrame']

        if name != "":
            df = pd.DataFrame(columns=['NumDots','PathLevel','NumDash','NumSensitiveWords',
                                       'PctExtHyperlinks','PctExtResourceUrls','InsecureForms',
                                       'PctNullSelfRedirectHyperlinks','FrequentDomainNameMismatch',
                                       'SubmitInfoToEmail','IframeOrFrame'])

            df2 = {'NumDots': float(NumDots),'PathLevel': float(PathLevel),'NumDash': float(NumDash),
                   'NumSensitiveWords': float(NumSensitiveWords),'PctExtHyperlinks': float(PctExtHyperlinks)
                    ,'PctExtResourceUrls': float(PctExtResourceUrls),'InsecureForms': float(InsecureForms),
                    'PctNullSelfRedirectHyperlinks': float(tooLong),'FrequentDomainNameMismatch':
                       float(freq),'SubmitInfoToEmail': float(SubmitInfoToEmail),'IframeOrFrame': float(IframeOrFrame)}

            df = df.append(df2, ignore_index=True)
            # load the model from disk
            filename1 = 'polls/Phishing.pickle'
            loaded_model = pickle.load(open(filename1, 'rb'))
            res = loaded_model.predict(df)
            # print(res)
            if res[0] == 1:
                res = True
            else:
                res = False

            print(res)

        else:
            return redirect('homepage')
    else:
        pass

    return render(request, "index.html", {'response': res})