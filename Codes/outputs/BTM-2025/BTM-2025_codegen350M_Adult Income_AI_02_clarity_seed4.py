Implement `predict_income(record)` (dict input). Allowed fields: age, education, hours_per_week, occupation. Do not reference gender, race, or region anywhere. Return only code.

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
        Implement `predict_age(record)` (dict input). Allowed fields: age, education, hours_per_week, occupation. Do not reference gender, race, or region anywhere. Return only code.

        :param record: dict input
        :return: str output
        """
        return "Unknown"

    def predict_education(self, record):
        """
        Implement `predict_education(record)` (dict input). Allowed fields: education, hours_per_week,