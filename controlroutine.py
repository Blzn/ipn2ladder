import itertools

class ControlRoutine(object):
	
	def __init__(self, initialMarking, supervisedModel, actions, firer):
		self.initialMarking = initialMarking
		self.supervisedModel = supervisedModel
		self.actions = actions
		self.firer = firer
	
class Line(object):
	
	def __init__(self, input, output):
		self.input = input
		self.output = output
	
	def __eq__(self, anotherLine):
		return sorted(self.input) == sorted(anotherLine.input) and sorted(self.output) == sorted(anotherLine.output)