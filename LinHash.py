class LinHash:



	def __init__(self,size):
		self.table = myList=[-1 for i in range(size)]

	def insert(i,val,size):
		if(self.table[i] == -1):
			self.table[i] = val
		else:
			count = 0
			while(self.table[i] != -1 && count < size):
				if(i == size - 1):
					i = 0
				else:
					i += 1
				count += 1

			if(count >= len(self.table)):
				print "The Hash Table is full, delete something or go away"
			else:
				self.table[i] = val

	def printHash():
		print self.table

	def delete(i):
		self.table[i] = -1