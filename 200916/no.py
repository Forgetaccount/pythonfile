
a = [1, 2, 3, 4, 5, 6,2]
b = [2, 4, 6, 8 ,10]
ret1= [x for x in b if x in set(a)]
print(ret1)
ret2= list(set(a) & set(b))
print(ret2)
ret3= list(set(a).intersection(b))
print(ret3)
ret4 = list((set(a).union(set(b)))^(set(a)^set(b)))
print(ret4)


zidian={'ProbabilisticMethods':0,'Theory':0,'CaseBased':0
        ,'NeuralNetworks':0,'GeneticAlgorithms':0,'RuleLearning':0
        ,'ReinforcementLearning':0}
a='ProbabilisticMethods'
b=zidian[a]+1
print(b)





