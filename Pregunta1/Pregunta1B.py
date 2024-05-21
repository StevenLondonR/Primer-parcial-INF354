import pandas as pd
import numpy as np

data = pd.read_csv('Raisin_DatasetComas.csv', encoding='utf-8',sep=';');

columnasArea=data['Area'].tolist()
columnasMayor=data['MajorAxisLength'].tolist()
columnasMenor=data['MinorAxisLength'].tolist()
columnasE=data['Eccentricity'].tolist()
columnasConvex=data['ConvexArea'].tolist()
columnasExtent=data['Extent'].tolist()
columnasP=data['Perimeter'].tolist()
columnasClass=data['Class'].tolist()


#print(data.columns)
#print(columnasMayor)
#print("//////////////////////////////////////////////////////////////")
print("-------------------------------------------------------- Quartil --------------------------------------------------------")
print(np.percentile(columnasArea, 40))
print(np.percentile(columnasMayor, 40))
print(np.percentile(columnasMenor ,40))
print(np.percentile(columnasE,40))
print(np.percentile(columnasConvex,40))
print(np.percentile(columnasExtent, 40))
print(np.percentile(columnasP, 40))
conClass=pd.DataFrame(columnasClass,columns=["val"])
per=np.percentile(conClass.index, 40)
#print("per: ",per)

nombreP40 = conClass.iloc[int(per)]["val"]
print("El quartil de la lista es:", nombreP40)
#print("//////////////////////////////////////////////////////////////")
print("--------------------------------------------------------Percentil 80--------------------------------------------------------")
print(np.percentile(columnasArea, 80))
print(np.percentile(columnasMayor, 80))
print(np.percentile(columnasMenor ,80))
print(np.percentile(columnasE,80))
print(np.percentile(columnasConvex,80))
print(np.percentile(columnasExtent, 80))
print(np.percentile(columnasP, 80))
conClass=pd.DataFrame(columnasClass,columns=["val"])
per=np.percentile(conClass.index, 80)
#print("per: ",per)

nombreP40 = conClass.iloc[int(per)]["val"]
print("El percentil 80 de la lista es:", nombreP40)

