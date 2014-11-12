class GPIOOut():
	"""gpioOut contains the functionality to output to any number of #GPIO pins"""

	def __init__(self, pins):
		"Set pins attribute and call setup"
		
		self.pins = pins
		self.pinState = {}
		self.setupPins()

	def setupPins(self):
		"Setup all pins constructed"

		for pin in self.pins:
		 	#GPIO.setup(pin,GPIO.OUT)
		 	self.pinState[pin] = False

	def setStates(self,states):
		"Switch all pins based on list of bool state values"

		#make sure states is same length as pins
		assert(len(states) == len(self.pins))

		for i,state in enumerate(states):
			self.setState(self.pins[i],onOff)

	def setState(self,pin,state):
		"Switch the given pin on or off depending on bool state"

		if state:
			self.turnOn(pin)
		else:
			self.turnOff(pin)

	def turnOn(self,pin):
		"Turn given pin on"
		#GPIO.output(pin,GPIO.HIGH)
		self.pinState[pin] = True

	def turnOff(self,pin):
		"Turn given pin off"
		#GPIO.output(pin,GPIO.LOW)
		self.pinState[pin] = True

	def getState(self,pin):
		"returns the state of the given pin as bool"

		return self.pinState[pin]

	def getOutput(self,pin):
		"Returns a bool of the pin state"

		return {"pin":pin,"state":self.getState(pin)}

	def getOutputs(self):
		"Returns an object with all the pin states"

		outputs = []

		for pin in self.pins:
			output = self.getOutput(pin)
			outputs.append(output)

		return outputs
