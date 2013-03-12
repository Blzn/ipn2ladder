import unittest
from ipn import InterpretedPetriNet
from converter import Converter
from controlroutine import ControlRoutine, Line

class ConverterTester(unittest.TestCase):

	def setUp(self):
		self.ipn = InterpretedPetriNet()
		self.ipn.inMatrix = [[0, 1, 0, 0],
							 [0, 0, 0, 1],
							 [1, 0, 1, 0],
							 [0, 0, 1, 0],
							 [0, 0, 0, 0]]
		self.ipn.outMatrix = [[1, 0, 0, 0],
							  [0, 0, 1, 0],
							  [0, 0, 0, 0],
							  [0, 0, 0, 0],
							  [0, 0, 0, 1]]
		self.ipn.m0 = [0, 0, 1, 1, 0]
		self.ipn.actions = {("Q0.2", "on"): [1, 2, 3],
							("Q0.3", "on"): [2]}
		self.ipn.firingConditions = [[("I0.0", "off"), ("I0.1", "on")],
									 [("I0.2", "on")],
									 [("I0.0", "on"), ("I0.3", "on")],
									 [("I0.2", "on"), ("I0.4", "on")]]
							
		self.converter = Converter(self.ipn)
		
		self.initialMarkingLine = Line([("M0", "closed")], [("MW1", "assign", 0), ("MW2", "assign", 0), ("MW3", "assign", 1), ("MW4", "assign", 1), ("MW5", "assign", 0), ("M0", "set")])
		
		self.supervisedModelPartILines = []
		self.supervisedModelPartILines.append(Line([("M5", "open")],[("MW3", "add", -1), ("MW1", "add", 1), ("M5", "reset")]))
		self.supervisedModelPartILines.append(Line([("M6", "open")],[("MW1", "add", -1), ("M6", "reset")]))
		self.supervisedModelPartILines.append(Line([("M7", "open")],[("MW3", "add", -1), ("MW4", "add", -1),("MW2", "add", 1), ("M7", "reset")]))
		self.supervisedModelPartILines.append(Line([("M8", "open")],[("MW2", "add", -1), ("MW5", "add", 1), ("M8", "reset")]))

		self.supervisedModelPartIILines = []
		self.supervisedModelPartIILines.append(Line([("M0", "open")], [("M1", "reset")]))
		self.supervisedModelPartIILines.append(Line([("MW3", "greaterEqual", 1)],[("M1","set")]))
		self.supervisedModelPartIILines.append(Line([("M0", "open")], [("M2", "reset")]))
		self.supervisedModelPartIILines.append(Line([("MW1", "greaterEqual", 1)],[("M2","set")]))
		self.supervisedModelPartIILines.append(Line([("M0", "open")], [("M3", "reset")]))
		self.supervisedModelPartIILines.append(Line([("MW3", "greaterEqual", 1), ("MW4", "greaterEqual", 1)],[("M3","set")]))
		self.supervisedModelPartIILines.append(Line([("M0", "open")], [("M4", "reset")]))
		self.supervisedModelPartIILines.append(Line([("MW2", "greaterEqual", 1)],[("M4","set")]))		
		
		self.supervisedModelLines = self.supervisedModelPartILines + self.supervisedModelPartIILines
	
		self.actionsLines = []
		self.actionsLines.append(Line([("MW1", "greaterEqual", 1), ("MW2", "greaterEqual", 1), ("MW3", "greaterEqual", 1)], [("Q0.2", "on")]))
		self.actionsLines.append(Line([("MW2", "greaterEqual", 1)], [("Q0.3", "on")]))
		
		self.firerLines = []
		self.firerLines.append(Line([("M1", "open")] + self.ipn.firingConditions[0], [("M5", "set")]))
		self.firerLines.append(Line([("M2", "open")] + self.ipn.firingConditions[1], [("M6", "set")]))
		self.firerLines.append(Line([("M3", "open")] + self.ipn.firingConditions[2], [("M7", "set")]))
		self.firerLines.append(Line([("M4", "open")] + self.ipn.firingConditions[3], [("M8", "set")]))
			
	def testGenInitialMarking(self):
		self.assertEqual(list(self.converter.genInitialMarking())[0], self.initialMarkingLine)
	
	def testGenSupervisedModelPartI(self):
		self.assertEqual(list(self.converter.genSupervisedModelPartI()), self.supervisedModelPartILines)
	
	def testGenSupervisedModelPartII(self):
		self.assertEqual(list(self.converter.genSupervisedModelPartII()), self.supervisedModelPartIILines)
	
	def testGenSupervisedModel(self):
		self.assertEqual(list(self.converter.genSupervisedModel()), self.supervisedModelLines)
		
	def testGenActions(self):
		self.assertEqual(list(self.converter.genActions()), self.actionsLines)
		
	def testGenFirer(self):
		self.assertEqual(list(self.converter.genFirer()), self.firerLines)
		
		
if __name__ == '__main__':
    unittest.main()

