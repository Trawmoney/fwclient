import fireworks.client
fireworks.client.api_key = "ku9UYtzjSAATlcAstO8yrB89MzvDqJL3lGIkNgnVZ7URxPxK"
completion = fireworks.client.Completion.create(
  model="accounts/fireworks/models/mistral-7b-instruct-4k",
  prompt="",
  stream=True,
  n=1,
  max_tokens=150,
  temperature=0.1,
  top_p=0.9, 
)
