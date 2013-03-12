import xml.etree.ElementTree as ET

class TwidoILGenerator(object):

	def __init__(self, controlRoutine, breakAtOutput=7):
		self.controlRoutine = controlRoutine
		self.breakAtOutput = breakAtOutput
	
	def writeIL(self, filepath="Twido1.xtwd", encoding="utf-8"):
		outputFile = open('il.txt', "w")
		outputFile.write(self.il)
		TwidoILWriter(self.il, filepath, encoding)
		
	def genIL(self):
		self.il =  self.convertLayerToIL(self.controlRoutine.initialMarking) + \
				   "<ListInstruction>L0:</ListInstruction>\n" + \
                   self.convertLayerToIL(self.controlRoutine.supervisedModel) + \
                   self.convertLayerToIL(self.controlRoutine.actions, "OR") + \
                   self.convertLayerToIL(lines = self.controlRoutine.firer, jumpTo = "L0")

	def convertLayerToIL(self, lines, logicalOperator = "AND", jumpTo=None):
		instructions = ""
		for line in lines:
			instructions += self.convertLineToIL(line, logicalOperator, jumpTo)
		return instructions

	def convertLineToIL(self, line, logicalOperator, jumpTo=None):
		inputInstructions = ""
		instructions = ""
		for input in range(len(line.input)):
				inputInstructions += "<ListInstruction>"
				if not input:
					inputInstructions += "LD"
				else:
					inputInstructions += logicalOperator
				inputInstructions += getattr(self, line.input[input][1])(line.input[input]) + "</ListInstruction>\n"
		if len(line.output) > self.breakAtOutput:
			lineOutputs = [line.output[i:i + self.breakAtOutput] for i in range(0, len(line.output), self.breakAtOutput)]
		else:
			lineOutputs = [line.output]
		for lineOutput in lineOutputs:
			instructions += inputInstructions
			for output in lineOutput:
			   instructions += "<ListInstruction>" + getattr(self, output[1])(output) + "</ListInstruction>\n"
		if jumpTo:
			instructions += "<ListInstruction>JMPC %" + jumpTo + "</ListInstruction>\n"
		return instructions
			
	def open(self, input):
		return " %" + input[0]

	def closed(self, input):
		return "N %" + input[0]
	
	def raising(self, input):
		return "R %" + input[0]
	
	def falling(self, input):
		return "F %" + input[0]
	
	def greaterEqual(self, input):
		return " [ %" + input[0] + " >= " + str(input[2]) + " ]"
	
	def greater(self, input):
		return " [ %" + input[0] + " > " + str(input[2]) + " ]"

	def lesser(self, input):
		return " [ %" + input[0] + " &lt; " + str(input[2]) + " ]"
		
	def assign(self, output):
		return "[ %" + output[0] + " := " + str(output[2]) + " ]"

	def add(self, output):
		if output[2] > 0:
			operator = " + "
		else:
			operator = " - "
		return "[ %" + output[0] + " := %" + output[0] + operator + str(abs(output[2])) + " ]"

	def set(self, output):
		return "S %" + output[0]

	def reset(self, output):
		return "R %" + output[0]

	def on(self, output):
		return "ST %" + output[0]
		
class TwidoILWriter(object):
	
	def __init__(self, controlRoutine, filePath="Twido1.xtwd", encoding="utf-8"):
		self.controlRoutine = controlRoutine
		self.XMLFile = ET.parse(filePath)
		self.root = self.XMLFile.getroot()
		self.program = self.root.findall('Program')[0]
		self.writeControlRoutineOnFile(filePath, encoding)
		
	def writeControlRoutineOnFile(self, filePath, encoding):
		self.cleanProgram()
		section = self.createSection()
		self.appendInstructions(section)
		self.XMLFile.write(filePath, encoding)
		
	def cleanProgram(self):
		for section in self.program.findall('Section'):
			self.program.remove(section)
	
	def createSection(self):
		section = ET.Element('Section', attrib={'SType': '0', 'Display': '1', 'SectionNum': '1'})
		self.program.insert(0, section)
		return section
	
	def appendInstructions(self, section):
		for instructionString in self.controlRoutine.split('\n')[:-1]:
			instruction = ET.fromstring(instructionString)
			section.append(instruction)