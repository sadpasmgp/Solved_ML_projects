from django.shortcuts import render, redirect
import pickle
import pandas as pd
import bz2

# Create your views here.
def first(request):
    res = 0
    if request.method == 'POST':
        if request.POST.get('pred_button'):
            latitude = request.POST['lat']
            longitude = request.POST['long']
            bright = request.POST['bright']
            daynight = request.POST['dn']
            frp = request.POST['frp']
            type_fire = request.POST['type_fire']
            scan = request.POST['scan']
            year = request.POST['year']
            month = request.POST['month']
            date = request.POST['date']

            if float(latitude) < 91 and float(latitude) >= -90:
                df = pd.DataFrame(columns=['Latitude', 'Longitude',
                                           'Brightness', 'Day or Night',
                                           'frp', 'type_2', 'type_3', 'scan',
                                           'year', 'month', 'date'])

                temp = helper(int(type_fire))
                df2 = {'Latitude': float(latitude), 'Longitude': float(longitude),
                       'Brightness': float(bright), 'Day or Night': int(daynight),
                       'frp': float(frp), 'type_2': temp[0], 'type_3': int(temp[1]),
                       'scan': int(scan), 'year': int(year), 'month': int(month),
                       'date': int(date)}

                df = df.append(df2, ignore_index=True)
                # load the model from disk
                filename = bz2.BZ2File('polls/ForestModel.bz2', 'rb')
                loaded_model = pickle.load(filename)
                res = loaded_model.predict(df)

        else:
            return redirect('homepage')
    else:
        pass

    return render(request, 'index.html', {'result': res})


def helper(x):
    if x == 0:
        return [0, 0]
    elif x == 2:
        return [1, 0]
    else:
        return [0, 1]