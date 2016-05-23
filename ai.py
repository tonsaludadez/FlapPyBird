class AI():
	"""This is an AI Implementation for the game Flappy Bird"""
	automata = {}
	currentGameStates = []

	def __init__(self):
		self.automata['N'] = []
		self.automata['J'] = []
		self.automata['D'] = []

	def addToCurrentGame(self,playerState):
		if len(self.currentGameStates) < 1000:
			self.currentGameStates.append(playerState)
		else:
			self.currentGameStates.pop(0)
			self.currentGameStates.append(playerState)

	def gameStart(self):
		currentGameStates = []

	def gameEnd(self):
		index = len(self.currentGameStates) - 1

		while self.currentGameStates[index] in self.automata['D'] and index >= 0:
			index = index - 1

		if index < 0:
			return

		while self.currentGameStates[index] in self.automata['J']:
			self.automata['J'].remove(self.currentGameStates[index])
			self.automata['D'].append(self.currentGameStates[index])
			index = index - 1

		if self.currentGameStates[index] in self.automata['N']:
			self.automata['N'].remove(self.currentGameStates[index])

		self.automata['D'].append(self.currentGameStates[index])
		index = index - 1

		if index < 0:
			return

		self.automata['J'].append(self.currentGameStates[index])
		index = index - 1
		while index >=0:
			if not self.currentGameStates[index] in self.automata['J']:
				self.automata['N'].append(self.currentGameStates[index])
			index = index - 1

	def inJump(self, currentState):
		return currentState in self.automata['J']

	def printAutomata(self):
		print self.automata

	def printJumpStates(self):
		print self.automata['J']

	def printCurrentGameStates(self):
		print self.currentGameStates

		