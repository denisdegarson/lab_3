import mypackage.module1 as md1

text = "Hello world"
dest = 'uk'
lang = 'en'
#print
print(md1.TransLate(text=text, dest=dest))
print(md1.LangDetect(text=text, set='all'))
print(md1.CodeLang(lang=lang))
md1.LanguageList(out='screen', text=text)
