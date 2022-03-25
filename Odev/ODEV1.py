Class1 = [1,2,5,6,7,8,6,4,7,3,6,3,2,6,7,4]
Class2 = [1,4,5,6,7,6,6,4,6,4,7,3,2,6,7,4]
Class3 = [2,2,5,4,7,8,3,4,7,5,6,3,2,6,7,4]
Class4 = [7,2,5,6,7,4,6,5,7,5,6,3,3,6,7,4]



def BestClass(s1, s2, s3, s4):
    avg1 = sum(s1) / len(s1)
    avg2 = sum(s2) / len(s2)
    avg3 = sum(s3) / len(s3)
    avg4 = sum(s4) / len(s4)
    Classes = [avg1, avg2, avg3, avg4]
    return max(Classes)

Sonuc = BestClass(Class1,Class2, Class3, Class4)
print(Sonuc)
