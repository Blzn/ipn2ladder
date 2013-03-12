from converter import Converter
from twidoilgenerator import TwidoILGenerator
from ipn import InterpretedPetriNet

f = open("matrizesPlanta.txt", "r")
f.readline()

ipnPlantaCompleta = InterpretedPetriNet()
ipnPlantaCompleta.inMatrix = []
ipnPlantaCompleta.outMatrix = []
ipnPlantaCompleta.m0 = [k*0 if k+1 not in [4,5,7,20,23] else 1 for k in range(41)]
ipnPlantaCompleta.actions = {("Q0.0.2", "on"): [1, 3, 4],
							 ("Q0.0.3", "on"): [3],
							 ("Q0.0.4", "on"): [8, 9, 12, 13],
							 ("Q0.0.5", "on"): [11, 12, 13, 14],
							 ("Q0.0.6", "on"): [7, 8, 13, 14],
							 ("Q0.0.7", "on"): [16, 17, 18, 22],
							 ("Q0.0.8", "on"): [19],
							 ("Q0.0.9", "on"): [19],
							 ("Q0.0.10", "on"): [19],
							 ("Q0.0.11", "on"): [23, 27, 28, 34, 38],
							 ("Q0.0.12", "on"): [34, 35, 36, 38, 39, 40],
							 ("Q0.0.13", "on"): [28, 29, 30, 33, 34, 35, 36],
							 ("Q0.0.14", "on"): [23, 25, 30, 36, 40]}
							 
ipnPlantaCompleta.firingConditions = [[("I0.0.0", "closed"), ("I0.0.1", "open")], #t1
					         		 [("I0.0.2", "open")], #t2
									 [("I0.0.0", "open"), ("I0.0.3", "open")], #t3
									 [("I0.0.2", "open"), ("I0.0.4", "open")], #t4
									 [("I0.0.3", "open"), ("I0.0.5", "open"), ("I0.0.7", "open"), ("I0.0.9", "open")], #t5
									 [("I0.0.3", "open"), ("I0.0.6", "open"), ("I0.0.7", "open"), ("I0.0.9", "open")], #t6
									 [("I0.0.3", "open"), ("I0.0.6", "open"), ("I0.0.7", "open"), ("I0.0.9", "closed")], #t7
									 [("I0.0.5", "open"), ("I0.0.7", "open"), ("I0.0.9", "closed")], #t8
									 [("I0.0.5", "open"), ("I0.0.8", "open"), ("I0.0.9", "closed"), ("I0.0.10", "open")], #t9
									 [("I0.0.6", "open"), ("I0.0.8", "open"), ("I0.0.9", "closed"), ("I0.0.10", "open")], #t10
									 [("I0.0.6", "open"), ("I0.0.8", "open"), ("I0.0.9", "open"), ("I0.0.10", "open")], #t11
									 [("I0.0.5", "open"), ("I0.0.8", "open"), ("I0.0.9", "open"), ("I0.0.10", "open")], #t12
									 [("I0.0.5", "open"), ("I0.0.7", "open"), ("I0.0.9", "open"), ("I0.0.10", "open")], #t13
									 [("I0.0.10", "raising")], #t14
									 [("I0.0.10", "falling")], #15
									 [("I0.0.10", "raising"), ("I0.0.11", "open")], #t16
									 [("I0.0.10", "open"), ("I0.0.12", "open"), ("I0.0.13", "open")], #t17
									 [("I0.0.10", "open"), ("I0.0.11", "open")], #t18
									 [("I0.0.10", "raising")], #t19
									 [("I0.0.10", "open"), ("I0.0.15", "open"), ("I0.0.17", "open"), ("I0.0.18", "open"), ("I0.0.19", "open")], #t20
									 [("I0.0.10", "open"), ("I0.0.14", "open"), ("I0.0.17", "open"), ("I0.0.18", "open"), ("I0.0.19", "open")], #t21
									 [("I0.0.10", "open"), ("I0.0.14", "open"), ("I0.0.17", "open"), ("I0.0.18", "closed"), ("I0.0.19", "open")], #t22
									 [("I0.0.15", "open"), ("I0.0.17", "open"), ("I0.0.18", "closed"), ("I0.0.19", "open"),], #t23
									 [("I0.0.15", "open"), ("I0.0.17", "open"), ("I0.0.18", "closed"), ("I0.0.20", "open"),], #t24
									 [("I0.0.14", "open"), ("I0.0.17", "open"), ("I0.0.18", "closed"), ("I0.0.20", "open"),], #t25
									 [("I0.0.14", "open"), ("I0.0.17", "open"), ("I0.0.18", "open"), ("I0.0.20", "open"), ("IW0.1.0", "lesser", 700)], #t26
									 [("I0.0.14", "open"), ("I0.0.17", "open"), ("I0.0.18", "open"), ("I0.0.20", "open"), ("IW0.1.0", "greater", 700)], #t27
									 [("I0.0.14", "open"), ("I0.0.17", "open"), ("I0.0.18", "closed"), ("I0.0.20", "open")], #t28
									 [("I0.0.15", "open"), ("I0.0.16", "open"), ("I0.0.18", "closed"), ("I0.0.20", "open")], #t29
									 [("I0.0.14", "open"), ("I0.0.16", "open"), ("I0.0.18", "closed"), ("I0.0.20", "open")], #t30
									 [("I0.0.14", "open"), ("I0.0.16", "open"), ("I0.0.18", "open"), ("I0.0.20", "open")], #t31
									 [("I0.0.15", "open"), ("I0.0.16", "open"), ("I0.0.18", "closed"), ("I0.0.20", "open")], #t32
									 [("I0.0.15", "open"), ("I0.0.16", "open"), ("I0.0.18", "closed"), ("I0.0.19", "open")], #t33
									 [("I0.0.14", "open"), ("I0.0.16", "open"), ("I0.0.18", "closed"), ("I0.0.19", "open")], #t34
									 [("I0.0.14", "open"), ("I0.0.16", "open"), ("I0.0.18", "open"), ("I0.0.19", "open")]] #t35

