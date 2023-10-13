"""
Rei Onishi
September 28, 2023

This code will decode encoded words.
"""



def main():
	
	#encodedWord = "WBLARF8TTS"
	#encodedWord = "L8KAOUL"
	encodedWord = "E8N8N8"
	#encodedWord = "8TRA8DY T8LA"
	#encodedWord = "8TT LHA TILLTA LIMAS"	
	#encodedWord = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS"
	#encodedWord = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"
	
	
	print(decoded_word(encodedWord))


#Your code goes here.
def decoded_word(encodedWord):
	decoded_word = ""
	for char in encodedWord:
		if char == "T":
			decoded_word += "L"
		elif char == "L":
			decoded_word += "T"
		elif char == "8":
			decoded_word += "A"
		elif char == "B":
			decoded_word += "A"
		elif char == "A":
			decoded_word += "E"
		elif char == "E":
			decoded_word += "B"
		else:
			decoded_word += char
	return decoded_word

if __name__ == "__main__":
    main()
