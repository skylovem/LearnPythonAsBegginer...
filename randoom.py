import random
for x in range(10):
    data=random.randint(1,31)
    print(data)
re=str(data)
print(re)
list=["glory","ahab","juena","nathaniel","alicia"]
def main():
    print(random.sample(list,k=2))
    
main()

