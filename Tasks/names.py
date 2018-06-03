def censor(text, m):

    word_list = text.split()
    result = ''
    stars = '*' * len(m)
 
    count = 0

    index = 0;
    for i in word_list:
 
        if i == m:
            word_list[index] = stars
        index += 1
 
    # join the words
    result =' '.join(word_list)
 
    return result
 
# Driver code
if __name__== '__main__':
     
    extract = "GeeksforGeeks is a computer science portal for geeks.\
               I am pursuing my major in computer science. "               
    cen = "computer"   
    print(censor(extract, cen))
