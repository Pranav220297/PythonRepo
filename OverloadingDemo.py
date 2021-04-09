class Review:
    def write_review(self,review):
        print(review)
#     def write_review(self):
#         print(review)
def add(x,*data): #  it is tuple
    print(type(data))
    print(x)
    for d in data:
        print(d)
def intro(**data): #key and value it is like dict
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))
intro()
intro(Firstname="Ganesh", Lastname="Babu", Age=25, Phone=1234567890)
intro(Firstname="Mary", Lastname="J", Email="jb@nomail.com", Country="India", Age=25, Phone=9876543210)
add(1,'2',3.5,4,5)
add(1)
# review1=Review()
# review1.write_review("some review about doctor consultation")
