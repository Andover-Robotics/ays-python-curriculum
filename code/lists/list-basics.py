activities = ['eat', 'code', 'sleep']
print(activities[len(activities) - 1])

elem = activities.pop(-1)
activities.insert(0, elem)

print(activities)

