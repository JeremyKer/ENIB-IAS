# Parameter learning 
print(" −−−−−−−−−−− Data −−−−−−−−−−− ")
import pandas as pd 
data = pd.DataFrame(data={
    "fruit" : ["banana" , "apple", "banana", "apple", "banana", "apple", "banana", "apple", "apple", "apple", "banana", "banana", "apple", "banana"] ,
    "tasty" : [ "yes", "no" ,  "yes",  "yes",  "yes",  "yes",  "yes",  "yes", "yes",  "yes",  "yes", "no", "no", "no" ] ,
    "size" : [ "large" ,"large", "large", "small" , "large", "large", "large" ,"small","large", "large" , "large", "large" , "small", "small"]
})

print(data)

from pgmpy.models import BayesianModel
model = BayesianModel([('fruit', 'tasty'),('size', 'tasty')]) # fruit −> tasty <− size


# State counts
print(" −−−−−−−−−−− State counts −−−−−−−−−−− ")
from  pgmpy.estimators import ParameterEstimator
pe = ParameterEstimator(model,data)
print("\n", pe.state_counts('fruit')) # unconditional
print( " −−−−−−−−−−−−−−−−−−−−−− ")
print("\n", pe.state_counts('tasty')) # conditional on fruit and size
print( " −−−−−−−−−−−−−−−−−−−−−− ")


# Maximum Likelihood Estimation
print("−−−−− Maximum Likelihood Estimation −−−−−−−−−−−−−−")
from pgmpy.estimators import MaximumLikelihoodEstimator
mle = MaximumLikelihoodEstimator(model,data)
print (mle.estimate_cpd("fruit") ) # unconditional
print( " −−−−−−−−−−−−−−−−−−−−−− ")
print(mle.estimate_cpd("tasty") ) # conditional
print( " −−−−−−−−−−−−−−−−−−−−−− ")


# Calibrate all CPDs of ‘model' using MLE:
model.fit(data, estimator=MaximumLikelihoodEstimator)
# Bayesian Parameter Estimation
print("−−−−− Bayesian Parameter Estimation −−−−−−−−−−−−−−")
from pgmpy.estimators import BayesianEstimator
est = BayesianEstimator(model, data)
print(est.estimate_cpd("tasty", prior_type="BDeu", equivalent_sample_size=10))
print( " −−−−−−−−−−−−−−−−−−−−−− ")

# BayesianEstimator , too , can be used via the fit()−method . Full example :
import numpy as np
import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import BayesianEstimator
# generate data
data = pd.DataFrame( np.random.randint(low =0, high =2, size =(5000, 4)), columns =["A", "B", "C","D"])
model = BayesianModel([("A", "B") , ("A", "C") , ("D", "C") , ("B", "D")])
model.fit(data, estimator=BayesianEstimator, prior_type="BDeu" ) # d e f a u l t e q u i v a l e n t s a m p l e s i z e =5
for cpd in model.get_cpds() :
    print(cpd)