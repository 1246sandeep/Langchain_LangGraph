from dotenv import load_dotenv
import os

load_dotenv()

def main() -> None:
    print("Hello from langchain-course-main!")
    print(os.environ.get("OPENAI_API_KEY"))
     
if __name__ == "__main__":
    main()
