import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
from dotenv import load_dotenv
import chainlit as cl

#------------------------

load_dotenv()
OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")

set_tracing_disabled(disabled=True)

history = []
#---------------------------

models = {
    "DeepSeek": "deepseek/deepseek-r1:free",
    "Gemini-2-flash-exp": "google/gemini-2.0-flash-exp:free",
    "Mistral": "mistralai/devstral-small:free",
    "Qwen": "qwen/qwen3-14b:free",
    "Meta-Llama": "meta-llama/llama-4-maverick:free"
}

#---------------------------------------------

@cl.on_chat_start
async def start_message():
    await cl.Message(content="Hello! How are you? 🙋‍♀️").send()
    
    settings = await cl.ChatSettings(
        [
            cl.input_widget.Select(
                id="Model",
                label="Choose Any LLM Model",
                values=list(models.keys()),
                initial_index=0
            )
        ]
    ).send()
    await setup_chat(settings)
#------------------------------

@cl.on_settings_update
async def setup_chat(settings):
    model_name = settings["Model"]

    cl.user_session.set("My Model", models[model_name])

    await cl.Message(content=f"You have selected {model_name} AI model. 🤖").send()


#----------------------------------    
@cl.on_message
async def my_message(msg: cl.Message):
    user_input = msg.content 
    history.append({"role": "user", "content": user_input})

    selected_model = cl.user_session.get("My Model")

    client = AsyncOpenAI(
        api_key=OPEN_ROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1"
    )

    agent = Agent(
        name="MyAgent",
        instructions="You are a helpful assistant.",
        model=OpenAIChatCompletionsModel(model=selected_model, openai_client=client)
    )

#----------------------------
    result = Runner.run_sync(agent, history)
    await cl.Message(content=result.final_output).send()