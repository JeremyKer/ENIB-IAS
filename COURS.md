# Réseaux Bayésiens 

Code réalisé par Jérémy KEROUANTON.


## Introduction

>On va voir lors du cours les conditions probabilistes.
La notion de probabilité conditionnelle permet de prendre en compte une prévision d'informations complémentaires.
En ce qui concerne le domaine d'applciation de cette notion, nous allons voir deux de ces domaines :
>* __diagnostic__ : En supposant un échec, un système basé sur Bayesian
les réseaux peuvent déterminer les causes les plus probables
qui a fourni le problème.
>* __classification__ : Basé sur un certain nombre de fonctionnalités du système, le bayésien les réseaux pourront les classer.

--------

## Structure 

### Causal graph 
Les graphiques causaux sont des modèles graphiques probabilistes utilisés pour coder des hypothèses sur le processus de génération de données.

#### Acyclic oriented graph
> En théorie des graphes, un graphe orienté acyclique, est un graphe orienté qui ne possède pas de circuit. Un tel graphe peut être vu comme une hiérarchie.


### Probability of the variables

#### Probability table
> La table de probabilités conditionnelles est définie pour un ensemble de variables aléatoires discrètes et mutuellement dépendantes afin d'afficher les probabilités conditionnelles d'une seule variable par rapport aux autres.


--------

## Inference

L'inférence bayésienne est le processus logique pour calculer ou réviser la probabilité d'une hypothèse. Cette approche est
régie par l'utilisation de règles strictes de combinaison de probabilités, dont dérive le théorème de Bayes.

```
Exemple : 

Ces tableaux permettent d'avoir toutes les informations concernant les différentes variables de notre graphique, et il sera possible pour les utiliser. Intéressé par la probabilité d'être «malade» dans une situation donnée, regardons le calendrier etsachez que nous sommes le 12 juillet. Nous en déduisons donc que nous ne sommes pas en chute. 
P (F = 0) = 1. 
En regardant l'arbre, nous observez également qu'il perd ses feuilles. 
P (L = 1) = 1.
Et on peut se demander: "connaissant ces éléments, l'arbre est-il malade?"
P (D = 1 | F = 0, L = 1) =?
P (A | B) = ce que nous voulons / possibilité (nous connaissons B, nous faisons varier A)
P (D, F, L) = P (L | D, F) ∗ P (F) ∗ P (D)
```

### Exercices pratiques

```
Detection of an animal disease

* In one animal population, one out of every hundred is affected
by a disease.
* A test used to detect the disease is characterized by a
probability of non-detection estimated at 5 % (false negative
rate), and a probability of inadvertent detection equal to 1 %
(false positive rate)
⇒ Propose a network and the associated probability tables
⇒ Estimate the probability of an individual being reached,
knowing that the test is negative
```

-----

## Learning 

On peut apprendre :
* les varaibles qui sont importantes et celle qui ne le sont pas,
* les relations entres les variables
* les probabilités conditionnelles 


-----
## Extended Models

On retrouve des modèles comme : 
* __Diagramme d'influence__ : 
    une représentation graphique et mathématique compacte d'une situation de décision. Il s'agit d'une généralisation d'un réseau bayésien, dans lequel non seulement les problèmes d'inférence probabiliste, mais aussi les problèmes de prise de décision (ex : critère d'utilité maximale attendue) peuvent être modélisés et résolus.
*


----
## Applications

### Domaine d'application
>* Medecine 
>    * Support diagnostique pour les problèmes cardiovasculaires 
>    * la supervision de transfusion, ... 

>* Industrie
>    * NASA: real-time fault diagnosis support for the propulsion systems of the Space Shuttle
>    * Lockheed Martin : control system of an autonomous underwater vehicle
>    * Ricoh : remote diagnostic assistance
>    * EDF : generator modeling

### Les logiciels 
>* Toolbox
>    * Bayes Net Toolbox (BNT) for Matlab
>    * gR, GRAPPA, . . . for R
>    * BNJ, JavaBayes, . . . for Java

>* Non-commercial software
>    * Microsoft Belief Network [US]
>    * Genie 2/Smile [US]

>* Logiciels commerciaux
>    * Bayesia [FR]
>    * ProBT (inférence probabiliste) [FR]
>    * Hugin [DK]
>    * Netica [CA]

### Comment choisir son outil ?
>* Limited offer
>* Tasks taken into account?
>    * creating a network ”graphically”?
>    * inference: implemented algorithms?
>    * learning: missing data? structure?
>* API?

---
## Librairie "pgympy"
Lors de ce cours et TP, nous allons utiliser la librairie __pgympy__ afin de :
* créer notre réseau,
* faire l'inférence, 
* l'apprentissage des paramètres,
* l'apprentissage de la structure

Pour plus d'informations, https://github.com/pgmpy/pgmpy.