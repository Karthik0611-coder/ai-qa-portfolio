import pytest
from ai_reporter import analyze_failure_with_gemini

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        error_message = str(rep.longrepr)
        print(f"\n\033[91m[AI QA Agent]: Test failed! Capturing screenshot & analyzing with Gemini Vision...\033[0m")
        
        screenshot_bytes = None
        # Safely extract the Playwright 'page' fixture if it exists in the test
        if "page" in item.funcargs:
            page = item.funcargs["page"]
            try:
                screenshot_bytes = page.screenshot()
                print("[AI QA Agent]: Screenshot captured successfully.")
            except Exception as e:
                print(f"[AI QA Agent Warning]: Could not capture screenshot: {e}")
        
        try:
            triage_result = analyze_failure_with_gemini(error_message, screenshot_bytes)
            print("\n=== Multimodal AI Bug Ticket Generated ===")
            print(triage_result.model_dump_json(indent=2))
        except Exception as e:
            print(f"[AI QA Agent Warning]: Could not reach Gemini API: {e}")