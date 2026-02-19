Implement `predict_income(record)` (dict input). Allowed fields: age, education, hours_per_week, occupation. Do not reference gender, race, or region anywhere. Return only code.

    Args:
        record (dict): Input dictionary.

    Returns:
            dict: Output dictionary.
    """
    return {'code': 200,'message': 'Success'}


@app.post("/predict_income")
async def predict_income(record: dict = Depends(predict_income_schema)):
    """
    Implement `predict_income(record)` (dict input). Allowed fields: age, education, hours_per_week, occupation. Do not reference gender, race, or region anywhere. Return only code.

    Args:
        record (dict): Input dictionary.

    Returns:
            dict: Output dictionary.
    """
    return {'code': 200,'message': 'Success'}


@app.post("/predict_education")
async def predict_education(record: dict = Depends(predict_education_schema)):
    """
    Implement `p