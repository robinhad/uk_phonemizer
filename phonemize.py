with open("rules.txt") as rules_file:
    rules = rules_file.read()
rules = rules.split("\n[Rules]\n\n")[1]
rules = rules.split("\n")
rules = [rule.split(" --> ") for rule in rules]
for i in range(0, len(rules)):
    rules[i][0] = rules[i][0].strip().lower()

for i in range(0, rules.count([""])):
    rules.remove([""])
rules, len(rules)

rules_dict = {}
for rule in rules:
    if rules_dict.get(rule[0]) is not None:
        try:
            assert rules_dict[rule[0]] == rule[1]
        except AssertionError:
            print(rule[0], rules_dict[rule[0]], rule[1])
            raise
    rules_dict[rule[0]] = rule[1]

del rules

def phonemize(text, mode="ipa"):
    text = text.lower()
    for rule in sorted(rules_dict.keys(), key=len, reverse=True):
        text = text.replace(rule, rules_dict[rule])
    text = text.replace("'", "")
    return text


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        sys.argv.pop(0)
        text = " ".join(sys.argv)
    else:
        text = "Привіт, як у тебе справи? м'яко падаєм, мякий"
    print(phonemize(text))