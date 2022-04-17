import re
#Decode a base64 text
def base64Decode(text):
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
    bit_str=""
    text_str=""

    #Loop through every char
    for char in text:
        #Ignore characters, which are not in the alphabet. Concatenate the binary representation of alphabet index of char
        if char in alphabet:
            bin_char = bin(alphabet.index(char)).lstrip("0b")
            bin_char = (6-len(bin_char))*"0" + bin_char
            bit_str += bin_char

    #Make 8bit - 2byte brackets
    brackets = re.findall('(\d{8})', bit_str)

    #Decode char binary -> ascii
    for bracket in brackets:
        text_str+=chr(int(bracket,2))

    return text_str

to_decode="RGF0YSBTZWN1cml0eQ=="
print("Masage to decode: "+to_decode)
decoded= base64Decode(to_decode)
print ("Base64 decoded: "+decoded)