def f(text):
    result = ""
    last_letter = (len(text))-2
    if len(text)==0 or len(text)==1:
        return text
    else:
        for i in text[]:
          if i !=text[last_letter]:
           result = result + i + '-'
          if i == text[last_letter]:
           result = result + i
    return result


print(f('sdgd'))