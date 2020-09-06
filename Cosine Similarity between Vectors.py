from scipy import spatial

feature_vector = [1,1,1] #this vector represents the preferred features specified by a user (e.g., cushion, comfort, support)
review_vector = [1,0,1] #this vector represents a single review where 0 indicates that the review did not contain the feature and 1 indicates that the review did contain the feature (e.g., cushion, comfort, support)
cosine_similarity = 1 - spatial.distance.cosine(feature_vector, review_vector) #calculates the cosine similarity between the two vectors
