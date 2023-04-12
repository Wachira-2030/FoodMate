
class RecipeRecommender:
    
    def __init__(self, df):
        self.df = df
        
    def recommend(self, target_calories, num_recommendations=5):
        recommendations = []
        for index, row in self.df.iterrows():
            if row['calories'] == target_calories:
                recommendations.append((row['name'], row['ingredients'],row['steps']))
            if len(recommendations) == num_recommendations:
                break
        return recommendations
