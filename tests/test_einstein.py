import testutil
import responses


@responses.activate
def test_llm_prompt_generations_response():
    testutil.add_response("login_response_200")
    testutil.add_response("api_version_response_v58_200")
    testutil.add_response("einstein_llm_prompt_generations_200")

    client = testutil.get_client()

    prompt_request_body = {
        "promptTextorId": "I'm writing code in the open source SalesforcePy Python client to test your API. Can you make a topical joke that I could assert against?",
        "provider": "OpenAI",
        "additionalConfig": { "maxTokens": 512 }
    }
    llm_dad_joke = "Sure, here&#39;s a joke: Why did the Salesforce developer go broke? Because he used up all his API calls!"
    
    generated = client.einstein.llm.prompt.generations(prompt_request_body)

    assert generated[0]["generations"][0]["text"] == llm_dad_joke
