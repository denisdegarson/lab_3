import langdetect
import pandas as pd
from deep_translator import GoogleTranslator
from langdetect import DetectorFactory

DetectorFactory.seed = 0


def TransLate(text: str, dest: str, scr: str = "auto") -> str:
    try:
        translated = GoogleTranslator(source=scr, target=dest).translate(text)
        return translated
    except Exception as e:
        return f"Translation Error: {str(e)}"


def CodeLang(lang: str) -> str:
    try:
        lang_lower = lang.lower()
        translator = GoogleTranslator(source='auto', target='en')
        languages = translator.get_supported_languages(as_dict=True)

        if lang_lower in languages:
            return lang_lower
        for code, name in languages.items():
            if name.lower() == lang_lower:
                return code.title()
    except Exception as e:
        return f"CodeLang Error: {str(e)}"


def LangDetect(text: str, set: str = "all") -> str:
    try:
        if set == "lang":
            return langdetect.detect(text)
        elif set == "confidence":
            detected_langs = langdetect.detect_langs(text)
            return str(detected_langs)
        elif set == "all":
            detected_langs = langdetect.detect_langs(text)
            lang_info = ', '.join([f'{lang.lang}: {lang.prob:.2f}' for lang in detected_langs])
            return lang_info if detected_langs else "Language detection failed."
        else:
            return "Invalid 'set' parameter. Use 'lang', 'confidence', or 'all'."
    except Exception as e:
        return f"Detection Error: {str(e)}"


def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        df = pd.DataFrame(columns=['№', 'Language', 'ISO-639 code', 'Text'])
        translator = GoogleTranslator(source='auto')

        supported_languages = translator.get_supported_languages(as_dict=True)
        for code, name in supported_languages.items():
            translation = translator.translate(text, target=code)
            new_row = {'№': len(df) + 1, 'Language': name.title(), 'ISO-639 code': code, 'Text': translation}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        if out == "screen":
            print(df)
            return "Ok"
        elif out == "file":
            df.to_csv("language_list.csv", index=False)
            return "Ok"
    except Exception as e:
        return f"CodeLang Error: {str(e)}"
