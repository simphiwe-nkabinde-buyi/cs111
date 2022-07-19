import tkinter as tk

def main():
    # create the TK root object
    root = tk.Tk()
    root.geometry("570x525")

    #create the main frame.
    frm_main = tk.Frame(root, bd=0, bg="gray10")
    frm_main.master.title("Music Player")
    frm_main.pack(fill=tk.BOTH, expand=1)

    populate_main_window(frm_main)

    root.mainloop()


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """

    # images
    global img_headphones
    global img_play_btn
    global img_pause_btn
    global img_next_btn
    global img_prev_btn
    img_headphones = tk.PhotoImage(file="images/headphones.png", format="png")
    img_play_btn = tk.PhotoImage(file="images/play-button.png", format="png")
    img_pause_btn = tk.PhotoImage(file="images/pause-button.png", format="png")
    img_next_btn = tk.PhotoImage(file="images/next-button.png", format="png")
    img_prev_btn = tk.PhotoImage(file="images/prev-button.png", format="png")

    # labels
    lbl_playin_from = tk.Label(frm_main, text="Playing from Playlist", fg="ivory2", bg="gray10")
    lbl_headphones = tk.Label(frm_main, image=img_headphones, bg="gray10", width=280, height=280)
    lbl_song = tk.Label(frm_main, text="We are the champions", fg="ivory2", bg="gray10", font="bold")
    lbl_artist = tk.Label(frm_main, text="Queen", fg="ivory4", bg="gray10")

    # list box
    list_songs = tk.Listbox(frm_main, selectmode="single", bg="gray8", fg="ivory2", bd=0, highlightthickness=0, selectbackground="gray12", width=36, height=28)

    # buttons
    btn_add_songs = tk.Button(frm_main, cursor="hand2", text="Add Songs", bd=0, fg="ivory3", bg="DarkOrchid4", width=33, highlightthickness=0, activeforeground="ivory4", activebackground="purple4")
    btn_play = tk.Button(frm_main, cursor="hand2", image=img_play_btn, bd=0, bg="gray10", highlightthickness=0, activebackground="gray10")
    btn_pause = tk.Button(frm_main, cursor="hand2", image=img_pause_btn, bd=0, bg="gray10", highlightthickness=0, activebackground="gray10")
    btn_next = tk.Button(frm_main, cursor="hand2", image=img_next_btn, bd=0, bg="gray10", highlightthickness=0, activebackground="gray10")
    btn_prev = tk.Button(frm_main, cursor="hand2", image=img_prev_btn, bd=0, bg="gray10", highlightthickness=0, activebackground="gray10")


    # grid layout
    lbl_playin_from.grid(row=0, column=1, columnspan=11)

    lbl_headphones.grid(row=1, column=0, columnspan=12, pady=20)

    lbl_song.grid(row=2, column=0, columnspan=12, pady=5)
    lbl_artist.grid(row=3, column=0, columnspan=12, pady=0)

    btn_prev.grid(row=4, column=0, columnspan=3, pady=3)
    btn_play.grid(row=4, column=3, columnspan=6, pady=20)
    btn_pause.grid(row=4, column=3, columnspan=6, pady=20)
    btn_next.grid(row=4, column=9, columnspan=3, pady=3)

    btn_add_songs.grid(row=0, column=13)
    list_songs.grid(row=1, rowspan=4, column=13)



# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
