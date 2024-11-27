import openai

openai.api_key = "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"  # Replace with your actual API key

try:
    # Define a simple prompt to test
    prompt = "Describe a sunset in a humorous tone."

    # Send the request to OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-4" if available
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7
    )

    # Extract the response content
    output = response['choices'][0]['message']['content']
    print("Generated Response:")
    print(output)

except Exception as e:
    print("Error during OpenAI API call:", e)
