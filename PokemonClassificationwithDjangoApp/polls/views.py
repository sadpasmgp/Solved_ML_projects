from django.shortcuts import render, redirect
import pandas as pd
import pickle
import os
import traceback

# Create your views here.

val = None

def first(request):
    if request.method == 'POST':
        if request.POST.get('pred_button'):
            name = request.POST['Pokemon Name']
            total = request.POST['total']
            HP = request.POST['HP']
            attack = request.POST['attack']
            defence = request.POST['defence']
            special = request.POST['special']
            speciald = request.POST['speciald']
            speed = request.POST['speed']
            genration = request.POST['gen']
            gender = request.POST['hasgen']
            Pr_male = request.POST['Pr_Male']
            evo = request.POST['hasMegaEvolution']
            height = request.POST['height']
            weight = request.POST['weight']
            catch_rate = request.POST['catch']
            bodystyle = request.POST['bodystyle']
            poke_type = request.POST['type']
            color = request.POST['color']

            print(name, type(total))
            if name != "":
                try:
                    df = pd.DataFrame(columns=['Total', 'HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def', 'Speed',
                                        'Generation', 'hasGender', 'Pr_Male', 'hasMegaEvolution', 'Height_m',
                                        'Weight_kg', 'Catch_Rate', 'Body_Style_new', 'Dark', 'Dragon',
                                        'Electric', 'Fighting', 'Fire', 'Flying', 'Grass', 'Normal', 'Poison',
                                        'Rock', 'Water', 'Black', 'Blue', 'Brown', 'Green', 'Grey', 'Pink',
                                        'Purple', 'Red', 'White', 'Yellow'])

                    type_pokemon = finding_type(poke_type)
                    color_pokemon = finding_color(color)
                    df2 = {"Total": int(total), 'HP': int(HP), 'Attack': int(attack), 'Defense': int(defence),
                           'Sp_Atk': int(special), 'Sp_Def': int(speciald), 'Speed': int(speed),
                           'Generation': int(genration), 'hasGender': bool(gender), 'Pr_Male': float(Pr_male),
                           'hasMegaEvolution': bool(evo), 'Height_m': float(height), 'Weight_kg': float(weight),
                           'Catch_Rate': int(catch_rate), 'Body_Style_new': int(bodystyle), 'Dark':
                            type_pokemon[0], 'Dragon': type_pokemon[1], 'Electric': type_pokemon[2],
                           'Fighting': type_pokemon[3], 'Fire': type_pokemon[4], 'Flying': type_pokemon[5],
                           'Grass': type_pokemon[6], 'Normal': type_pokemon[7], 'Poison': type_pokemon[8],
                            'Rock': type_pokemon[9], 'Water': type_pokemon[10], 'Black': color_pokemon[0],
                           'Blue': color_pokemon[1], 'Brown': color_pokemon[2], 'Green': color_pokemon[3],
                           'Grey': color_pokemon[4], 'Pink': color_pokemon[5], 'Purple': color_pokemon[6],
                           'Red': color_pokemon[7], 'White': color_pokemon[8], 'Yellow': color_pokemon[9]}

                    df = df.append(df2, ignore_index=True)

                    # load the model from disk
                    filename = 'polls/pokemon_model.pickle'
                    loaded_model = pickle.load(open(filename, 'rb'))
                    res = loaded_model.predict(df)
                    print(res)
                    global val

                    def val():
                        return res

                    return redirect('results_show')
                except:
                    traceback.print_exc()
                    return redirect("404")


    return render(request, 'index.html')


def func(request):
    return render(request, '404.html')

def results(request):
    ok = val()
    ok = str(ok[0])
    return render(request, 'results.html', {'result': ok})

def finding_type(x):
    # Dark	Dragon	Electric	Fighting	Fire	Flying	Grass	Normal	Poison	Rock	Water
    if x == "Dark":
        return [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif x == "Dragon":
        return [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif x == "Electric":
        return [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    elif x == 'Fighting':
        return [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    elif x == 'Fire':
        return [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    elif x == "Flying":
        return [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    elif x == "Grass":
        return [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    elif x == "Normal":
        return [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    elif x == 'Poison':
        return [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    elif x == "Rock":
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    else:
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]


def finding_color(y):
    # Black	Blue	Brown	Green	Grey	Pink	Purple	Red	White	Yellow
    if y == 'Black':
        return [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif y == "Blue":
        return [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    elif y == "Brown":
        return [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    elif y == "Green":
        return [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    elif y == "Grey":
        return [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    elif y == "Pink":
        return [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    elif y == "Purple":
        return [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    elif y == "Red":
        return [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    elif y == "White":
        return [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    else:
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
