import numpy as np

# # exercise number 1
# gym_data = np.array([
#     [28, 75, 175, 4],
#     [34, 68, 168, 3],
#     [45, 82, 180, 2],
#     [22, 58, 162, 5],
#     [38, 90, 0, 1],
#     [29, 65, 170, 0]
# ], dtype=float)

# # col0 = age, col1 = weight (kg), col2 = height (cm), col3 = number of sessions in a week
# member_names = np.array(["Ali","Sara","Reza","Neda","Hassan","Maryam"])

# print("Data shape:", gym_data.shape)
# print("Number of columns:", gym_data.shape[1])

# gym_data_col_numbers = gym_data.shape[1]
# print(gym_data_col_numbers)

# for col in range(1, gym_data_col_numbers):
#     number_of_nonzeros = np.count_nonzero(gym_data[:, col])
#     gym_data[:, col] = np.where(
#     gym_data[:, col] == 0,
#     np.sum(gym_data[:, col]) / number_of_nonzeros,
#     gym_data[:, col]
#     )

# print(gym_data)

# print ("*" * 50)
# new_gym_data = gym_data[:, 1:]
# print (new_gym_data)
# print ("*" * 50)

# weight, height, num_sessions = new_gym_data[:,0], new_gym_data[:,1], new_gym_data[:,2] 
# coef1 = 1
# coef2 = 2
# physical_readiness_score = ((weight / ((height / 100) ** 2)) * coef1) + (num_sessions * coef2)
# physical_readiness_score = physical_readiness_score.reshape(6, 1)
# new_gym_data = np.concatenate((new_gym_data, physical_readiness_score), axis = 1)
# print(new_gym_data)
# best_index = np.argmax(new_gym_data[:, 3])
# print (f"the best performance is for {member_names[best_index]} with score of {new_gym_data[:,3][best_index]}")
# print ("*" * 50)
# num_sessions_new = new_gym_data[:, 2]
# mean = np.mean(num_sessions_new)
# deviation = np.abs(num_sessions_new - np.mean(num_sessions_new))
# max_distance = np.max(deviation)

# print("Member(s) with maximum deviation:")
# for i in range(len(num_sessions_new)):
#     if deviation[i] == max_distance:
#         print(member_names[i], "->", "with", "->", deviation[i], "has the most deviation")

print("-" * 70)
# exercise 2
# recipes = np.array([
#     [15, 350, 2, 5],
#     [45, 600, 7, 10],
#     [10, 200, 0, 3],
#     [30, 450, 5, 7],
#     [60, 800, 8, 12]
# ], dtype = float)

recipe_names = ["Salad", "Curry", "Toast", "Pasta", "Stew"]
# c0 = cook time, c1 = colorie, c2 = spiciness, c3 = ingridients number

# max_recepies = (np.max(recipes, axis = 0)).reshape(1,4)
# min_recepies = (np.min(recipes, axis = 0)).reshape(1,4)
# print(max_recepies)
# print(min_recepies)
# normalized_recepies = (recipes - min_recepies) / (max_recepies - min_recepies)
# print(normalized_recepies)

# users = np.array([
#     [10, 250, 1, 4],
#     [50, 700, 8, 11],
#     [25, 400, 4, 6]
# ], dtype = float)
# print("=" * 60)
# normalized_users =  (users - min_recepies) / (max_recepies - min_recepies)
# print(normalized_users)

# distances = np.linalg.norm(normalized_users[:,None, :] - normalized_recepies[None, :, :], axis = 2)
# print(distances.shape)
# print(distances)

# user_preference = np.argmin(distances, axis=1)

# for i in range(len(user_preference)):
#     print(f"User {i + 1} probably enjoys mostly: {recipe_names[user_preference[i]]}")

# recipe_names = np.array(recipe_names)
# print(recipe_names[user_preference])

# sorted_indecies = np.argsort(distances, axis = 1)
# sorted_preferences = recipe_names[sorted_indecies]
# print(sorted_preferences)

# exercise 3
# col0 = quiz, col1 = midterm , col2 = final
scores = np.array([
    [18, 15, 20],
    [12, 14, 16],
    [20, 19, 18],
    [10,  8, 15]
])
# 3 ways of weighting
scheme_A = np.array([0.5, 0.3, 0.2])
scheme_B = np.array([0.2, 0.3, 0.5])
scheme_C = np.array([0.1, 0.2, 0.7])

weights = np.concatenate((scheme_A, scheme_B, scheme_C), axis = 0).reshape(3, 3)
print(weights, weights.shape)
final_score = scores @ weights.T
print (final_score)
print(final_score.shape)

methods = np.array(["A", "B", "C"])
max_scoring_method = np.argmax(final_score, axis = 1)
print(f"the method of weighting for each student is equal to {methods[max_scoring_method]} respectively")

manager_method = methods[np.argmax(np.mean(final_score, axis = 0))]
print(f"manager method of weighting that can max students score is {manager_method}")
# q + m + 2q = 1 >>> 3q + m = 1 >>> assue --> q = 0.225, m = 0.325 , f = 0.45
new_weight = np.array([0.225, 0.325, 0.45]).reshape(1, 3)
weights = np.concatenate((weights, new_weight), axis = 0)
print(f"new weight matrix is {weights} and its shape is {weights.shape}")
