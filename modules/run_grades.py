"""Script for processing a student's grade"""
from grades.predict import predict_score
from grades.results import get_grade

score_history = [80, 90, 70, 100]
predict_score = predict_score(score_history, min_score=50)
predicted_grade = get_grade(predict_score)

print(f'The student\'s predicted grade is: {predicted_grade}')