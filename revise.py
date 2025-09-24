# student name
stu_name = "aravind"
# subject marks
maths = int(input("enter the maths mark:"))
science = int(input("enter the science marks:"))
chemistry = int(input("enter the chemistry:"))

total_marks = maths + science + chemistry
avg = total_marks/3



grade ="f"
if avg  >= 90:
    print("grade A")
elif avg >= 80:
    print("grade B")
elif avg >= 60:
    print("grade C")
elif avg >= 40:
    print("grade D")
print(avg)

