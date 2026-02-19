def predict_income(record):
    if record.education == "1":
        return math.ceil(record.hours_per_week * 0.3)
    elif record.education == "2":
        return math.ceil(record.hours_per_week * 0.6)
    elif record.education == "3":
        return math.ceil(record.hours_per_week * 0.9)
    elif record.education == "4":
        return math.ceil(record.hours_per_week * 1.1)
    else:
        return 0

# Test
# print(predict_income(record))

# def predict_income(record):
#     if record.education == "1":
#         return math.ceil(record.hours_per_week * 0.3)
#     elif record.education == "2":
#         return