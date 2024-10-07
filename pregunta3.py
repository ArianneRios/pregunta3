# -*- coding: utf-8 -*-
"""pregunta3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YPTVOwBAr9An9BczpxCAS0AbTSPMugSx
"""

from google.colab import drive
drive.mount('/content/drive')

# Paso 1: Montar Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Paso 2: Importar librerías necesarias
import pandas as pd
import arff
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, KBinsDiscretizer, MinMaxScaler

# Paso 3: Leer el archivo CSV con el separador correcto
file_path = '/content/drive/My Drive/Breast_Cancer 2.csv'  # Asegúrate de que este sea el camino correcto

# Eliminar espacios en blanco de los nombres de las columnas
data.columns = data.columns.str.strip()

# Mostrar las primeras filas y las columnas del DataFrame para verificar los datos
print(data.head())
print(data.columns)

# Paso 4: Convertir a ARFF
# Convertir DataFrame a una estructura compatible con ARFF
arff_data = {
    'description': '',
    'relation': 'breast_cancer_data',
    'attributes': [(col, 'STRING') for col in data.columns],
    'data': data.values
}

# Guardar el archivo ARFF
with open('/content/breast_cancer.arff', 'w') as f:
    arff.dump(arff_data, f)

print("Archivo ARFF generado.")

# Paso 5: Aplicar OneHotEncoder

categorical_columns = ['Race', 'Marital Status', 'T Stage', 'N Stage']

# Aplicar OneHotEncoder
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')  # Usar sparse_output
encoded_data = encoder.fit_transform(data[categorical_columns])

# Convertir el resultado a un DataFrame
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(categorical_columns))

# Reemplazar las columnas originales por las codificadas
data = data.drop(categorical_columns, axis=1)
data = pd.concat([data, encoded_df], axis=1)

print("OneHotEncoder aplicado.")

# Paso 6: Aplicar LabelEncoder

label_col = 'Grade'

# Aplicar LabelEncoder
label_encoder = LabelEncoder()
data[label_col] = label_encoder.fit_transform(data[label_col])

print("Etiquetas convertidas con LabelEncoder.")

# Paso 7: Discretización

continuous_columns = ['Age']  # Cambia por las columnas que quieras discretizar


discretizer = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
data[continuous_columns] = discretizer.fit_transform(data[continuous_columns])

print("Discretización realizada.")

#  Normalización

numeric_columns = ['Age']
# Aplicar MinMaxScaler
scaler = MinMaxScaler()
data[numeric_columns] = scaler.fit_transform(data[numeric_columns])

print("Normalización realizada.")

print(data.head())