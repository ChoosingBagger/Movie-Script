def properName(fieldName):
    try:
        fieldName = fieldName.lower()
        return fieldName
    except:
        return fieldName


def urlTransform(character, url):
    temp = url.split()
    newURL = character.join(temp)
    return newURL