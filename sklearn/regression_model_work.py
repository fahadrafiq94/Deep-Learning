import matplotlib.pyplot as plt 
import numpy as np
from sklearn import datasets,linear_model # we use built in data set diabetes from sklearn 
from sklearn.metrics import mean_squared_error

diabetes = datasets.load_diabetes() # this load data set from sklearn 

# print(diabetes.key())   # it will show the keys of data set 
# above line show this ----> 
# dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename'])
 
# print(diabetes.data)

# print(diabetes.DESCR) #it shows the data dataset description

diabetes_x = np.array([ [1], [2], [3] ]) #input x value in array

#for x axis 

diabetes_x_Train = diabetes_x
diabetes_x_Test= diabetes_x


#for y axis 
   #we use np.array bcoz in sklearn  we use array in this way
diabetes_y_train = np.array([ [3] ,[2], [4] ])
diabetes_y_test = np.array([ [3] ,[2], [4] ])
 
  #for linear model
model = linear_model.LinearRegression() # linearregression ko import kiya
model.fit(diabetes_x_Train,diabetes_y_train) #hum learn krwa rai is se 
 
diabetes_y_predict =model.predict(diabetes_x_Test) #we gave him feature and it give us value 

print("mean squaed error is ",mean_squared_error(diabetes_y_test,diabetes_y_predict ))

print("weights ",model.coef_) #it will give th weights 
print("intercept",model.intercept_)  #it will give us intercept 

plt.scatter(diabetes_x_Test,diabetes_y_test) #its create scatter plot of data
plt.plot(diabetes_x_Test,diabetes_y_predict)
plt.show() #its show scatter plot

# mean squaed error is  3920.5108316442765
# weights  [941.43097333]
# intercept 153.39713623331698

