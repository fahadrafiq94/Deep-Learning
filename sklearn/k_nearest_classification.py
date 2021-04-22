from sklearn import datasets 

#importing k neigbhor classifier 
from sklearn.neighbors import KNeighborsClassifier


#loading data
iris = datasets.load_iris()

# print(iris.DESCR) 
features = iris.data #data me features hote hain
labels = iris.target #target me labels hote

print(features[0], labels[0])
# [5.1 3.5 1.4 0.2] 0   is me 3 classes hoti 0 1 aur 2 -0 Iris-Setosa -1 Iris-Versicolour -2 Iris-Virginica
                
clf = KNeighborsClassifier() #we create classifier here
#every classifier has a fit function and predict function
 
clf.fit(features,labels) #it fit himself in old data

preds = clf.predict([[22,1,1,1]]) # is me hum 2d array me data dete aur wo bata deta
print(preds)

