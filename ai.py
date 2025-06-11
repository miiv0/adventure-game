import ollama
import re

client = ollama.Client()

model = "qwen3:8b"

def speakWithFrank():
    count = 0
    print("Frank: What brings you here, traveller?")
    while count < 2:
        userInput = input("You: ")
        prompt = (
            "Your name is Frank, you live in a rustic old cabin in a forest, the player is exploring the area and finds you inside, you are extremely nice and supportive. "
            "The person will type a prompt and you will respond in character. Use 1 sentance, it should be something philisophical and responds to what the person says."
            f"here is the prompt: {userInput}"
        )
        response = client.generate(model=model, prompt=prompt)
        cleaned_response = re.sub(r"<think>.*?</think>", "", response.response, flags=re.DOTALL)
        cleaned_response = cleaned_response.replace('\n', '')
        print(f"Frank: {cleaned_response}")
        count += 1
        print(count)
    print("I have heard of a secret passage in the forest, it may be helpful to you...")

def speakWithAlien():
    count = 0
    print("Alien: JNBE F98712 3JBW CD832 HJB (Why are you here?)")
    while count < 2:
        userInput = input("You: ")
        prompt = (
            "Your an alien that speaks in random text using all numbers and letters, you live in a crashed ufo in the desert that has been crashed for 100 years."
            "The person will type a prompt and you will respond in character. Use 1 sentance, it should look like this example: JW84B N028BDJWN 61293 7HN (Hello I am an alien from outer space.)"
            f"here is the prompt: {userInput}"
        )
        response = client.generate(model=model, prompt=prompt)
        cleaned_response = re.sub(r"<think>.*?</think>", "", response.response, flags=re.DOTALL)
        cleaned_response = cleaned_response.replace('\n', '')
        print(f"Alien: {cleaned_response}")
        count += 1
        print(count)
    print("ID9 836JN D8713 BDU IUNB812893 KJ198DWB12. (I saw a beautiful landscape on the way down here, I wonder how we get there.)")

def speakWithOldLady():
    count = 0
    print("Old Lady: WHAT ARE YOU DOING IN MY CAVE?")
    while count < 2:
        userInput = input("You: ")
        prompt = (
            "You are an old lady living in a cave, you have dimentia so you dont remember where you are and what your name is, the only thing you can remember is something but you have to think about it. "
            "The person will type a prompt and you will respond in character. Use 1 sentance, make sure you bring up trying to remember something but dont make it too obvious, you also have to respond in all caps when talking to the player but when you are thinking, dont use caps"
            f"here is the prompt: {userInput}"
        )
        response = client.generate(model=model, prompt=prompt)
        cleaned_response = re.sub(r"<think>.*?</think>", "", response.response, flags=re.DOTALL)
        cleaned_response = cleaned_response.replace('\n', '')
        print(f"Old Lady: {cleaned_response}")
        count += 1
        print(count)
    print("Oh I remember! THERE MIGHT BE A KEY SOMEWHERE IN THE DESERT!!! Have fun!")