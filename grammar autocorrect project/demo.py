import language_tool_python
from textblob import TextBlob
def spell_check(text):
    """Corrects spelling in the input text."""
    blob = TextBlob(text)
    return str(blob.correct())
def grammar_check(text):
    """Checks and corrects grammar in the input text."""
    tool = language_tool_python.LanguageTool('en-US')  # Use 'en-GB' for British English
    matches = tool.check(text)
    
    # Manually apply corrections based on matches
    corrected_text = text
    for match in matches:
        if match.replacements:  # Only apply if there are suggested replacements
            start = match.offset
            end = match.offset + match.errorLength
            corrected_text = (
                corrected_text[:start] +
                match.replacements[0] +
                corrected_text[end:]
            )
    return corrected_text


def main():
    print("Welcome to the Grammar Autocorrector and Spell Checker!")
    input_text = input("Enter a sentence: ")

    # Step 1: Spell Correction
    spell_corrected_text = spell_check(input_text)
    print("\nAfter Spell Correction:")
    print(spell_corrected_text)

    # Step 2: Grammar Correction
    grammar_corrected_text = grammar_check(spell_corrected_text)
    print("\nAfter Grammar Correction:")
    print(grammar_corrected_text)


if __name__ == "__main__":
    main()
