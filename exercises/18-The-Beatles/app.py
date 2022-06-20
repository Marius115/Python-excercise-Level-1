# Your code here!!
def sing ():
    song = ""
    for i in range (8):
        if i == 4:
           # print ("whisper words of wisdom,let it be, let it be")
            song += "whisper words of wisdom, let it be, let it be, "
        else:
            song=song+ "let it be, "
            # print ("let it be,")
    song += "there will be an answer, let it be"
    # print ("there will be an answer, let it be")
    return song     
print(sing())
