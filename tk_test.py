import tkinter

root = tkinter.Tk()
root.title('hoge')
root.geometry("300x200")


# Canvasの作成
canvas = tkinter.Canvas(
    root, 
    width = 200,
    height = 100,
    bg = "cyan"
    )
# Canvasを配置
canvas.pack()

root.mainloop()