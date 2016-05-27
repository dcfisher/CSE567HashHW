class KeyValue:

	keyValCount = 0

	def __init__(self,v,k):
		self.key = k
		self.value = v
		KeyValue.keyValCount += 1

	def getKey():
		return self.key

	def getValue():
		return self.value

	def setValue(v):
		self.value = v

	def setKey(k):
		self.key = k

	def getCount():
		return KeyValue.keyValCount

	def hashFunctionGR():
		return (.618033*self.key)%100