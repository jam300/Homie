import string
import numpy as np


def main():
	list_letra = list(string.ascii_uppercase[:])
	let = input("Introduzca una letra: ")
	simbolo = input(
		"Introduzca un simbolo si quiere sustituir el espacio de caso contrario deje un espacio y presione Enter: ")

	index_letra = list_letra.index(let.upper())
	# print(index_letra)
	if (index_letra == 0):
		print(list_letra[index_letra])
	else:
		D = 2 * (index_letra)
		I = D - 1
		M = np.empty((D + 1, D + 1), dtype='str')
		M[:] = simbolo
		# print(M)
		# print(index_letra)
		# print(D)
		# print(I)
		# M[1][0], M[0][0]= 'B','B'
		# print(M)
		for i in range(0, index_letra):
			if (i == 0):
				M[i][int(D / 2)] = list_letra[i]
				M[D][int(D / 2)] = list_letra[i]
				M[int(D / 2)][i] = list_letra[index_letra]
				M[int(D / 2)][D] = list_letra[index_letra]
			else:
				M[i][(int(D / 2)) - i] = list_letra[i]
				M[i][(int(D / 2)) + i] = list_letra[i]
				M[D - i][(int(D / 2)) - i] = list_letra[i]
				M[D - i][(int(D / 2)) + i] = list_letra[i]
			# print(M)

		for i in range(0, D + 1):
			for j in range(0, D + 1):
				print(M[i][j], end="")
				print(" ")

	if __name__ == '__main__':
		main()