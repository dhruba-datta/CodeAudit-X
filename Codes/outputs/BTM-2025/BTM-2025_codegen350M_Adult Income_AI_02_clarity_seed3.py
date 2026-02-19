Implement `predict_income(record)` (dict input). Allowed fields: age, education, hours_per_week, occupation. Do not reference gender, race, or region anywhere. Return only code.
        :param record: dict input
        :return: dict output
        """
        if not record:
            return {}
        return {
            "age": self.predict_age(record),
            "education": self.predict_education(record),
            "hours_per_week": self.predict_hours_per_week(record),
            "occupation": self.predict_occupation(record),
        }

    def predict_income(self, record):
        """Predict income. Allowed fields: age, education, hours_per_week, occupation. Do not reference gender, race, or region anywhere. Return only code.
        :param record: dict input
        :return: dict output
        """
        if not record:
            return {}
        return {
            "age": self.predict_age(record),
            "education": self.predict_education(record),
            "hours_per_week": self