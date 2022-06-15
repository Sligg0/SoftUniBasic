book_pages = int(input())
pages_per_hour = int(input())
days_to_read = int(input())

#Да се отпечата броят часове, които Жоро трябва да отделя за четене всеки ден.
book_time_to_read = book_pages / pages_per_hour
hours_per_day_for_read = book_time_to_read / days_to_read

print(round(hours_per_day_for_read))