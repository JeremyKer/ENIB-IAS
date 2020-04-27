# Starting with defining the network structure. 
from pgmpy.models import BayesianModel
Diagnostic_model = BayesianModel([('Age', 'Cancer'),
                              ('Age', 'Fumeur'),
                              ('Fumeur', 'Cancer'),
                              ('Cancer', 'TbOuCa'),
                              ('VisiteAsie', 'Tuberculose'),
                              ('Tuberculose', 'TbOuCa'),
                              ('TbOuCa', 'Radiographie'),
                              ('TbOuCa', 'DifficultéRespiratoire'),
                              ('Bronchite', 'DifficultéRespiratoire')])

# visu
import networkx as nx
import pylab as plt
nx.draw(Diagnostic_model, with_labels=True)
plt.show()

# Now defining the parameters.
from pgmpy.factors.discrete import TabularCPD
cpd_age = TabularCPD(variable='Age', variable_card=3, values=[[1/3],[1/3],[1/3]])
cpd_fumeur = TabularCPD(variable='Fumeur', variable_card=2, 
            values=[[0.7,0.5,0.25],[0.3,0.5,0.75]], evidence=['Age'], evidence_card=[3])
cpd_cancer = TabularCPD(variable='Cancer', variable_card=2, 
            values=[[0.05,0.01,0.15,0.001,0.05,0.01],[0.95,0.99,0.85,0.999,0.95,0.99]],
            evidence=['Age','Fumeur'],evidence_card=[3, 2])
cpd_visAsie = TabularCPD(variable='VisiteAsie', variable_card=2, values=[[0.5],[0.5]])
cpd_bronchite = TabularCPD(variable='Bronchite', variable_card=2, values=[[0.3],[0.7]])
cpd_tuberculose = TabularCPD(variable='Tuberculose', variable_card=2,
            values=[[0.7,0.2],[0.3,0.8]], evidence=['VisiteAsie'], evidence_card=[2])
cpd_tubOuCa = TabularCPD(variable='TbOuCa', variable_card=2, 
            values=[[1,1,1,0],[0,0,0,1]],
            evidence=['Tuberculose','Cancer'],evidence_card=[2, 2])
cpd_radiographie = TabularCPD(variable='Radiographie', variable_card=2,
            values=[[1,0.5],[0,0.5]], evidence=['TbOuCa'], evidence_card=[2])
cpd_diffRespi = TabularCPD(variable='DifficultéRespiratoire', variable_card=2, 
            values=[[1,1,1,0.3],[0,0,0,0.7]],
            evidence=['Bronchite','TbOuCa'], evidence_card=[2, 2])

#associating the parameters
Diagnostic_model.add_cpds(cpd_age, cpd_fumeur, cpd_cancer, cpd_visAsie, cpd_bronchite, cpd_tuberculose, cpd_tubOuCa, cpd_radiographie, cpd_diffRespi)

#Checking if the cpds are valid for the model
print("CPDS valid : ",Diagnostic_model.check_model())


# ####################################################
# #	exploitation du réseau Bayesien
# ####################################################
from pgmpy.inference import VariableElimination
# Diagnostic_infer = VariableElimination(Diagnostic_model)
# print(cpd_tubOuCa) # Donc valeur 0 = vrai, 1=faux
# q = Diagnostic_infer.query(variables=['TbOuCa'], evidence={'Tuberculose': 0}) # 0 = avoir la tuberculose
# print("chance d'avoir TbOuCa si j'ai la tuberculose :")
# print(q)
# q = Diagnostic_infer.query(variables=['TbOuCa'], evidence={'Cancer': 0}) # 0 = avoir le cancer
# #print("chance d'avoir TbOuCa si j'ai le cancer :")
# #print(q)
# q = Diagnostic_infer.query(variables=['TbOuCa'], evidence={'Tuberculose': 0,'Cancer': 0}) 
# #print("chance d'avoir TbOuCa si j'ai les deux :")
# #print(q)
# q = Diagnostic_infer.query(variables=['TbOuCa'], evidence={'Tuberculose': 1,'Cancer': 1}) 
# #print("chance d'avoir TbOuCa si je suis en bonne santé :")
# #print(q)
# # tous les cas sont vérifiés

# #détermination de l'influence des param sur TbOuCa
# #print("La variable VisiteAsie influence fortement la chance d'avoir TbOuCa :")
# q = Diagnostic_infer.query(variables=['TbOuCa'], evidence={'Age': 1,'Fumeur':0,'VisiteAsie':1}) 
# #print("sans voyage en Asie :")
# #print(q)
# q = Diagnostic_infer.query(variables=['TbOuCa'], evidence={'Age': 1,'Fumeur':0,'VisiteAsie':0}) 
# #print("avec voyage en Asie :")
# #print(q)

