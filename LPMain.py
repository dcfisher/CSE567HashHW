import KeyValue
import LinHash

def main:
	size = [11]
	v1 = KeyValue(12, "Dustin Fisher")
    v2 = KeyValue(23, "Rusty Venture")
    v3 = KeyValue(36, "Doc Hammer")
    v4 = KeyValue(95, "Brock Samson")
    v5 = KeyValue(80, "Dean Venture")
    v6 = KeyValue(53, "The Monarch")
    v7 = KeyValue(47, "Dr Girlfriend")
    v8 = KeyValue(16, "Billy Quizboy")
    v9 = KeyValue(92, "Pete White")
    v10 = KeyValue(71, "Byron Orpheus")

    v11 = KeyValue(12, "Dustin Fisher")
    v12 = KeyValue(23, "Rusty Venture")
    v13 = KeyValue(36, "Doc Hammer")
    v14 = KeyValue(95, "Brock Samson")
    v15 = KeyValue(80, "Dean Venture")
    v16 = KeyValue(53, "The Monarch")
    v17 = KeyValue(47, "Dr Girlfriend")
    v18 = KeyValue(16, "Billy Quizboy")
    v19 = KeyValue(92, "Pete White")
    v20 = KeyValue(71, "Byron Orpheus")

    v21 = KeyValue(13, "Dustin Fisher")
    v22 = KeyValue(22, "Rusty Venture")
    v23 = KeyValue(31, "Doc Hammer")
    v24 = KeyValue(90, "Brock Samson")
    v25 = KeyValue(81, "Dean Venture")
    v26 = KeyValue(52, "The Monarch")
    v27 = KeyValue(47, "Dr Girlfriend")
    v28 = KeyValue(18, "Billy Quizboy")
    v29 = KeyValue(98, "Pete White")
    v30 = KeyValue(75, "Byron Orpheus")
     
    kv = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10]
    hits = [v11,v12,v13,v14,v15,v16,v17,v18,v19,v20]
    misses = [v21,v22,v23,v24,v25,v26,v27,v28,v29,v30]
     

	lf = []

    hash = LinHash(size)
    for v in kv:
        h = v.hashFunctionGR(size)
        hash.insert(int(h),v)
                 
##     hash.printHash()
    lf.append(len(kv)/size)
     
    print("Load factor is %0.0f percent" %(100*lf[0])) 

    c = hash.find(v12)
    d = hash.find(v21)

    print(c)
    print(d)


main()