for x in range(41):
	linha = f.readline()
	linhaMatriz = []
	for item in linha[4:]:
		if not item in [" ", "\n"]:
			linhaMatriz.append(int(item))
			
	ipnPlantaCompleta.inMatrix.append(linhaMatriz)
	
f.readline()

for x in range(41):
	linha = f.readline()
	linhaMatriz = []
	for item in linha[4:]:
		if not item in [" ", "\n"]:
			linhaMatriz.append(int(item))
			
	ipnPlantaCompleta.outMatrix.append(linhaMatriz)

f.close()

converter = Converter(ipnPlantaCompleta)

ilGenerator = TwidoILGenerator(converter.controlRoutine)
ilGenerator.genIL()
ilGenerator.writeIL('Twido2.xtwd')

ipnCartesiano =  InterpretedPetriNet()
ipnCartesiano.inMatrix = []
ipnCartesiano.outMatrix = []
for x in range(15):
	ipnCartesiano.inMatrix.append(ipnPlantaCompleta.inMatrix[x][:12]) 
	ipnCartesiano.outMatrix.append(ipnPlantaCompleta.outMatrix[x][:12]) 
ipnCartesiano.actions = ipnPlantaCompleta.actions
ipnCartesiano.firingConditions = ipnPlantaCompleta.firingConditions[:12]
ipnCartesiano.m0 = ipnPlantaCompleta.m0[:15]

converterCartesiano = Converter(ipnCartesiano)

ilGeneratorCartesiano = TwidoILGenerator(converterCartesiano.controlRoutine)
ilGeneratorCartesiano.genIL()
ilGeneratorCartesiano.outputIL("cartesiano.txt")

ipnMesa =  InterpretedPetriNet()
ipnMesa.inMatrix = []
ipnMesa.outMatrix = []
for x in range(24):
	ipnMesa.inMatrix.append(ipnPlantaCompleta.inMatrix[x][:19]) 
	ipnMesa.outMatrix.append(ipnPlantaCompleta.outMatrix[x][:19])
ipnMesa.actions = ipnPlantaCompleta.actions
ipnMesa.firingConditions = ipnPlantaCompleta.firingConditions[:19]
ipnMesa.m0 = ipnPlantaCompleta.m0[:24]

converterMesa = Converter(ipnMesa)

ilGeneratorMesa = TwidoILGenerator(converterMesa.controlRoutine)
ilGeneratorMesa.genIL()
ilGeneratorMesa.outputIL("mesa.txt")

ipnAteBalanca =  InterpretedPetriNet()
ipnAteBalanca.inMatrix = []
ipnAteBalanca.outMatrix = []
for x in range(30):
	ipnAteBalanca.inMatrix.append(ipnPlantaCompleta.inMatrix[x][:25]) 
	ipnAteBalanca.outMatrix.append(ipnPlantaCompleta.outMatrix[x][:25]) 
ipnAteBalanca.actions = ipnPlantaCompleta.actions
ipnAteBalanca.firingConditions = ipnPlantaCompleta.firingConditions[:25]
ipnAteBalanca.m0 = ipnPlantaCompleta.m0[:30]

converterAteBalanca = Converter(ipnAteBalanca)

ilGeneratorAteBalanca = TwidoILGenerator(converterAteBalanca.controlRoutine)
ilGeneratorAteBalanca.genIL()
ilGeneratorAteBalanca.outputIL("atebalanca.txt")
