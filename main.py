text = input("Enter text: ")
# تقسیم متن به جملات
sentences = text.split('.')

result = []  # به جای دیکشنری از لیست استفاده می‌کنیم
def chose_rightOne(text):
    word_count = 0  # شماره کلمه از 1 شروع می‌شود
    
    for sentence in sentences:
        # حذف فاصله‌های اضافی و تقسیم جمله به کلمات
        sentence = sentence.strip()
        if not sentence:  # اگر جمله خالی بود، ادامه بده
            continue
        words = sentence.split()
        
        for i, word in enumerate(words):
            # حذف ویرگول یا نقطه از انتهای کلمه
            clean_word = word.rstrip(',.')
            
            # اگر کلمه خالی شد، ادامه بده
            if not clean_word:
                continue
                
            word_count += 1  # افزایش شماره کلمه
            
            # بررسی اینکه کلمه با حرف بزرگ شروع شود، عدد نباشد و اولین کلمه جمله نباشد
            if clean_word[0].isupper() and not clean_word.isdigit() and i != 0:
                result.append((word_count, clean_word))  # ذخیره به صورت تاپل در لیست
    
    return result

chose_rightOne(text)

# چاپ خروجی
if result:
    for count, word in result:
        print(f"{count}:{word}")
else:
    print("None")
