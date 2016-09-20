'''
Author	: Nikhil Gabhane
Date	: Sept 20, 2016 
'''
class encryption(object):
	def __init__(self):
		self.letters = "acdegilmnoprstuw"

	def reverse_hash(self,hash_code):
		res = []
		if hash_code == 7:
			return "It's an Empty String"
		if hash_code <259:
			return "Invalid hash code"
		try:
			tmp = hash_code % 37
			hash_code = hash_code - tmp
			res.insert(0,self.letters[tmp])			
			while hash_code != 37 * 7 and hash_code > 0:
				hash_code = hash_code/37
				tmp = hash_code % 37
				res.insert(0,self.letters[tmp])
				hash_code = hash_code - tmp
		except:
			return "Invalide hash code"
		res = "".join(res)
		if hash_code < 0:
			print "Invalid hash code"
		else:
			return res

if __name__ == "__main__":
	#This try block will ensure entered hash code doesn't contain characters
	try:
		hash_code = int(raw_input("Please enter hash code: "))
		enc = encryption()
		res = enc.reverse_hash(hash_code)
		print "Output :", res
	except:
		print "Output : Invalid hash code"




