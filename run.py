from Opstraextract.bot_ke_function import Booking
import time
with Booking() as bot :
    bot.land_first_page()
    bot.login(email="arindhariwal1@gmail.com", password="arin3054!@")
    bot.kaamka_page()
    bot.open_data()
    column_ki_list = bot.column_name()
    column_ki_list = column_ki_list[:9]
    for i in range (1,11) :
        tareek = bot.lets_date(index=i)
        scape = bot.data_extract()
        bot.create_csvfile(date=tareek, scraped_data=scape, col_ka_data=column_ki_list)
    while True:
        time.sleep(1)