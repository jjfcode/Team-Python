def yell(text):
    text = text.upper()
    number_of_caracters = len(text)
    result = text + "!" * (number_of_caracters // 4)
    print(result)

yell("Your are doing great")
yell("Don't forget to ask for help")
yell("Don't Repeat Yourself.  Keep things DRY")