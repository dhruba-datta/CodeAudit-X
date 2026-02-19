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