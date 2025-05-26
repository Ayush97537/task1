# task1
Data Cleaning & Preprocessing Task

Objective

Learn how to clean and prepare raw data for Machine Learning models using Python libraries.

Tools Used
Python
Pandas
NumPy
Seaborn
Matplotlib
Scikit-learn

Dataset
The Titanic dataset is used for this task. It contains passenger information such as age, sex, fare, and survival status.
Steps Performed
1. Import Dataset
Loaded the Titanic dataset using pandas.read_csv() and explored the basic structure.
2. Handle Missing Values
Replaced missing Age values with the median.
Replaced missing Embarked values with the mode.
Dropped the Cabin column due to excessive missing values.
3. Encode Categorical Variables
Converted Sex and Embarked columns into numerical format using one-hot encoding.
4. Feature Scaling
Scaled Age and Fare using StandardScaler to bring them to a similar scale.
5. Outlier Detection & Removal
Visualized outliers using a boxplot.
