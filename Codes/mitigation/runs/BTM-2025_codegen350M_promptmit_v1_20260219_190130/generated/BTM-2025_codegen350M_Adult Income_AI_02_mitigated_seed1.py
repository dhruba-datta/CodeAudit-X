# Import all the required packages
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

# Import the data
data = pd.read_csv('housing.csv')

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data[['age', 'hours_per_week', 'education', 'occupation']]
                                                   , data['income']
                                                   , test_size=0.2
                                                   , random_state=42)

# Create a linear regression model and fit it to the training data
model = LinearRegression()
model.fit(X_train, y