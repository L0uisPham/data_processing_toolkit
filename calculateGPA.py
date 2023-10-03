import pandas as pd

filename = 'new_data/Grade '
grades = {'7.csv', '8.csv', '9.csv', '11.csv'}


def gpaConvert(score):
    if score >= 93:
        return 4.0
    elif score >= 90:
        return 3.7
    elif score >= 87:
        return 3.3
    elif score >= 83:
        return 3.0
    elif score >= 80:
        return 2.7
    elif score >= 77:
        return 2.3
    elif score >= 73:
        return 2.0
    elif score >= 70:
        return 1.7
    elif score >= 67:
        return 1.3
    elif score >= 63:
        return 1.0
    elif score >= 60:
        return 0.7
    else:
        return 0.0



for i in grades:
    df = pd.read_csv(filename + i)
    if i == '7.csv' or i == '8.csv':
        df['Core Class Avg T1'] = df['Core Class Avg T1'].apply(gpaConvert)
        df['Core Class Avg T2'] = df['Core Class Avg T2'].apply(gpaConvert)
    else:
        df['Avg Q1'] = df['Avg Q1'].apply(gpaConvert)
        df['Avg Q2'] = df['Avg Q2'].apply(gpaConvert)

    df.to_csv(filename + i, index=False)

