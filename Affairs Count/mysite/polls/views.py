from django.shortcuts import render, redirect
import pandas as pd
import pickle

# Create your views here.
def index_func(request):
    res = 0
    if request.method == 'POST':
        name = request.POST['Name']
        age = request.POST['age']
        years_marr = request.POST['years_marr']
        child = request.POST['child']
        education = request.POST['education']
        occu_level = request.POST['occu_level']
        rate_marr = request.POST['rate_marr']
        religion_type = request.POST['religion_type']
        occu_hus_level = request.POST['occu_hus_level']

        if name != "":
            df = pd.DataFrame(columns=['age', 'yrs_married', 'children', 'educ', 'occupation',
                                       'rate_1.0', 'rate_2.0', 'rate_3.0', 'rate_4.0', 'rate_5.0',
                                       'religion_1.0', 'religion_2.0', 'religion_3.0', 'religion_4.0',
                                       'husb_occ_1.0', 'husb_occ_2.0', 'husb_occ_3.0', 'husb_occ_4.0',
                                       'husb_occ_5.0', 'husb_occ_6.0'])

            rate = helperRate(int(rate_marr))
            rel = helperReligion(int(religion_type))
            hus = helperOccupationHusband(int(occu_hus_level))

            df2 = {'age': float(age), 'yrs_married': float(years_marr), 'children': float(child),
                   'educ': float(education), 'occupation': float(occu_level), 'rate_1.0': rate[0],
                   'rate_2.0': rate[1], 'rate_3.0': rate[2], 'rate_4.0': rate[3], 'rate_5.0': rate[4],
                    'religion_1.0': rel[0], 'religion_2.0': rel[1], 'religion_3.0': rel[2],
                   'religion_4.0': rel[3], 'husb_occ_1.0': hus[0], 'husb_occ_2.0': hus[1],
                   'husb_occ_3.0': hus[2], 'husb_occ_4.0': hus[3], 'husb_occ_5.0': hus[4],
                   'husb_occ_6.0': hus[5]}

            df = df.append(df2, ignore_index=True)
            # load the model from disk
            filename = 'polls/AffairsPCA.pickle'
            pca = pickle.load(open(filename, 'rb'))
            data = pca.transform(df)
            filename1 = 'polls/Affairs.pickle'
            loaded_model = pickle.load(open(filename1, 'rb'))

            res = loaded_model.predict(data)
            res = int(res)
            print(res)

        else:
            return redirect('homepage')
    else:
        pass

    return render(request, "index.html", {'response': res})










def helperRate(x):
    if x == 1:
        return [1, 0, 0, 0, 0]
    elif x == 2:
        return [0, 1, 0, 0, 0]
    elif x == 3:
        return [0, 0, 1, 0, 0]
    elif x == 4:
        return [0, 0, 0, 1, 0]
    else:
        return [0, 0, 0, 0, 1]


def helperReligion(x):
    if x == 1:
        return [1, 0, 0, 0]
    elif x == 2:
        return [0, 1, 0, 0]
    elif x == 3:
        return [0, 0, 1, 0]
    else:
        return [0, 0, 0, 1]


def helperOccupationHusband(x):
    if x == 1:
        return [1, 0, 0, 0, 0, 0]
    elif x == 2:
        return [0, 1, 0, 0, 0, 0]
    elif x == 3:
        return [0, 0, 1, 0, 0, 0]
    elif x == 4:
        return [0, 0, 0, 1, 0, 0]
    elif x == 5:
        return [0, 0, 0, 0, 1, 0]
    else:
        return [0, 0, 0, 0, 0, 1]