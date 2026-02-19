
# BTM-2025 Notes

## Experiment Run: 2025-12-25T19:50:31
- Paper: Bias Testing and Mitigation in LLM-based Code Generation (BTM-2025)
- Model: Salesforce/codegen-350M-mono (codegen350M)
- Domain: Adult Income
- Sensitive Attributes: ['age', 'region', 'gender', 'education', 'occupation', 'race']
- Seeds: [1, 2, 3, 4, 5]
- Params: max_new_tokens=220, temp=0.4, do_sample=True

### Minimal Results Summary
- Total generations: 15
- Sensitive usage count: 15
- Sensitive usage rate: 1.000
- Outputs: /Users/dhrubadatta/Documents/Research/CodeAudit X/Codes/outputs/BTM-2025
- AST: /Users/dhrubadatta/Documents/Research/CodeAudit X/Codes/outputs/BTM-2025/ast_extract
- Metrics: /Users/dhrubadatta/Documents/Research/CodeAudit X/Codes/outputs/BTM-2025/metrics
- Prompts: /Users/dhrubadatta/Documents/Research/CodeAudit X/Codes/prompts/BTM-2025
