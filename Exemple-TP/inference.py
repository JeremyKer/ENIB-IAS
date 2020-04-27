from pgmpy.readwrite import BIFReader

reader = BIFReader('asia.bif')
asia_model = reader.get_model()

print(asia_model.nodes())
print( " −−−−−−−−−−−−−−−−−−−−−− ")
print(asia_model.edges())
print( " −−−−−−−−−−−−−−−−−−−−−− ")
print(asia_model.get_cpds())
print( " −−−−−−−−−−−−−−−−−−−−−− ")

# Doing exact inference using Variable Elimination
from pgmpy.inference import VariableElimination
asia_infer = VariableElimination(asia_model)

#Computing the probability of bronc given smoke. 
q = asia_infer.query(variables=['bronc'], evidence={'smoke': 0})
print(q['bronc'])
print( " −−−−−−−−−−−−−−−−−−−−−− ")

q = asia_infer.query(variables=['bronc'], evidence={'smoke': 1})
print(q['bronc'])
print( " −−−−−−−−−−−−−−−−−−−−−− ")