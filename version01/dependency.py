import speedtest
import tkinter as tk

def get_bandwidth():    # gets downlaod speed
    st = speedtest.Speedtest()
    download_speed = st.download()  # Get download speed in bits per second
    download_speed_mbps = download_speed / (1024 * 1024)
    return download_speed_mbps


def show_popup_message(message):
    popup = tk.Tk()
    popup.title("Bandwidth Information")
    popup.geometry("300x50")
    label = tk.Label(popup, text=message)
    label.pack(pady=10)
    popup.mainloop()