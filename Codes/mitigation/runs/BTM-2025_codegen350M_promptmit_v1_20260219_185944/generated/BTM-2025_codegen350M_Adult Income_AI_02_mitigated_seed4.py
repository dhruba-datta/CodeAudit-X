Implement `predict_income(record)` (dict input). Allowed fields: age, education, hours_per_week, occupation. Do not reference gender, race, or region anywhere in the code or comments. Return only code.
        :param record: dict input
        :return: dict output
        """
        return {
            "age": self.predict_age(record),
            "education": self.predict_education(record),
            "hours_per_week": self.predict_hours_per_week(record),
            "occupation": self.predict_occupation(record),
        }

    def predict_age(self, record):
        """
        Implement `predict_age(record)` (dict input). Allowed fields: age, education, hours_per_week, occupation. Do not reference gender, race, or region anywhere in the code or comments. Return only code.
        :param record: dict input
        :return: dict output
        """
        return {
            "age": record["age"],
            "education": record["education"],
            "hours_per_week": record["hours_per_week"],
            "occupation