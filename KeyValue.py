class KeyValue:

	keyValCount = 0

	def __init__(self,k,v):
		self.key = k
		self.value = v
		KeyValue.keyValCount += 1

	def getKey(self):
		return self.key

	def getValue(self):
		return self.value

	def setValue(self,v):
		self.value = v

	def setKey(self,k):
		self.key = k

	def getCount():
		return KeyValue.keyValCount

	def hashFunctionGR(self,s):
		return (.618033*self.key)%s