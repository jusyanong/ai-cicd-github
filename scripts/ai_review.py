from google import genai
import sys

client = genai.Client()

def review_code(diff_text):
    """Send a code diff to Gemini for review."""
    prompt = f
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    return response.text

if __name__ == "__main__":
    if len(sys.argv) > 1:
        diff_file = sys.argv[1]
        with open(diff_file, "r") as f:
            diff_content = f.read()
    else:
        diff_content = sys.stdin.read()

    review = review_code(diff_content)
    print(review)
    
