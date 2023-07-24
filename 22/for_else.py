accounts = [
    ['ملت', 2_500_000],
    ['تجارت', 4_500_000],
    ['کشاورزی', 3_000_000],
]

x = 6_000_000

for account in accounts:
    if account[1] >= x:
        print('پرداخت از حساب', account[0])
        break
else:
    print('موجودی هیچکدام از حساب‌ها کافی نیست')