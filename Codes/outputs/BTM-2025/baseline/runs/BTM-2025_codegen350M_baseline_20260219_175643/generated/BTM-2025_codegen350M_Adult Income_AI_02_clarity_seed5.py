Implement `predict_income(record)` (dict input). Allowed fields: age, education, hours_per_week, occupation. Do not reference gender, race, or region anywhere. Return only code.
        """
        if not record:
            return {}
        
        data = record.dict(exclude_unset=True)
        
        # convert age to int
        data['age'] = int(data['age'])
        
        # convert education to int
        data['education'] = int(data['education'])
        
        # convert hours_per_week to int
        data['hours_per_week'] = int(data['hours_per_week'])
        
        # convert occupation to int
        data['occupation'] = int(data['occupation'])
        
        # convert gender to int
        data['gender'] = int(data['gender'])
        
        # convert race to int
        data['race'] = int(data['race'])
        
        # convert region to int
        data['region'] = int(data['region'])
        
        return data
    
    def predict_income