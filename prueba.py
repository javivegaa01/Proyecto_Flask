from tabulate import tabulate
titulo=[["GRUPO A"],["betis","puntos","dife"]]
print(tabulate(titulo,headers="firstrow",tablefmt='fancy_grid',stralign='center',floatfmt='.0f'))