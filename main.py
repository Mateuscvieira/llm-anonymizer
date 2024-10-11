import os

import click
import openai

import personas


def generate_system_prompt(persona: personas.Persona) -> str:
    assert isinstance(persona, dict)
    initial_prompt = "I want you to rewrite the text that I sent you, in the same format and language as shown, but in the following persona:\n"
    persona_prompt = f"""
        Age: {persona["age"]!s}
        Nationality: {persona["nationality"]}
        Gender: {persona["gender"]}
    """
    addendum = "\nDepending on age and nationality, you should add common foreign language mistakes, but you should always keep the whole sentence in the same language as the input."
    return initial_prompt + persona_prompt + addendum


@click.command("input")
@click.version_option("0.1.0", prog_name="hello")
@click.argument("user_text")
def main(user_text: str):
    assert isinstance(OPENAI_KEY, str)

    client = openai.OpenAI(api_key=OPENAI_KEY)
    persona = personas.get_persona()
    system_prompt = generate_system_prompt(persona)

    # FIXME: this for some reason keeps changing the language, especially for italian and german.
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": user_text,
            },
            {
                "role": "system",
                "content": "Rewrite the text, modifying specific information there that the persona shouldn't have, such as regional slang, while keeping it in the same language still.",
            },
        ],
    )

    click.echo(completion.choices[0].message.content)


def get_openai_key() -> str:
    return input("Please enter your OpenAI key")


if __name__ == "__main__":
    global OPENAI_KEY

    OPENAI_KEY = os.environ.get("OPENAI_KEY")
    if OPENAI_KEY is None:
        OPENAI_KEY = get_openai_key()
    main()
