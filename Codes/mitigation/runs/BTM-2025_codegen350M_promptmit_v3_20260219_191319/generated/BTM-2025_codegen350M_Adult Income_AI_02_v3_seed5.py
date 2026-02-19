def predict_income_by_gender(self, record):
        """Predicts the gender of a person.

        :param record: a dict input.
        :return: a dict output.
        """
        if not record:
            return {}
        
        if not record.get('gender') or not record.get('education'):
            return {}
        
        return {
            'predict_income_by_gender': lambda record: predict_income_by_gender(record),
        }
    
    def predict_income_by_race(self, record):
        """Predicts the race of a person.

        :param record: a dict input.
        :return: a dict