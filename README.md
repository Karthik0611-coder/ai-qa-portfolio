# 🤖 AI-Integrated Quality Engineering Portfolio (`ai-qa-portfolio`)

An enterprise-grade test automation framework that integrates **Playwright**, **Pydantic**, and **Gemini API (Flash 3.8)** to automate failure triage, capture visual context, and generate executive markdown dashboards in real-time.

![AI QA Pipeline](https://github.com/YOUR_USERNAME/ai-qa-portfolio/actions/workflows/ai_qa_pipeline.yml/badge.svg)

---

## 🚀 Key Features

- **Automated Failure Hooks:** Uses `conftest.py` lifecycle hooks to intercept test failures, capture screenshots, and harvest Aria snapshots instantly.
- **Multimodal AI Triage:** Sends failure logs and UI screenshots to Gemini Vision to diagnose root causes automatically.
- **Strict Schema Validation:** Enforces data integrity using **Pydantic v2**, ensuring all AI-generated bug reports conform to a strict enterprise schema.
- **Resilient Network Handling:** Features built-in automatic retries, fallback strategies, and **Offline Fallback Mode** ensuring CI/CD pipelines never fail due to transient network spikes.
- **Historical Audit Logs:** Automatically archives immutable, timestamped JSON reports in a `/reports` directory.
- **Executive Dashboard Generation (`qa_summary.md`):** Compiles live summaries of severity levels, affected modules, and recommended engineering actions.
- **Cloud CI/CD Integration:** Automated execution via **GitHub Actions** with artifact uploads for audit logs.

---

## 🛠️ Tech Stack

- **Language:** Python 3.11+
- **Test Runner:** Pytest
- **Browser Automation:** Playwright (Chromium)
- **Data Validation:** Pydantic
- **AI Model:** Google Gemini API (`gemini-3.8-flash`)
- **CI/CD:** GitHub Actions

---

## 📂 Project Architecture

```text
ai-qa-portfolio/
│
├── .github/workflows/       # GitHub Actions CI/CD workflow
├── reports/                 # Immutable timestamped JSON bug reports
├── conftest.py              # Pytest lifecycle hooks for failure capture
├── ai_reporter.py           # Pydantic models & Gemini vision triage engine
├── test_login.py            # Automated test suite (Playwright + SauceDemo)
├── requirements.txt         # Project dependencies
├── qa_summary.md            # Live executive markdown dashboard
└── latest_bug_report.json   # Quick-access pointer for latest failure