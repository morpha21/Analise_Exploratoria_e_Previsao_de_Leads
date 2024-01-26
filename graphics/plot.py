import matplotlib.pyplot as plt
import seaborn as sns

from pandas import DataFrame
from cycler import cycler

sns.set()



def dataplot(dados: DataFrame,
		colunax: str,
		colunay: str,
		add: list = [],
		linestyle1: str = 'none',
		linestyle2: str = 'none',
		mew: float = None,
		mec: str = None,
		size: tuple = (5,5)
	):
	"""Cria um gráfico a partir de duas colunas de um Pandas DataFrame"""
	cores = cycler(color=['mediumseagreen','y','k','g','chocolate','m','b','r'])
	df = dados.sort_values(colunax)
	fig = plt.figure(figsize=size, dpi=100, facecolor='moccasin')
	axes1 = fig.add_axes([0, 0, 1, 1])
	axes1.set_prop_cycle(cores)

	if add != []:
		plt.plot(add[0], add[1], marker ='.', linestyle=linestyle2,mew=mew, mec=mec)

	plt.plot(df[colunax], df[colunay], marker ='.', linestyle=linestyle1, mew=mew, mec=mec)
	plt.xlabel(colunax)
	plt.ylabel(colunay)
	plt.show()