# #print("La variable VisiteAsie influence fortement la chance d'avoir TbOuCa quelque soit l'age :")
# q = Diagnostic_infer.query(variables=['TbOuCa'], evidence={'Age': 0,'Fumeur':1,'VisiteAsie':0}) 
# #print("Jeune :")
# #print(q)
# q = Diagnostic_infer.query(variables=['TbOuCa'], evidence={'Age': 1,'Fumeur':1,'VisiteAsie':0}) 
# #print("Adulte :")
# #print(q)
# q = Diagnostic_infer.query(variables=['TbOuCa'], evidence={'Age': 2,'Fumeur':1,'VisiteAsie':0}) 
# #print("Agé :")
# #print(q)

# #print("Voyager en Asie et fumer influence fortement la chance d'avoir TbOuCa :")
# q = Diagnostic_infer.query(variables=['TbOuCa'], evidence={'Age': 0,'Fumeur':0,'VisiteAsie':0}) 
# #print("Jeune :")
# #print(q)
# q = Diagnostic_infer.query(variables=['TbOuCa'], evidence={'Age': 1,'Fumeur':0,'VisiteAsie':0}) 
# #print("Adulte :")
# #print(q)
# q = Diagnostic_infer.query(variables=['TbOuCa'], evidence={'Age': 2,'Fumeur':0,'VisiteAsie':0}) 
# #print("Agé :")
# #print(q)

# # la variable Bronchite n'influence effectivement pas TbOuCa car n'est pas lié dans le graphe.
# q = Diagnostic_infer.query(variables=['TbOuCa'], evidence={'Bronchite':0}) 
# #print("Bronchite :")
# #print(q['TbOuCa'])
# q = Diagnostic_infer.query(variables=['TbOuCa'], evidence={'Bronchite':1}) 
# #print("Sans bronchite :")
# #print(q)



##############################################################################
#    extraire un réseau Bayesien à partir d'une base de données
##############################################################################
import pandas as pd
file = open('./Asia.txt','r')

#Lecture de la premiere ligne (non prise en compte
line = file.readline().split()

#Creation des tableaux contenant les données
N=[]
smoker=[]
cancer=[]
age=[]
tuberculosis=[]
tbOrCa=[]
visitAsia=[]
xray=[]
bronchitis=[]
dyspnea=[]
geographical=[]

#Boucle de lecture du fichier et écriture dans les tableaux
for i in range(0,9999) :
  line = file.readline().split()
 
  N.append(line[0])
  smoker.append(line[1])
  cancer.append(line[2])
  age.append(line[3])
  tuberculosis.append(line[4])
  tbOrCa.append(line[5])
  visitAsia.append(line[6])
  xray.append(line[7])
  bronchitis.append(line[8])
  dyspnea.append(line[9])
  

  try:
    line[11]
  except IndexError:
    geographical.append("?")
  else:
    geographical.append("Zone "+line[11])

#génération des données
data = pd.DataFrame(data = {'Fumeur' : smoker,'Cancer': cancer, 'Age':age, 'Tuberculose':tuberculosis,'TbOuCa':tbOrCa, 'VisiteAsie':visitAsia,'Radiographie':xray,'Bronchite':bronchitis,'Dyspnea':dyspnea,'Geographie':geographical})
print(data)


#Apprentissage de la structure
from pgmpy.estimators import HillClimbSearch, BicScore
bic = BicScore(data)
hc = HillClimbSearch(data, scoring_method=bic)
best_model = hc.estimate()
print(best_model.edges())
# la relecture de la structure trouvée révèle que le programme donne les liaisons mais pas le sens de ces dernières.
# le model avec le bon sens serait donc : 
bon_model = BayesianModel([('Cancer', 'TbOuCa'), ('TbOuCa', 'Dyspnea'), ('TbOuCa', 'Bronchite'), ('TbOuCa', 'Radiographie'), ('Fumeur','Bronchite'), ('Radiographie', 'Dyspnea'), ('Tuberculose', 'TbOuCa'), ('Bronchite','Dyspnea')])



#apprentissage des paramètres
#print("estimation des cpds :")
from pgmpy.estimators import BayesianEstimator
est = BayesianEstimator(best_model,data)
print(est.estimate_cpd('Cancer', prior_type='BDeu', equivalent_sample_size=10))

best_model.fit(data, estimator=BayesianEstimator, prior_type='BDeu')
#for cpd in best_model.get_cpds():
#	print(cpd)

#Caractéristique des personnes ayant un cancer
model_infer = VariableElimination(best_model)
q = model_infer.query(variables=['Age','Fumeur','Tuberculose','VisiteAsie','Radiographie','Bronchite','Dyspnea','Geographie','TbOuCa'], evidence={'Cancer':2}) # 0 = ? , 1=False, 2=True
print("Caratéristiques des personnes ayant le cancer :")
#print(q['Age'])
print(q['Fumeur'])
print(q['Tuberculose'])
print(q['VisiteAsie'])
print(q['Radiographie'])
print(q['Bronchite'])
print(q['Dyspnea'])
print(q['Geographie'])
print(q['TbOuCa'])


