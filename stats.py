def number_of_words(text):
    return len(text.split())
def number_of_chars(text):
    result = []
    for char in text:
        char = char.lower()
        if not {"char":char,"num":0} in result:
            result.append({"char":char,"num":0})
    for char in text:
        for i in range(0,len(result)):
            if result[i]["char"] == char:
                result[i]["num"] += 1
                break
            
    return result
def sort_on(items):
    return items["num"]
def sort_dict(dict):
    dict.sort(reverse=True,key=sort_on)
    return dict