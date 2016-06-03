class LinHash:

     def __init__(self,size):
          self.table = [-1 for i in range(size)]
          self.size = size

     def insertD(self,i,val,size):
          self.size = size
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

     def delete(self,kv):
          h = kv.hashFunctionGR(self.size)
          h = int(h)
          c = self.find(kv)
          h += c-1
          self.table[h] = -1

     def find(self,kv):
          h = kv.hashFunctionGR(self.size)
          h = int(h)
          count = 1
          while(count <= self.size):
               if(self.table[h] == -1):
                    return count
               elif(self.table[h].getKey() == kv.getKey()):
                    return count
               else:
                     h+=1
                     count+=1
                     if(h >= self.size):
                          h = 0
          return count




          
