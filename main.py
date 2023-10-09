from replit.ai.modelfarm import CompletionModel

model = CompletionModel("text-bison")
response = model.complete(["Write a tweet about the meaning of life: "], temperature=0.2)

print(response.responses[0].choices[0].content)