import eel
import desktop
import pos

app_name="html"
end_point="index.html"
size=(700,600)

# @ eel.expose
# def kimetsu_search(word,csv_name):
#     search.kimetsu_search(word,csv_name)
@ eel.expose
def main():
    pos.main()
    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)