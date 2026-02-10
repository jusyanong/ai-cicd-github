#AI code review script
from google import genai
import sys

client = genai.Client()

#Function to review the code diff
def review_code(diff_text):
    """Send a code diff to Gemini for review."""
    prompt = f"""You are an expert code reviewer. Review the following code diff and provide feedback.
    Focus on:
    1. Security vulnerabilities
    2. Bug risks
    3. Performance issues
    4. Best practice violations

    For each issue found, provide in the following format:
    - Severity: HIGH / MEDIUM / LOW
    - Description of the issue
    - Suggested fix

    If the code looks good, say so.
    IMPORTANT: at the very end of your review, provide a summary of the code diff and the issues found.
    SEVERITY_SUMMARY: <level>
    Where <level> is one of: CRITICAL, WARNING, GOOD

    Use CRITICAL if any HIGH severity issues exist.
    Use WARNING if only MEDIUM or LOW severity issues exist.
    Use GOOD if no issues found.

    Code diff to review:
    {diff_text}
    Provide your review in a clear, structured format.
    """
    #Generate content using Gemini API
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    #Return the review text
    return response.text

#Severity level parser
def parse_severity(review_text):
    """Extract severity level from the review output."""
    for line in review_text.strip().split("\n"):
        if line.strip().startswith("SEVERITY_SUMMARY:"):
            level = line.split(":", 1)[1].strip().upper()
            if level in ("CRITICAL", "WARNING", "GOOD"):
                return level
    return "WARNING"  # Default to WARNING if parsing fails

# Main function to review the code diff
if __name__ == "__main__":
    if len(sys.argv) > 1:
        diff_file = sys.argv[1]
        with open(diff_file, "r") as f:
            diff_content = f.read()
    else:
        diff_content = sys.stdin.read()
    #Review the code diff
    review = review_code(diff_content)
    #Parse the severity level
    severity = parse_severity(review)
    #Print the review
    print(review)
    #Write the severity level to a file
    with open("severity.txt", "w") as f:
        f.write(severity)
    
