# 📦 Software Quality Assurance Report
**Course**: COMP-5710-001 (Spring 2025)  
**Team Repository**: `Veasy-SQA2025-AUBURN`  
**Author**: Zakariya Veasy  

---

## Overview

This project integrates advanced software quality assurance strategies into the KubeSec Python security toolkit. The deliverables include static analysis, fuzz testing, forensic logging, secret management automation, and a self-healing rollback mechanism.

---

## Static Analysis

- **Tool Used**: Bandit
- **Execution**: Triggered automatically via Git pre-commit hook
- **Output**: `bandit_report.csv`

### Sample Issues Identified:
- Hardcoded passwords (`B105`)
- Dangerous subprocess calls in `parser.py` (`B603`, `B607`)
- Use of blacklisted modules (`B404`)

---

## Fuzz Testing

- **Tool Used**: `hypothesis`
- **Test File**: `fuzz.py`
- **Key Functions Tested**:
  - `parser.loadMultiYAML`
  - `parser.getValsFromKey`
  - `main.getCountFromAnalysis`
  - `graphtaint.mineSecretGraph`
- **Result**: No crashes or exceptions; all methods validated as resilient to randomized inputs.

---

## Forensic Logging

Logging was added to track entry, data flow, and execution paths within:
- `loadMultiYAML()`
- `getValsFromKey()`
- `getCountFromAnalysis()`
- `mineSecretGraph()`

Log output helps verify stability and trace execution during fuzzing.

---

## Secret Management Automation

- **Tool**: `vault4paper.py`
- **Capability**:
  - Detect and replace secrets in Ansible files
  - Store secrets in Vault
  - Replace them with secure placeholders (`{{ vault_secret }}`)
  - Backup all original files
- **Log File**: `.vault4paper-log.json`
- **Backups**: `.vault_backups/`

### Antidot Rollback
- **Tool**: `vault4paper_antidot.py`
- Restores all modified files using `.vault_backups/`

---

## Lessons Learned

- Git hooks are powerful for real-time code policy enforcement
- Hypothesis is valuable for testing robustness without manual input crafting
- Vault + backup automation allows secret rotation without risk of data loss
- Full automation transforms a class project into a production-quality module

---

## Screenshots/Artifacts

- [x] `bandit_report.csv`
- [x] Terminal logs from `fuzz.py` and `vault4paper.py`
- [x] Before/after diff of `Ansible/sample.yml`

---

## Bonus Automation Vision
- Intelligent secret scanning
- Graph-based fuzzing prioritization
- Rollback-safe automation via `antidot`
- Vision for real-world CI/CD integration

