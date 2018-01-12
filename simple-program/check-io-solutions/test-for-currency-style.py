# Your result:  "Clayton Kershaw $31,000,000\nZack Greinke $27,000,000\nAdrian Gonzalez $21,857,143\n"
# Right result: "Clayton Kershaw $31,000,000\nZack Greinke $27,000,000\nAdrian Gonzalez $21,857,143\n"
# and whats wrong

your_result = "Clayton Kershaw $31,000,000\nZack Greinke $27,000,000\nAdrian Gonzalez $21,857,143\n"
right_result = "Clayton Kershaw $31,000,000\nZack Greinke $27,000,000\nAdrian Gonzalez $21,857,143\n"
for i in range(len(your_result)):
    if your_result[i] == right_result[i]:
        print(your_result[i], end='')
    else:
        print('[',your_result[i],']',end='')

print(len(your_result))
print(len(right_result))