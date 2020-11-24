import eel
import desktop
import pos


app_name = "html"
end_point = "index.html"
size = (700, 600)


@ eel.expose
def main_1(item_code, order_quantity):
    pos.main(item_code, order_quantity)


@ eel.expose
def main_2(pay_amount, total_price):
    pos.show_change(pay_amount, total_price)

desktop.start(app_name, end_point, size)
