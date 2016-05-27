from KeyValue import KeyValue
from LinHash import LinHash
import random

def main():
     size = 2001
     randInts = random.sample(range(100,9999),100)
     randIntsMiss = random.sample(range(100,9999),100)
     hits = []
     misses = []
     kv = []
     
     
     for i in range(0,99):
         keyVal = KeyValue(randInts[i],randInts[i+1])
         keyValMiss = KeyValue(randIntsMiss[i],randIntsMiss[i+1])
         misses.append(keyValMiss)
         kv.append(keyVal)
         hits.append(keyVal)
     

	lf = []

     hash = LinHash(size)
     for v in kv:
         h = v.hashFunctionGR(size)
         hash.insert(int(h),v)
                 
##     hash.printHash()
     lf.append(len(kv)/size)
     
     print("Load factor is %0.0f percent" %(100*lf[0]))                   
     
     s = 0
     for hit in hits:
         t = hash.find(hit)
         s += t     
     print("Search Hit: %0.2f" %(s/100))
     
     s = 0
     for miss in misses:
         t = hash.find(miss)
         s += t
     print("Search Miss: %0.2f" %(s/100))

     
main()
