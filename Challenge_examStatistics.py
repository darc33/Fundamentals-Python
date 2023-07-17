#CHALLENGE EXAM STATISTICS (computes sum, average, variance and standard deviation)
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
    print ("The grades are:")
    for grade in grades_input:
        print (grade)

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  
  for score in scores:
    variance += (average - score) ** 2
  
  return variance / float(len(scores))

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)

print_grades(grades)
print ("\nThe sum of the grades is:", grades_sum(grades))
print ("\nThe average of the grades is:", grades_average(grades))
print ("\nThe variance of the grades is:", variance)
print ("\nThe std deviation of the grades is:", grades_std_deviation(variance))