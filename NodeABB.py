class NodeABB:
	def __init__(self, data=None, esq=None, dir=None):
		self._data = data
		self._esq = esq
		self._dir = dir
		self._tam = 1 if data else 0

	def setRaizArbin(self, elem):
		self._data = elem

	def raizArbin(self):
		return self._data

	def setEsqArbin(self, arbin):
		self._esq = arbin
		
	def esqArbin(self):
		return self._esq
		
	def setDirArbin(self, arbin):
		self._dir = arbin

	def dirArbin(self):
		return self._dir
		
	def __len__(self):
		return self._tam

	def add(self, node):
		if self.raizArbin() is None:
			self.setRaizArbin(node.raizArbin())
		elif node.raizArbin() < self.raizArbin():
			if self.esqArbin() is None:
				self.setEsqArbin(node)
			else:
				self.esqArbin().add(node)
		elif node.raizArbin() > self.raizArbin():
			if self.dirArbin() is None:
				self.setDirArbin(node)
			else:
				self.dirArbin().add(node)
	
		self._tam += 1

	def min(self):
		return self if self.esqArbin() is None else self.esqArbin().min()
		
	def removeMin(self):
		if self.esqArbin() is None:
			return self.dirArbin()

		self.setEsqArbin(self.esqArbin().removeMin())

		return self
		
	def remove(self, elem):
		if elem < self.raizArbin():
			self.setEsqArbin(self.esqArbin().remove(elem))
		elif elem > self.raizArbin():
			self.setDirArbin(self.dirArbin().remove(elem))
		else:
			if self.dirArbin() is None:
				return self.esqArbin()
			if self.esqArbin() is None:
				return self.dirArbin()

			tmp = self.dirArbin().min()
			self.setRaizArbin(tmp.raizArbin())
			self.dirArbin().removeMin()

		return self
