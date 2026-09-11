import re
email=input("enter  your email")
if re.search(r"^[^@]+@[^@]+\.edu$",email):
    print("valid")

else:
    print("invalid")
# ===================== REGEX NOTES =====================
# Regex = Regular Expression → used to search/check patterns in text.
# Python: import re
# re.search(pattern, text) → searches pattern; returns Match if found, None otherwise.
#
# ---------------- BASIC SYMBOLS ----------------
# .       → any ONE character
# *       → 0 or more repetitions
# +       → 1 or more repetitions
# ?       → 0 or 1 repetition
# {m}     → exactly m times
# {m,n}   → m to n times
#
# Examples:
# a* → "", "a", "aa", "aaa"...
# a+ → "a", "aa", "aaa"... (empty not allowed)
# a? → "" or "a"
# a{3} → "aaa"
# a{2,4} → "aa", "aaa", "aaaa"
#
# IMPORTANT: quantifier applies to the thing immediately before it.
# ab* → a + 0 or more b
# (ab)* → whole "ab" repeats 0 or more times
#
# ---------------- ANCHORS ----------------
# ^ → START of string
# $ → END of string
#
# ^hello → "hello world" ✓, "my hello" ✗
# hello$ → "say hello" ✓, "hello123" ✗
#
# IMPORTANT: ^ inside [] has DIFFERENT meaning:
# ^hello     → START
# [^abc]     → NOT a/b/c
#
# ---------------- CHARACTER SET ----------------
# [abc]  → ONE character: a OR b OR c
# [a-z]  → lowercase letter
# [A-Z]  → uppercase letter
# [0-9]  → digit
# [^abc] → any character EXCEPT a, b, c
#
# ---------------- SPECIAL CHARACTERS ----------------
# \d → decimal digit (0-9)
# \D → NOT a digit
# \s → whitespace (space, tab, newline)
# \S → NOT whitespace
# \w → word character (letters, numbers, _)
# \W → NOT a word character
#
# Capital version = usually opposite:
# \d ↔ \D
# \s ↔ \S
# \w ↔ \W
#
# ---------------- DOT ----------------
# .  → any ONE character
# \. → actual/literal dot
#
# Example:
# a.b   → aab, acb, a5b...
# a\.b  → only a.b
#
# ---------------- OR & GROUP ----------------
# A|B       → A OR B
# (abc)     → group
# (?:abc)   → non-capturing group
#
# Example:
# cat|dog   → cat OR dog
# (ab)+     → "ab", "abab", "ababab"...
#
# ---------------- FLAGS ----------------
# re.IGNORECASE → ignores uppercase/lowercase
# re.MULTILINE  → ^ and $ work for each line
# re.DOTALL     → . also matches newline
#
# ---------------- RAW STRING ----------------
# r"\d+" → raw string; useful for regex backslashes.
#
# ---------------- .strip() ----------------
# .strip() is NOT regex.
# Removes whitespace from START and END of a string.
# "  anuj@gmail.edu  ".strip() → "anuj@gmail.edu"
#
# ---------------- EMAIL EXAMPLES ----------------
# r".*@.*"
# → anything + @ + anything
# → @ alone ALSO matches because .* allows ZERO characters.
#
# r"..*@..*"
# → at least 1 character + @ + at least 1 character
# → @ ✗
# → hello@ ✗
# → @gmail ✗
# → hello@gmail ✓
#
# r"^.+@.+\.edu$"
# → START + 1+ chars + @ + 1+ chars + .edu + END
#
# anuj@gmail.edu       ✓
# anuj@gmail.com       ✗
# @gmail.edu            ✗
# anuj@.edu             ✗
# anuj@gmail.edu123     ✗
# my anuj@gmail.edu     ✓  ← because .+ allows spaces
#
# IMPORTANT: ^.+@.+\.edu$ is only a BASIC pattern,
# not a complete/strict email validator.
#
# =========================================================
# QUICK MEMORY:
# . = any 1
# * = 0+
# + = 1+
# ? = 0/1
# ^ = START
# $ = END
# [] = SET
# [^] = NOT SET
# \d = digit
# \s = whitespace
# \w = word
# | = OR
# \. = actual dot
# =========================================================