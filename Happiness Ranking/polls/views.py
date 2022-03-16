from django.shortcuts import render, redirect
import pandas as pd
import pickle

# Create your views here.
def first(request):
    res = 0
    if request.method == 'POST':
        if request.POST.get('pred_button'):
            name = request.POST['Country Name']
            region = request.POST['Region']
            HapScore = request.POST['hapScore']
            standerror = request.POST['se']
            economy = request.POST['eco']
            family = request.POST['fam']
            lifeExp = request.POST['life']
            freedom = request.POST['free']
            government = request.POST['gov']
            generosity = request.POST['Gen']
            dystopia = request.POST['dys']

            if name != "":
                df = pd.DataFrame(columns=['Happiness Score', 'Standard Error',
                                               'Economy (GDP per Capita)', 'Family',
                                               'Health (Life Expectancy)', 'Freedom', 'Generosity',
                                               'Dystopia Residual'])

                df2 = {'Happiness Score': float(HapScore), 'Standard Error': float(standerror),
                           'Economy (GDP per Capita)': float(economy), 'Family': float(family),
                            'Health (Life Expectancy)': float(lifeExp), 'Freedom': float(freedom),
                           'Generosity': float(generosity), 'Dystopia Residual': float(dystopia)}

                df = df.append(df2, ignore_index=True)
                # Loading StandardScaler Model
                sc = pickle.load(open(r'polls/HappinessScaler.pickle', 'rb'))
                temp = sc.fit_transform(df)

                # load the model from disk
                filename = 'polls/HappinessModel.pickle'
                loaded_model = pickle.load(open(filename, 'rb'))
                res = loaded_model.predict(temp)
                res = int(abs(res))
        else:
            return redirect('homepage')
    else:
        pass

    return render(request, 'index.html', {'result': res})
