import KeyValue
import LinHash

def main:
	size = [10,15,20,30,40,50]
	v1 = KeyValue(40512, "Dustin Fisher")
	v2 = KeyValue(44123, "Rusty Venture")
	v3 = KeyValue(12826, "Doc Hammer")
	v4 = KeyValue(51825, "Brock Samson")
	v5 = KeyValue(57230, "Dean Venture")
	v6 = KeyValue(57123, "The Monarch")
	v7 = KeyValue(81727, "Dr Girlfriend")
	v8 = KeyValue(34716, "Billy Quizboy")
	v9 = KeyValue(67192, "Pete White")
	v10 = KeyValue(03471, "Byron Orpheus")

	kv = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10]


	for s in size:
		hash = LinHash(s)
		for v in kv:
			h = v.hashFunctionGR()
			hash.insert(h,v,s)
		
		hash.printHash()
		lf = len(kv)/size
		print("\n\n") 



main()