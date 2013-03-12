import unittest
from converter import Converter
from ipn import InterpretedPetriNet
from twidoilgenerator import TwidoILGenerator

class TwidoILGeneratorTester(unittest.TestCase):

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
        self.ipn.actions = {("Q0.0.2", "on"): [1, 2, 3],
							("Q0.0.3", "on"): [2]}

        self.ipn.firingConditions = [[("I0.0.0", "closed"), ("I0.0.1", "raising")],
									 [("I0.0.2", "open")],
									 [("I0.0.0", "open"), ("I0.0.3", "open")],
									 [("I0.0.2", "open"), ("I0.0.4", "open")]]

        self.converter = Converter(self.ipn)

        self.ilGenerator = TwidoILGenerator(self.converter.controlRoutine)

        self.initialMarkingInstructions = "<ListInstruction>LDN %M0</ListInstruction>\n" + \
										  "<ListInstruction>[ %MW1 := 0 ]</ListInstruction>\n" + \
										  "<ListInstruction>[ %MW2 := 0 ]</ListInstruction>\n" + \
										  "<ListInstruction>[ %MW3 := 1 ]</ListInstruction>\n" + \
										  "<ListInstruction>[ %MW4 := 1 ]</ListInstruction>\n" + \
										  "<ListInstruction>[ %MW5 := 0 ]</ListInstruction>\n" + \
										  "<ListInstruction>S %M0</ListInstruction>\n"

        self.supervisedModelInstructions = "<ListInstruction>LD %M5</ListInstruction>\n" + \
										   "<ListInstruction>R %M5</ListInstruction>\n" + \
										   "<ListInstruction>[ %MW1 := %MW1 + 1 ]</ListInstruction>\n" + \
										   "<ListInstruction>[ %MW3 := %MW3 - 1 ]</ListInstruction>\n" + \
										   "<ListInstruction>LD %M6</ListInstruction>\n" + \
										   "<ListInstruction>R %M6</ListInstruction>\n" + \
										   "<ListInstruction>[ %MW1 := %MW1 - 1 ]</ListInstruction>\n" + \
										   "<ListInstruction>LD %M7</ListInstruction>\n" + \
										   "<ListInstruction>R %M7</ListInstruction>\n" + \
										   "<ListInstruction>[ %MW2 := %MW2 + 1 ]</ListInstruction>\n" + \
										   "<ListInstruction>[ %MW3 := %MW3 - 1 ]</ListInstruction>\n" + \
										   "<ListInstruction>[ %MW4 := %MW4 - 1 ]</ListInstruction>\n" + \
										   "<ListInstruction>LD %M8</ListInstruction>\n" + \
										   "<ListInstruction>R %M8</ListInstruction>\n" + \
										   "<ListInstruction>[ %MW2 := %MW2 - 1 ]</ListInstruction>\n" + \
										   "<ListInstruction>[ %MW5 := %MW5 + 1 ]</ListInstruction>\n" + \
										   "<ListInstruction>LD %M0</ListInstruction>\n" + \
										   "<ListInstruction>R %M1</ListInstruction>\n" + \
										   "<ListInstruction>LD [ %MW3 >= 1 ]</ListInstruction>\n" + \
										   "<ListInstruction>S %M1</ListInstruction>\n" + \
										   "<ListInstruction>LD %M0</ListInstruction>\n" + \
										   "<ListInstruction>R %M2</ListInstruction>\n" + \
										   "<ListInstruction>LD [ %MW1 >= 1 ]</ListInstruction>\n" + \
										   "<ListInstruction>S %M2</ListInstruction>\n" + \
										   "<ListInstruction>LD %M0</ListInstruction>\n" + \
										   "<ListInstruction>R %M3</ListInstruction>\n" + \
										   "<ListInstruction>LD [ %MW3 >= 1 ]</ListInstruction>\n" + \
										   "<ListInstruction>AND [ %MW4 >= 1 ]</ListInstruction>\n" + \
										   "<ListInstruction>S %M3</ListInstruction>\n" + \
										   "<ListInstruction>LD %M0</ListInstruction>\n" + \
										   "<ListInstruction>R %M4</ListInstruction>\n" + \
										   "<ListInstruction>LD [ %MW2 >= 1 ]</ListInstruction>\n" + \
										   "<ListInstruction>S %M4</ListInstruction>\n"

        self.actionsInstructions = "<ListInstruction>LD [ %MW2 >= 1 ]</ListInstruction>\n" + \
                                   "<ListInstruction>ST %Q0.0.3</ListInstruction>\n" + \
                                   "<ListInstruction>LD [ %MW1 >= 1 ]</ListInstruction>\n" + \
                                   "<ListInstruction>OR [ %MW2 >= 1 ]</ListInstruction>\n" + \
                                   "<ListInstruction>OR [ %MW3 >= 1 ]</ListInstruction>\n" + \
                                   "<ListInstruction>ST %Q0.0.2</ListInstruction>\n"

        self.firerInstructions = "<ListInstruction>LD %M1</ListInstruction>\n" + \
                                 "<ListInstruction>ANDN %I0.0.0</ListInstruction>\n" + \
                                 "<ListInstruction>ANDR %I0.0.1</ListInstruction>\n" + \
                                 "<ListInstruction>S %M5</ListInstruction>\n" + \
								 "<ListInstruction>JMPC %L0</ListInstruction>\n" + \
                                 "<ListInstruction>LD %M2</ListInstruction>\n" + \
                                 "<ListInstruction>AND %I0.0.2</ListInstruction>\n" + \
                                 "<ListInstruction>S %M6</ListInstruction>\n" + \
								 "<ListInstruction>JMPC %L0</ListInstruction>\n" + \
                                 "<ListInstruction>LD %M3</ListInstruction>\n" + \
                                 "<ListInstruction>AND %I0.0.0</ListInstruction>\n" + \
                                 "<ListInstruction>AND %I0.0.3</ListInstruction>\n" + \
                                 "<ListInstruction>S %M7</ListInstruction>\n" + \
								 "<ListInstruction>JMPC %L0</ListInstruction>\n" + \
                                 "<ListInstruction>LD %M4</ListInstruction>\n" + \
                                 "<ListInstruction>AND %I0.0.2</ListInstruction>\n" + \
                                 "<ListInstruction>AND %I0.0.4</ListInstruction>\n" + \
                                 "<ListInstruction>S %M8</ListInstruction>\n" + \
								 "<ListInstruction>JMPC %L0</ListInstruction>\n"

    def testConvertInitialMarkingLines(self):
		self.assertEqual(self.initialMarkingInstructions, self.ilGenerator.convertLayerToIL(self.ilGenerator.controlRoutine.initialMarking))

    def testConvertSupervisedModelLines(self):
		self.assertEqual(self.supervisedModelInstructions, self.ilGenerator.convertLayerToIL(self.ilGenerator.controlRoutine.supervisedModel))

    def testConvertActionsLines(self):
		self.assertEqual(self.actionsInstructions, self.ilGenerator.convertLayerToIL(self.ilGenerator.controlRoutine.actions, "OR"))

    def testConvertFirerlLines(self):
		self.assertEqual(self.firerInstructions, self.ilGenerator.convertLayerToIL(lines = self.ilGenerator.controlRoutine.firer, jumpTo = "L0"))

if __name__ == '__main__':
    unittest.main()
