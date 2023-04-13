# FoodMate:From kitchen to table – Foodmate's got you covered with recipe recommendations.

## Introduction

![pexels-larissa-farber-16190930](https://user-images.githubusercontent.com/58382818/182008486-01c0a56b-f055-4d94-b38f-7d838d5f8b0f.png)


## Business Understanding
The food and health industry is a highly competitive and crowded space. With so many diet plans, meal delivery services, and health apps available, it can be overwhelming for individuals to navigate and make informed decisions about their dietary choices. This creates a major business problem for stakeholders who want to provide effective solutions that meet the needs of their customers. One major issue is the lack of personalized nutrition recommendations available in the market. Many existing meal delivery services and health apps provide generic diet plans that are not tailored to an individual's specific needs and preferences. This can lead to frustration and disappointment, as customers may not see the desired results and may eventually give up on their healthy eating goals altogether. Another challenge is the time and effort required to plan and prepare healthy meals. Many individuals lead busy lives and do not have the time or energy to research and create nutritious meals every day. 
<br><br>
This can lead to unhealthy eating habits and may have negative consequences on their overall health and wellbeing. To address these challenges, stakeholders need to develop innovative solutions that provide personalized and convenient dietary recommendations. The food recommender system with a chatbot offers a unique and effective solution that addresses these challenges. It utilizes advanced technology to analyze an individual's weight and BMI and provides personalized diet recommendations for breakfast, lunch, and dinner. It also includes easy-to-follow recipes for each meal, making healthy eating more accessible and convenient for individuals. Overall, the business problem for stakeholders is to provide effective solutions that meet the needs of individuals in the highly competitive and crowded food and health industry. The food recommender system with a chatbot offers a unique and innovative solution that addresses the lack of personalized nutrition recommendations and the time and effort required to plan and prepare healthy meals.

## Main Objectives
* To develop a Food/recipe Recommendation system that suggests nutritious food to individuals and gym instructors thus promoting a healthy lifestyle


## Specific Objectives
* Identify the key features and factors that impact an individual's overall health, and determine which ones should be incorporated into the food recommendation system.
* Clean and preprocess the nutrition data available in the dataset, and combine it with external data sources to create a comprehensive nutrition database that can be used by the recommendation system.
* Develop and implement recommendation algorithms that can generate personalized food recommendations based on the user's individual characteristics such as age, gender, degree of physical activity, locally available foods, and dietary customs.
* Create a chatbot that can interact with users and collect relevant information such as dietary preferences, and restrictions, as well as any other relevant information that can be used to personalize food recommendations.
* Integrate the recommendation algorithms and chatbot into a user-friendly and intuitive interface that allows users to easily access and interact with the system.
* Deploy the food recommendation system and chatbot, and conduct user testing to gather feedback and identify areas for improvement.



## Data Preparation and .
*Assessing the Data:* The recipe dataset contains  a list of 230186 rows of recipes and 12 columns while the nutrition dataset contains information on approximately 8.8 thousand types of food. The dataset includes various features related to the nutrition value of each food item per 100gram serving. There are 75 features in total, you can find features like calories, vitamin_d, zink, protein, lactose. 

## modeling
The project started off with a baseline model which was a class that takes in the data frame .The recommend method takes as input a target calorie value and the number of recommendations desired, and returns a list of food recommendations that have equal and less calories than the target calorie value.

The model was further advanced by coming up with  KNN and SVD models.  The KNN means model performed better and was tuned using the hyperparameters .



<br><br>
*Data Cleaning:* A new dataframes were created to contain relevant features.  Data in the nutrition dataset were stripped of irrelevant characters, converted to float type and columns renamed to contain units of measurements.  Data in the recipe data frame was converted to object type to float. The dataframes were then checked to identify the presence of duplicates and missing values. The recipe dataset only had one missing value which was dropped. Outliers were then identified and removed.
<br><br>
*Exploring the Data/Selecting Features:* To build an effective food recommendation system, a comprehensive exploratory data analysis (EDA) was conducted. This involved examining the key features of the dataset, including nutrient information, calorie count, and serving size.
<br><br>
To get a better understanding of the dataset, visualizations such as scatter plots and  box plots were created. Scatter plots were used to explore the relationship between calorie count and various nutrients such as total fat, saturated fat, cholesterol, sodium, and potassium.
<br><br>
Box plots were used to examine the distribution of key nutrient values such as protein, carbohydrates, sugar, and sodium. These plots provided insights into the distribution of these values and helped to identify any potential outliers or anomalies.
<br><br>
In addition, a word cloud was utilized to capture a holistic view of the text and identify the most frequent ingredients used.
<br><br>
Overall, the EDA analysis provided valuable insights into the key features of the dataset and helped to identify any potential issues or challenges that needed to be addressed before building the food recommendation system.


<br><br>
*Making Predictions:* The project started off with a baseline model which was a class that takes in the data frame .The recommend method takes as input a target calorie value and the number of recommendations desired, and returns a list of food recommendations that have equal and less calories than the target calorie value.
<br><br>
The model was further advanced by coming up with  KNN and SVD models.  The KNN means model performed better and was tuned using the hyperparameters .



## Conclusion.
* This model architecture  can be used to meet specific user calories by recommending specified calorie counts

* A number of healthy recipes are available for users , making our  model diverse
 
* Our project will greatly contribute to the health industry by helping individuals make more informed food choices


## Recommendations
* The performance of the model can in the future include more recipes, especially for locally available foods.
<br><br>
* Continuously update and improve your system by incorporating user feedback and adding new features and datasets.
<br><br>
* Collect user preference data through surveys, feedback forms, or user interaction with the recommender system.

## Minimum Viable Product
In order to calculate nutritional recommendations for users, any algorithm needs the following information:
<br><br>
* User information (e.g., likes, dislikes, food consumption, or nutritional needs)
<br><br>
* A set of constraints or rules which will improve the quality of recommendation process. Constraints like health details (heart disease system should recommend menus with less fat and salt.)
<br><br>
* food recommender systems should take into account constraints with regard to the availability of ingredients in the households 



