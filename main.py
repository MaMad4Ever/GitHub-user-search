import customtkinter as ctk
from customtkinter import CTkImage
from tkinter import PhotoImage
import requests
from PIL import Image, ImageDraw
from io import BytesIO

ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.title("Github User Search")
root.geometry("900x500+300+200")
root.resizable(False, False)
root.configure(fg_color="#141d2f")
icon_image = PhotoImage(file='assets/logo.png')
root.iconphoto(False, icon_image)


def search_users():
    username = search_label.get()
    if username:
        response = requests.get(f"https://api.github.com/users/{username}")
        if response.status_code == 200:
            user_data = response.json()
            display_user_info(user_data)
        else:
            label_result.configure(text="User  not found", text_color="red")
    else:
        label_result.configure(text="Please enter a username", text_color="red")

def load_image(url,  size=(100, 100)):
    response = requests.get(url)
    if response.status_code == 200:
        img_data = Image.open(BytesIO(response.content)).convert("RGBA")
        
        mask = Image.new("L", size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size[0], size[1]), fill=255)

        img_data = img_data.resize(size, Image.Resampling.LANCZOS)
        circular_image = Image.new("RGBA", size)
        circular_image.paste(img_data, (0, 0), mask)

        return ctk.CTkImage(light_image=circular_image, size=size)
    else:
        return None

def display_user_info(user_data):
    label_result.configure(text="")
    label_name.configure(text=user_data.get('name', 'N/A'))
    label_username.configure(text="@" + user_data.get('login', 'N/A'))
    label_bio.configure(text=user_data.get('bio'))
    label_join.configure(text="Joined " + user_data.get('created_at', 'N/A')[0:4])
    label_repos_num.configure(text=user_data.get('public_repos', 'N/A'))
    label_followers_num.configure(text=user_data.get('followers', 'N/A'))
    label_following_num.configure(text=user_data.get('following', 'N/A'))
    label_location.configure(text=user_data.get('location', 'N/A'))
    label_x.configure(text=user_data.get('twitter_username', 'N/A'))
    label_link.configure(text=user_data.get('blog', 'N/A'))
    label_company.configure(text=user_data.get('company', 'N/A'))
    avatar_url = user_data.get('avatar_url')
    avatar_image = load_image(avatar_url)
    label_avatar.configure(image=avatar_image)


title_label = ctk.CTkLabel(root,text="DevFinder", font=("Courier New", 22, "bold"))
title_label.place(x=200, y=10)

label_result = ctk.CTkLabel(root, text="")
label_result.place(x=160, y=70)

search_label = ctk.CTkEntry(root, placeholder_text="Search Github username", border_width=0, width=390, height=60, font=("Courier New", 16), fg_color="#1e2a47", placeholder_text_color="#fff",text_color="#fff", corner_radius=15)
search_label.place(x=200, y=50)

search_button = ctk.CTkButton(root,text="Search", command=search_users, font=("Courier New", 16, "bold"),border_width=0, cursor="hand2",width=100, height=60, fg_color="#0079ff",hover_color="#60abff",text_color="#fff", corner_radius=15)
search_button.place(x=600, y=50)

frame = ctk.CTkFrame(root, fg_color="#1e2a47", width=500, height=360, corner_radius=15)
frame.place(x=200, y=130)

image_url = "https://avatars.githubusercontent.com/u/113606119?v=4"
image = load_image(image_url)
label_avatar = ctk.CTkLabel(frame, image=image, text="", corner_radius=50)
label_avatar.place(x=10, y=20)

label_name = ctk.CTkLabel(frame, text="MaMad", font=("Courier New", 22, "bold"))
label_name.place(x=140, y=20)

label_username = ctk.CTkLabel(frame, text="@MaMad4Ever", text_color="#0079ff")
label_username.place(x=140, y=40)

label_bio = ctk.CTkLabel(frame, text="This profile has no bio")
label_bio.place(x=140, y=70)

label_join = ctk.CTkLabel(frame, text="Joined 2020",font=("Space Mono", 14))
label_join.place(x=390, y=0)

user_stats = ctk.CTkFrame(frame, fg_color="#141d2f", width=450, height=100, corner_radius=15)
user_stats.place(x=25, y=150)

label_repos = ctk.CTkLabel(user_stats, text="Repos",font=("Space Mono", 14))
label_repos.place(x=40, y=10)

label_repos_num = ctk.CTkLabel(user_stats, text="22",font=("Courier New", 22, "bold"))
label_repos_num.place(x=40, y=40)

label_followers = ctk.CTkLabel(user_stats, text="Followers",font=("Space Mono", 14))
label_followers.place(x=170, y=10)

label_followers_num = ctk.CTkLabel(user_stats, text="7",font=("Courier New", 22, "bold"))
label_followers_num.place(x=170, y=40)

label_following = ctk.CTkLabel(user_stats, text="Following",font=("Space Mono", 14))
label_following.place(x=330, y=10)

label_following_num = ctk.CTkLabel(user_stats, text="2",font=("Courier New", 22, "bold"))
label_following_num.place(x=330, y=40)

image_location = ctk.CTkImage(Image.open("./assets/location.png"), size=(22, 22))
image_location_label = ctk.CTkLabel(frame, image=image_location, text="")
image_location_label.place(x=20, y=272)
label_location = ctk.CTkLabel(frame, text="Not Available",font=("Space Mono", 16))
label_location.place(x=50, y=270)

image_x = ctk.CTkImage(Image.open("./assets/x.png"), size=(22, 22))
image_x_label = ctk.CTkLabel(frame, image=image_x, text="")
image_x_label.place(x=300, y=270)
label_x = ctk.CTkLabel(frame, text="Not Available",font=("Space Mono", 16))
label_x.place(x=330, y=270)

image_link = ctk.CTkImage(Image.open("./assets/link.png"), size=(22, 22))
image_link_label = ctk.CTkLabel(frame, image=image_link, text="")
image_link_label.place(x=20, y=320)
label_link = ctk.CTkLabel(frame, text="Not Available",font=("Space Mono", 16))
label_link.place(x=50, y=320)

image_company = ctk.CTkImage(Image.open("./assets/organization.png"), size=(22, 22))
image_company_label = ctk.CTkLabel(frame, image=image_company, text="")
image_company_label.place(x=300, y=320)
label_company = ctk.CTkLabel(frame, text="Not Available",font=("Space Mono", 16))
label_company.place(x=330, y=320)

root.mainloop()