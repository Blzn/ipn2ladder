from controlroutine import ControlRoutine, Line
import itertools

class Converter(object):
	
	def __init__(self, ipn):
		self.ipn = ipn
		self.controlRoutine = self.genControlRoutine()
		
	def genInitialMarking(self):
		lineInput = [("M0", "closed")]
		lineOutput = [("MW" + str(place + 1), "assign", self.ipn.m0[place]) for place in range(len(self.ipn.m0))] + [("M0", "set")]
		yield Line(lineInput, lineOutput)
		
	def genSupervisedModelPartI(self):
		numOfTransitions = len(self.ipn.inMatrix[0])
		for trans in range(numOfTransitions):
			lineInput = [("M" + str(numOfTransitions + 1 + trans), "open")]
			lineOutput = [("M" + str(numOfTransitions + 1 + trans), "reset")]
			for place in range(len(self.ipn.inMatrix)):
				if self.ipn.inMatrix[place][trans]:
					lineOutput.append(("MW" + str(place + 1), "add", -self.ipn.inMatrix[place][trans]))
				if self.ipn.outMatrix[place][trans]:
					lineOutput.append(("MW" + str(place + 1), "add", self.ipn.outMatrix[place][trans]))
			yield Line(lineInput, lineOutput)
		
	def genSupervisedModelPartII(self):
		numOfTransitions = len(self.ipn.inMatrix[0])		
		numOfPlaces = range(len(self.ipn.inMatrix))
		resetLineInput = [("M0", "open")]
		for trans in range(numOfTransitions):
			resetLineOutput = [("M" + str(trans + 1), "reset")]
			lineInput = [("MW" + str(place + 1),  "greaterEqual", self.ipn.inMatrix[place][trans]) for place in numOfPlaces if self.ipn.inMatrix[place][trans]]
			lineOutput = [("M" + str(trans + 1), "set")]
			yield Line(resetLineInput, resetLineOutput)
			yield Line(lineInput, lineOutput)
			
	def genSupervisedModel(self):
		return itertools.chain(self.genSupervisedModelPartI(), self.genSupervisedModelPartII())
		
	def genActions(self):
		for lineOutput, places in self.ipn.actions.iteritems():
			lineInput = [("MW" + str(place),  "greaterEqual", 1) for place in places]
			yield Line(lineInput, [lineOutput])
				
	def genFirer(self):
		numOfTransitions = len(self.ipn.inMatrix[0])
		for trans in range(numOfTransitions):
			lineInput = [("M" + str(trans + 1), "open")] + self.ipn.firingConditions[trans]
			lineOutput = [("M" + str(numOfTransitions + 1 + trans), "set")]
			yield Line(lineInput, lineOutput)
			
	def genControlRoutine(self):
		return ControlRoutine(self.genInitialMarking(), self.genSupervisedModel(), self.genActions(), self.genFirer())