import pandas as pd

# 输入数据
train_date = pd.read_csv('D:\\D\\python\\Titanic_Data-master\\train.csv')
test_date = pd.read_csv('D:\\D\\python\\Titanic_Data-master\\test.csv')

# # 查看数据基础信息，对数据格式和缺失值进行判断
# print(train_date.info())
# print('------')
# print(train_date.describe())
# print('------')
# print(train_date.describe(include=['O']))
# print('-'*30)
# print(test_date.info())

# # 查看Embarked数值的计数
# print(train_date['Embarked'].value_counts())



# # 对缺失值和0的值进行填充
train_date['Age'].fillna(train_date['Age'].mean(), inplace=True)
test_date['Age'].fillna(test_date['Age'].mean(), inplace=True)
train_date['Fare'].fillna(train_date['Fare'].mean(), inplace=True)
test_date['Fare'].fillna(test_date['Fare'].mean(), inplace=True)
train_date['Embarked'].fillna('S', inplace=True)
train_date['Fare'].replace(0, train_date['Fare'].mean(), inplace=True)
test_date['Fare'].replace(0, test_date['Fare'].mean(), inplace=True)


print(train_date.info())
print('------')
print(test_date.info())
print('------')
print(train_date.describe(include=['O']))
print('------')
print(test_date.describe())

# for i in range(len(train_date['Fare'])):
#     if train_date.loc[i, 'Fare'] == 0:
#         print(train_date.loc[i, 'Name'])

# # 提取数据的特征选择
feature = ['Pclass', 'Sex', 'Age', 'SibSp', '']
