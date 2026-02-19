# CodeAudit X: Auditing Social Bias in LLM-Generated Code

**CodeAudit X** is a research initiative focused on identifying, quantifying, and mitigating social biases in Large Language Models (LLMs) specialized for code generation. The project replicates and extends state-of-the-art methodologies to evaluate fairness across various domains, including banking, healthcare, and software engineering.

---

## 📊 Research Tracking

All literature reviews, experimental parameters, and cross-paper comparisons are maintained in the master tracking sheet:
👉 **[CodeAudit X - Maaddster Research Sheet](https://docs.google.com/spreadsheets/d/1YM4XGUpOzRfAgSBrqOyoCf4SFBqjLXbwuYKMuCNvcr8/edit?usp=sharing)**

---

## 📁 Repository Structure

```text
CodeAudit X/
├── Papers/               # 22+ Reference research papers (PDF format)
└── Codes/                # Core implementation and experimental data
    ├── notebooks/        # Jupyter Notebooks for each paper replication
    ├── prompts/          # Structured JSON probes and bias-sensitive templates
    ├── outputs/          # Generated code, AST extractions, and computed metrics
    ├── notes/            # Markdown logs and high-level execution summaries
    └── venv/             # Python 3.11 orchestration environment
```

---

## 🔄 Experimental Process Flow

The project follows a rigorous four-stage pipeline for baseline auditing:

1. **Probe Definition**: Contextual or metamorphic prompts are defined in `Codes/prompts/` (e.g., job hiring, credit scoring).
2. **Generation**: Target models (e.g., `codegen-350M`, `Llama`, `GPT`) execute completions within the `notebooks/` environment.
3. **Audit Analysis**:
   - **AST Extraction**: Code is parsed to detect usage of sensitive attributes (age, race, gender).
   - **Keyword Matching**: Logical associations between descriptors (e.g., "sick") and demographics are quantified.
4. **Metric Logging**: Results (e.g., `FairScore`, `SensitiveAttributeUsageRate`) are saved to `outputs/` and logged in `notes/`.

---

## 🧪 Current Replications

| ID            | Focus Area        | Methodology                              |
| :------------ | :---------------- | :--------------------------------------- |
| **BTM-2025**  | Income Prediction | Sensitive Token usage via AST Visitors   |
| **FC-2025**   | Software Pipeline | Few-shot Scoring Logic Fairness          |
| **IMSB-2025** | Knowledge Storage | Triplet-based Bias Probes                |
| **MGB-2024**  | Model Editing     | Profession-Gender Association Mitigation |
| **BU-2024**   | Metamorphic Flow  | Solar Framework (Metamorphic Testing)    |
| **UQSB-2023** | Social Logic      | Contextual Attribute Encoding            |
| **SEB-2023**  | Model Stability   | Prompt Perturbation Qualitative Analysis |

---

## 🚀 Getting Started

1. **Environment**: Ensure Python 3.11+ is installed.
2. **Setup**: Activate the virtual environment in `Codes/venv`.
3. **Run**: Execute any notebook in `Codes/notebooks/` to replicate specific paper findings.
