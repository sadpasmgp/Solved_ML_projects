from django.shortcuts import render, redirect
import pandas as pd
import pickle, os, random

# Finding attrition rate:
def Attrition_rate_finder(request):
    if request.method == 'POST':
        if request.POST.get('attrition_button'):
            name = request.POST['Person Name']
            location = request.POST['location']
            emp_group = request.POST['emp-group']
            function = request.POST['function']
            gender = request.POST['gender']
            tenure_group= request.POST['tenure group']
            experience = request.POST['experience']
            age = request.POST['age']
            Maritial = request.POST['Marital']
            Hiring = request.POST['Hiring']
            Promoted = request.POST['Promoted']
            Job = request.POST['Job']
            # print(name)

            results = Finder(name, location, emp_group, function, gender, tenure_group,
                                      experience, age, Maritial, Hiring, Promoted, Job)
            print(results)
            results = str(results[0])
        else:
            print('Not Working')

    else:
        results = None

    return render(request, 'attrition_form.html', {'result': results})


def Finder(name, location, emp_group, function, gender, tenure_group,
                                  experience, age, Maritial, Hiring, Promoted, Job):
    if name != "":
        df = pd.DataFrame(columns=['id', 'Experience (YY.MM)', 'Age in YY.', 'New Location',
                                   'New Promotion', 'New Job Role Match', 'Agency', 'Direct',
                                   'Employee Referral', 'Marr.', 'Single', 'other status', 'B1', 'B2',
                                   'B3', 'other group', '< =1', '> 1 & < =3', 'Operation', 'Sales',
                                   'Support', 'Female', 'Male', 'other'])

        HiringSource = HiringPeep(Hiring)
        Maritial_Status = MStatus(Maritial)
        EmpGrp = EmployeeGrp(emp_group)
        tengrp = TenureGrp(tenure_group)
        func = FunctionName(function)
        gen = Gender(gender)
        count = Co()
        df2 = {'id': count, 'Experience (YY.MM)': float(experience), 'Age in YY.': float(age), 'New Location': location,
               'New Promotion': int(Promoted), 'New Job Role Match': int(Job), 'Agency': HiringSource[0],
               'Direct': HiringSource[1], 'Employee Referral': HiringSource[2], 'Marr.': Maritial_Status[0], 'Single':
               Maritial_Status[1], 'other status': Maritial_Status[2], 'B1': EmpGrp[0], 'B2': EmpGrp[1],
               'B3': EmpGrp[2], 'other group': EmpGrp[3], '< =1': tengrp[0], '> 1 & < =3': tengrp[1],
               'Operation': func[0], 'Sales': func[1], 'Support': func[2], 'Female': gen[0], 'Male': gen[1],
               'other': gen[2]}

        df = df.append(df2, ignore_index=True)

        # load the model from disk
        filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), r'Attrition\finalized_model.pickle')
        loaded_model = pickle.load(open(filename, 'rb'))
        res = loaded_model.predict(df)
        print(res)

        return res

    else:
        return None

def Co():
    return random.randrange(20, 500)

def HiringPeep(x):
    if str(x) == "Agency":
        return [1, 0, 0] # Agency,Direct, Employee Referral
    elif str(x) == "Direct":
        return [0, 1, 0]
    else:
        return [0, 0, 1]


def MStatus(x):
    if str(x) == "Marr.":
        return [1, 0, 0]
    elif str(x) == "Single":
        return [0, 1, 0]
    else:
        return [0, 0, 1]

def EmployeeGrp(x):
    if str(x) == "B1":
        return [1, 0, 0, 0]
    elif str(x) == "B2":
        return [0, 1, 0, 0]
    elif str(x) == 'B3':
        return [0, 0, 1, 0]
    else:
        return [0, 0, 0, 1]

def TenureGrp(x):
    if str(x) == "< =1":
        return [1, 0]
    else:
        return [0, 1]

def FunctionName(x):
    if str(x) == "Operation":
        return [1, 0, 0]
    elif str(x) == "Sales":
        return [0, 1, 0]
    else:
        return [0, 0, 1]

def Gender(x):
    if str(x) == "Female":
        return [1, 0, 0]
    elif str(x) == "Male":
        return [0, 1, 0]
    else:
        return [0, 0, 1]