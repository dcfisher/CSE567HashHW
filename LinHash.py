class LinHash:

     def __init__(self,size):
          self.table = [-1 for i in range(size)]
          self.size = size

     def insert(self,i,val):
          if(self.table[i] == -1):
               self.table[i] = val
          else:
               count = 0
               while(self.table[i] != -1 and count <= self.size):
                    if(i == self.size - 1):
                         i = 0
                    else:
                         i += 1
                    count += 1

               if(count >= len(self.table)):
                    print ("The Hash Table is full, delete something or go away")
               else:
                    self.table[i] = val

     def printHash(self):
                count = 0
                for t in self.table:
                        
                        if(t == -1):
                                print("Null")
                        else:
                                print("Index %d: Key = %d   Value = %s" %(count, t.getKey(),t.getValue()))
                        count +=1      

     def delete(self,i):
          self.table[i] = -1

     def find(self,kv):
          h = kv.hashFunctionGR(self.size)
          h = int(h)
          count = 1
          while(count <= self.size):
               if(self.table[h] == -1):
                    print("not found")
                    return count

               elif(self.table[h].getKey() == kv.getKey()):
                    print("found")
                    return count
                    
               else:
                     h+=1
                     count+=1
                     if(h >= self.size):
                          h = 0
          return count   