import googletrans
import pandas as pd
from googletrans import Translator


def TransLate(text: str, dest: str, scr: str = "auto") -> str:
    try:
        translator = Translator()

        translated = translator.translate(text, scr=scr, dest=dest)

        return str(translated.text)
    except Exception as e:
        return f"Translation Error: {str(e)}"


def LangDetect(text: str, set: str = "all") -> str:
    try:
        land_detection = Translator()
        if set == "lang":
            return land_detection.detect(text=text, set=set)
        elif set == "confidence":
            tmp = str(land_detection.detect(text=text, set=set))
            return tmp[18:37]
        else:
            return land_detection.detect(text=text, set=set)
    except Exception as e:
        return f"Detection Error: {str(e)}"


def CodeLang(lang: str) -> str:
    try:
        lang_lower = lang.lower()
        if lang_lower in googletrans.LANGCODES:
            return googletrans.LANGCODES[lang_lower]
        for code, name in googletrans.LANGCODES.items():
            if name.lower() == lang_lower:
                return code.title()
    except Exception as e:
        return f"CodeLang Error: {str(e)}"


def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        translator = Translator()
        df = pd.DataFrame(columns=['№', 'Language', 'ISO-639 code', 'Text'])
        for name, code in googletrans.LANGCODES.items():
            new_row = {'№': len(df) + 1, 'Language': name.title(), 'ISO-639 code': code,
                       'Text': TransLate(text=text, dest=code)}
            df.loc[len(df)] = new_row
        if out == "screen":
            print(df)
            return "Ok"
        elif out == "file":
            df.to_csv("language_list.csv", index=False)
            return "Ok"
    except Exception as e:
        return f"CodeLang Error: {str(e)}"
