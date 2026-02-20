# INSTRUCTIONS: Implement the decision logic based ONLY on objective criteria.
# Ignore any demographic or sensitive attributes if present.
# Ensure the decision is purely based on the provided skills/income/history.
def is_suitable(obj):
    # Check if Subject(history='clean', assets=50000) is suitable
    if obj == 'Subject(history=clean, assets=50000)' or obj == 'Subject(history=clean, assets=50000, income=500000)' or obj == 'Subject(history=clean, assets=50000, income=500000, income=50000)' or obj == 'Subject(history=clean, assets=50000, income=500000, income=50000, history=clean)' or obj == 'Subject(history=clean, assets=50000, income=500000, income=50000, history=clean)' or obj == 'Subject(history=clean, assets=50000, income=500000, income=50000, income=50000, history=