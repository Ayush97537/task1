df = pd.read_csv('titanic.csv')

Explore dataset

print(df.head()) print(df.info()) print(df.describe())

Handle missing values

print("Missing values before:") print(df.isnull().sum())

df['Age'].fillna(df['Age'].median(), inplace=True) df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True) df.drop(columns=['Cabin'], inplace=True)  # Drop column with too many missing values

print("Missing values after:") print(df.isnull().sum())

Encode categorical variables

df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

Feature scaling for numerical columns

scaler = StandardScaler() df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

Detect and remove outliers using IQR for 'Fare'

Q1 = df['Fare'].quantile(0.25) Q3 = df['Fare'].quantile(0.75) IQR = Q3 - Q1

df = df[(df['Fare'] >= Q1 - 1.5 * IQR) & (df['Fare'] <= Q3 + 1.5 * IQR)]

Visualize outliers with boxplot

sns.boxplot(x=df['Fare']) plt.title('Boxplot of Fare (Outliers Removed)') plt.show()

Final dataset info

print(df.info()) print(df.head())