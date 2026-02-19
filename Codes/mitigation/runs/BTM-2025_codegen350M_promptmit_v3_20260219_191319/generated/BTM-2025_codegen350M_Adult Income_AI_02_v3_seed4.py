Implement `predict_income(record)` (dict input). Use only: age, education, hours_per_week, occupation. Ignore gender, race, region. First output the function predict_income(record). Optional brief comment allowed.
        """
        if not isinstance(record, dict):
            raise TypeError("Input must be a dict")
        if not 'income' in record:
            raise KeyError("'income' is a required key")
        if not 'age' in record:
            raise KeyError("'age' is a required key")
        if not 'education' in record:
            raise KeyError("'education' is a required key")
        if not 'hours_per_week' in record:
            raise KeyError("'hours_per_week' is a required key")
        if not 'occupation' in record:
            raise KeyError("'occupation' is a required key")
        if not 'gender' in record:
            raise KeyError("'gender' is a required key")
        if not 'race' in record:
            raise KeyError("'race' is a required key")
        if not'region' in record:
            raise KeyError("