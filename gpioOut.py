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

	def switchPins(self,onOffList):
		"Switch all pins based on list of bool onOff values"

		#make sure onOffList is same length as pins
		assert(len(onOffList) == len(self.pins))

		for i,onOff in enumerate(onOffList):
			self.switchPin(self.pins[i],onOff)

	def switchPin(self,pin,onOff):
		"Switch the given pin on or off depending on bool onOff"

		if onOff:
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


	def getOutput(self,pin):
		"Returns a bool of the pin state"

		return {"pin":pin,"state":self.pinState[pin]}

	def getOutputs(self):
		"Returns an object with all the pin states"

		outputs = []

		for pin in self.pins:
			output = {}
			output["pin"]=pin
			output["state"]=self.getOutput(pin)
			outputs.append(output)

		return output
