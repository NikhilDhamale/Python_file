
#vowels in python 

word="artificial intelligence is the most imp thing in comp. "

count=0

for ch in word:
    if(ch=='a'or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        count=count+1

print("this is vowels : ",count)