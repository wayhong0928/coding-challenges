# Time Conversion
# https://www.hackerrank.com/challenges/time-conversion/problem

# 依序取得AM/PM、小時、分鐘秒數，根據AM/PM調整小時，最後格式化輸出

def timeConversion(s):
    period = s[-2:]
    hour = int(s[:2])
    time = s[2:-2]
    
    if period == 'AM':
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
    
    return f"{hour:02d}{time}"