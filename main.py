from workflows.review_workflow import create_review_workflow


def main():

    code_input = input("Paste your code here (press Enter twice when done):\n")
    lines = [code_input]

    try:
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
    except EOFError:
        pass

    full_code = "\n".join(lines)

    if not full_code.strip():
        print("Error: No code provided")
        return

    print("\n" + "=" * 60)
    print("Initializing Code Review Agents...")
    print("=" * 60 + "\n")

    workflow = create_review_workflow()

    initial_state = {
        "code_content": full_code,
        "analyzer_result": {},
        "optimizer_result": {},
        "security_result": {},
        "documentation_result": {},
        "final_review": {},
    }

    print("Running Code Analysis Agent...")
    print("Running Optimization Agent...")
    print("Running Security Check Agent...")
    print("Running Documentation Agent...")
    print("Combining Results...\n")

    result = workflow.invoke(initial_state)

    print("=" * 60)
    print("FINAL CODE REVIEW REPORT")
    print("=" * 60 + "\n")

    print("CODE ANALYSIS (Bug Detection):")
    print("-" * 40)
    print(result["analyzer_result"]["content"])
    print("\n")

    print("OPTIMIZATION SUGGESTIONS:")
    print("-" * 40)
    print(result["optimizer_result"]["content"])
    print("\n")

    print("SECURITY ANALYSIS:")
    print("-" * 40)
    print(result["security_result"]["content"])
    print("\n")

    print("DOCUMENTATION REVIEW:")
    print("-" * 40)
    print(result["documentation_result"]["content"])
    print("\n")

    print("Summary ")
    print("-" * 40)
    print(result["documentation_result"]["content"])
    print("\n")

    print("=" * 60)
    print(result["final_review"]["content"])
    print("=" * 60)

    print("=" * 60)
    print("Review Complete")
    print("=" * 60)


if __name__ == "__main__":
    main()
