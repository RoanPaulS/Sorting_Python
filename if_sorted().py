word1 = input("Please enter any word : ");
word2 = input("Please enter other word : ");
print("Sorted word1 is ",sorted(word1));
print("Sorted word2 is ",sorted(word2));

if sorted(word1) == sorted(word2):
    print("Both are Equal");
else:
    print("Not Equal");
