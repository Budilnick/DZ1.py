salary = [2500, 1500.3252, 5000.34525, 1245.50, 7500.12]
print(len(salary))
print(sum(salary, len(salary)))
print(round(sum(salary)/len(salary), 2), '- srednee okruglenno')
print(sum(salary)/len(salary), '- srednee')
print(max(salary), "- max")
print(round(max(salary), ), "- max okrugl")
print(min(salary), "- min")
print(round(min(salary), 2), "- min okrugl")

names = ['Денис', "Антон", "Катя", "Женя", "Вася"]
zipped = dict(zip(names, salary))
print(zipped)
#print(list(zipped))
#print(dict(zipped))
print(round(zipped["Антон"], 2) , '- zp Antona')










