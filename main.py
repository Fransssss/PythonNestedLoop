# nested loop

print("\n==Practice to deal with nested loop ==")

row = int(input("How many row/s: "))
column = int(input("How many column/s: "))
symbol = input("Input character to fill: ")

for i in range(column):
    for j in range(row):
        print(symbol, end="")       # fill space between symbol with empty string ""
    print()                         # fill in the end of each line with empty string ""/nothing