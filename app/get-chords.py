import openai
import pretty_midi

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = 'YOUR_API_KEY'

# Initialize the OpenAI API client
openai.api_key = api_key

def ask_gpt(question):
    # Define the ChatGPT model
    model = "gpt-3.5-turbo"

    # Generate a response using ChatGPT
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ],
    )

    # Extract and print the assistant's reply
    assistant_reply = response['choices'][0]['message']['content']
    print("Assistant: ", assistant_reply)

    # Convert the assistant's reply to MIDI notes
    midi_notes = text_to_midi(assistant_reply)

    return midi_notes

def text_to_midi(text):
    # Replace this with your own logic to convert text to MIDI notes
    # For simplicity, we'll assume C4 (middle C) for all notes and a fixed duration
    notes = [60] * len(text)  # C4 note number
    durations = [0.5] * len(text)  # 0.5 seconds duration for each note

    # Create a PrettyMIDI object
    midi = pretty_midi.PrettyMIDI()
    piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
    piano = pretty_midi.Instrument(program=piano_program)

    # Add the notes to the instrument
    # Add the instrument to the MIDI file
    midi.instruments.append(piano)

    # Save the MIDI file
    midi.write('output.tidal')

    return midi

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        midi_notes = ask_gpt(user_input)
