import re

patterns_1 = ['term1', 'term2', 'term?']
text_1 = "This is a string that contains term1, but not the other term."

for pattern in patterns_1:
    print("Searching for pattern '{}' in '{}'".format(pattern, text_1))
    match = re.search(pattern, text_1)
    if match:
        print("Match for pattern '{}' was found, spanning string indexes {} to {}."
              .format(match.re.pattern, match.span()[0], match.span()[1]))
    else:
        print("No match was found.")

# https://docs.python.org/3/library/re.html

# Now, I'll compile my pattern first. This is a more likely scenario for production code.
my_pattern_string = "[Tt]o\\w*"
my_pattern = re.compile(my_pattern_string)
my_strings = ["I, Mr Tough, need to walk toward the toilet tonight!",
              "no matches here",
              "You go to hell! You go to hell and you die!"]
for s in my_strings:
    print("Search for instances of regex pattern '{}' in string: [{}]".format(my_pattern_string, s))
    my_match_iterator = my_pattern.finditer(s)
    print("MATCHES FOUND:")
    for match in my_match_iterator:
        print(match)

# Regex is also handy for splitting a string
split_result = re.split("[\\d]+", "This1will2be3split1234on5743every43242integer42344it43202328finds423.")
print(split_result)
