def way_too_long_words():
    n = int(input().strip())
    for _ in range(n):
        s = input().strip()
        if len(s) > 10:
            print(f"{s[0]}{len(s) - 2}{s[-1]}")
        else:
            print(s)
 
 
if __name__ == "__main__":
    way_too_long_words()