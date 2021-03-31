from tools.print_info import print_info


print("列表推导式")


A = [1, 2, 3, 4, 5, 6, 7, 8]

a = [i for i in A if i >= 3]
print(a)

employee_old = [{'Name': 'Adam', 'Salary': 100},
                {'Name': 'Bob', 'Salary': 150},
                {'Name': 'Cindy', 'Salary': 200}]
employee_new = [{'Name': employee['Name'], 'Salary': employee['Salary']+200} if employee['Salary'] > 150
                else
                {'Name': employee['Name'], 'Salary': employee['Salary']+500} for employee in employee_old]
"""
# employees_new = [
#     {'name': employee['name'], 'salary': employee['salary'] + 200} if employee['salary'] > 5000 else
#     {'name': employee['name'], 'salary': employee['salary'] + 500} for employee in employee_old]
"""
#print(employees_new)
print(employee_new)


print_info("字典推导式")
dict_old = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}
dict_new = {value: key for key, value in dict_old.items()}
print(dict_new)


print_info("集合推导式:典型用法 -- 去重")
list_old = [1, 2, 3, 5, 2, 3]
set_new = {x for x in list_old}
print(set_new)

print_info("生成器")
my_generator = (x for x in range(5)) # 注意是()
print(my_generator)
print(type(my_generator))
print('a')
print(my_generator.__next__())
print('b')
print(next(my_generator))
print('c')
for i in my_generator:
    print(i)
# 只能遍历一遍
# print(next(my_generator))
# print(next(my_generator))


print_info("借助yield建造生成器")
def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        n += 1
        yield b #return b + 暂停
        a, b = b, a+b

g = fib(5)
print(g)
print(next(g))