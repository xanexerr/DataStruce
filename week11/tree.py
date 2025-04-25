<<<<<<< HEAD
class Tree:
    
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')
    
    def root(self):
        raise NotImplementedError('must be implemented by subclass')
    
    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')
    
    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')
    
    def children(self, p):
        raise NotImplementedError('must be implemented by subclass')
    
    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')
    
    def is_root(self, p):
        return self.root() == p
    
    def is_leaf(self, p):
        return self.num_children(p) == 0
    
    def is_empty(self):
        return len(self) == 0
    
    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
        
    def _height2(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))
        
    def height(self, p=None):
        if p is None:
            p = self.root()
=======
class Tree:
    
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')
    
    def root(self):
        raise NotImplementedError('must be implemented by subclass')
    
    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')
    
    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')
    
    def children(self, p):
        raise NotImplementedError('must be implemented by subclass')
    
    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')
    
    def is_root(self, p):
        return self.root() == p
    
    def is_leaf(self, p):
        return self.num_children(p) == 0
    
    def is_empty(self):
        return len(self) == 0
    
    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
        
    def _height2(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))
        
    def height(self, p=None):
        if p is None:
            p = self.root()
>>>>>>> 9e27ab5b329a795e16a958d6379acd18504b93e3
        return self._height2(p)