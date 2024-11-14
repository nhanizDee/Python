from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import MultinomialNB

# Import dataset
jobPosts = pd.read_csv('job_posts.csv')

# Create input matrix X and output matrix y
X = jobPosts['company_profile']
y = jobPosts['fake']

# Reformat job posts using CountVectorizer()
vectorizer = CountVectorizer()
vectorizer = vectorizer.fit(X)
XVectorized = vectorizer.transform(X)

# View word list
print(vectorizer.get_feature_names_out())