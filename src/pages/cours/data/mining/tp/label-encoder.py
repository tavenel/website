from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()
enc.fit(data['Regime'])
data['RegimeN'] = enc.transform(data['Regime'])

