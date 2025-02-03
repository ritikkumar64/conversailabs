from scraper import scrape_website
from database import store_content
from chatbot import setup_chatbot, generate_response

def main():
    url = input("https://www.conversailabs.com/")
    print("Scraping website...")
    scraped_text = scrape_website(url)
    if not scraped_text:
        print("Failed to scrape the website. Please check the URL and try again.")
        return

    print("Storing content...")
    vector_store = store_content(scraped_text)

    print("Setting up chatbot...")
    chatbot = setup_chatbot(vector_store)

    print("Chatbot is ready! Type 'exit' to quit.")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        response = generate_response(chatbot, query)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()