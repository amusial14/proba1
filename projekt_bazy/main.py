from budowa import Baza
from budowa import create_db
from insertion import insert_data




baza = Baza()



baza.stworz_tabele()

# baza.show_tables()


# baza.clear_table("employees")
# baza.clear_truncate_table("malfunctions")
# baza.clear_truncate_table("payments")
insert_data(baza)

# baza.show_table("payments")
# baza.show_table("payment_ticket")
# baza.show_table("guest_insurance")
baza.show_table("inspections")
baza.show_table("attractions")


# baza.cursor.execute("""
# SELECT DISTINCT
#     g.guest_id,
#     a.attraction_name,
#     p.payment_date
# FROM guests g
# JOIN payments p        ON p.guest_id = g.guest_id
# JOIN payment_ticket pt ON pt.payment_id = p.payment_id
# JOIN prices pr         ON pr.ticket_id = pt.ticket_id
# JOIN attractions a     ON a.attraction_id = pr.attraction_id
# ORDER BY g.guest_id, a.attraction_name;
# """)

# for row in baza.cursor:
#     print(row)



# baza.show_table("attractions")




baza.zamknij_polaczenie()