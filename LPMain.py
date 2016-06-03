from KeyValue import KeyValue
from LinHash import LinHash
import random

def main():
     size = [1113,1327,1511,2003,3001,4001,5003,9001]
     sizeD = [1009,1321,1499,1999,2999,3989,4999,8999]
     kvSize = 1000
     randInts = random.sample(range(100,9999),kvSize)
     randIntsMiss = random.sample(range(100,9999),kvSize)
     hits = []
     misses = []
     kv = []
     lf = []
     hitTries = []
     missTries = []
     hitTries2 = []
     missTries2 = []
     hashStore = []
     hashStore2=[]
     
     for i in range(0,kvSize-1):
         keyVal = KeyValue(randInts[i],randInts[i+1])
         keyValMiss = KeyValue(randIntsMiss[i],randIntsMiss[i+1])
         misses.append(keyValMiss)
         kv.append(keyVal)
         hits.append(keyVal)

     makeTheHash(size,kv,lf,hashStore)
     testTheHash(hits,misses,kvSize,hitTries,missTries,hashStore,lf)

     print("\n\n")
     makeTheDoubleHash(size,kv,lf,hashStore2,sizeD)
     testTheHash(hits,misses,kvSize,hitTries2,missTries2,hashStore2,lf)


def makeTheHash(size, kv, lf, hashStore):
     i = 0
     for s in size:    
         hsh = LinHash(s)
         for v in kv:
              h = v.hashFunctionGR(s)
              hsh.insert(int(h),v,s)

         lf.append(len(kv)/s)
         hashStore.append(hsh)

def makeTheDoubleHash(size, kv, lf, hashStore,sD):
     i = 0
     for s in size:    
         hsh = LinHash(s)
         for v in kv:
              hf = v.hashFunctionGR(s)
              if(hsh.find(v) == -1):
                   hsh.insert(int(hf),v,s)
              else:
                   hf = v.hashFunctionGR(sD[i])
                   hsh.insert(int(hf),v,sD[i])
         i+=1
         hashStore.append(hsh)


def testTheHash(hits,misses,kvSize,hitTries,missTries,hashStore,lf):
     for hsh in hashStore:
          tot = 0
          for hit in hits:
               t = hsh.find(hit)
               tot += t     
          hitTries.append(tot/kvSize)
                  
          tot = 0
          for miss in misses:
               t = hsh.find(miss)
               tot += t
          missTries.append(tot/kvSize)
          
##     hashStore[3].printHash()
     
     print("Load Factor ", end="| ")
     for load in lf:
         print("{l:.2f}".format(l = load),end="| ")   
     print()
     print("Search Hit  ", end="| ")
     for hit in hitTries:
         print("{h:4.1f}".format(h = hit),end="| ") 
     print()
     print("Search Miss ", end="| ")
     for miss in missTries:
         print("{m:4.1f}".format(m = miss),end="| ")
     print()
     print("HitsToMisses", end="| ")
     i = 0
     for miss in missTries:
         print("{r:4.2f}".format(r = hitTries[i]/miss),end="| ")
         i+=1

     print()
     knuth = [(5.5/55.5),(3.0/8.5),(2.0/5.0),(1.5/2.5)]
     print("Knuth Est.  ", end="| ")
     for kn in knuth:
         print("{k:4.2f}".format(k = kn),end="| ")
         

main()
