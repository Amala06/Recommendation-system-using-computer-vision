from numpy.lib.twodim_base import mask_indices
import pandas as pd
from pandas.core.frame import DataFrame
import streamlit as st
import plotly.express as px
from PIL import Image
from streamlit.state.session_state import Value

st.set_page_config(page_title='TREND WITH AI')
st.header(' TREND with AI')
excel_file='sample.xlsx'

df_m=pd.read_csv(r'C:\Users\amala\Downloads\maindb.csv')
r=df_m['vote_avg']
v=df_m['vote_count']
c=df_m['vote_avg'].mean()
m=500
d=df_m['weighted_votes']=(r*v+c*m)/(v+m)
d=df_m[['occasion','combination','weighted_votes','skin_colour','prices','o_p']].sort_values('weighted_votes',ascending=False)
v=df_m[['occasion','combination','weighted_votes','skin_colour','prices','o_p']]
k=df_m[['occasion','combination','weighted_votes','skin_colour','prices','o_p']]
l=df_m[['occasion','combination','weighted_votes','skin_colour','prices','o_p']]



skin=d['skin_colour'].unique().tolist()
skin_selected=['MEDIUM FAIR']
mask=d['skin_colour'].isin(skin_selected)
f=d[mask].head(60)
occ=f['occasion'].unique().tolist()
occ_selected=['INTERVIEW']
mask=f['occasion'].isin(occ_selected)
data1=f[mask].head(30)


skin=d['skin_colour'].unique().tolist()
skin_selected=['MEDIUM FAIR']
mask=d['skin_colour'].isin(skin_selected)
e=d[mask].head(60)
var=e['occasion'].unique().tolist()
var_selected=['FESTIVE']
mask=e['occasion'].isin(var_selected)
data2=e[mask].head(20)


skin=d['skin_colour'].unique().tolist()
skin_selected=['MEDIUM FAIR']
mask=d['skin_colour'].isin(skin_selected)
s=d[mask].head(60)
gar=s['occasion'].unique().tolist()
gar_selected=['FRESHERS']
mask=s['occasion'].isin(gar_selected)
data3=s[mask].head(20)



skin=v['skin_colour'].unique().tolist()
skin_selected=['MEDIUM FAIR']
mask=v['skin_colour'].isin(skin_selected)
g=v[mask].head(30)
lal=g['occasion'].unique().tolist()
lal_selected=['FRESHERS']
mask=g['occasion'].isin(lal_selected)
data4=g[mask].tail(10)
dul=data4.sort_values('prices',ascending= True)
hul=data4.sort_values('prices',ascending=False)


skin=k['skin_colour'].unique().tolist()
skin_selected=['MEDIUM FAIR']
mask=k['skin_colour'].isin(skin_selected)
n=k[mask].head(60)
nal=n['occasion'].unique().tolist()
nal_selected=['INTERVIEW']
mask=n['occasion'].isin(nal_selected)
data7=n[mask].tail(20)
lul=data7.sort_values('prices',ascending= True)
nul=data7.sort_values('prices',ascending=False)









img=Image.open(r'C:\Users\amala\Downloads\intw.jpg')
imu=Image.open(r'C:\Users\amala\Downloads\fresh.jpg')
fes=Image.open(r'C:\Users\amala\Downloads\fest.jpg')

nav=st.sidebar.radio("Navigation",["Home","Profile","Know your skin colour","Trends","About Us"])


if nav=="Home":
    nickname=st.text_input("WHAT'S YOUR NICKNAME?")
 
    st.write("welcome {}".format(nickname))

    
    st.write("HOME")
    image =Image.open(r'C:\Users\amala\Downloads\TREND with AI.jpg')
    st.image(image,caption='Let your style speaks for you',use_column_width=True)
   
    st.sidebar.radio("Gender",["Male","Female"])
    st.subheader("Want to know the TREND?")
    st.write("Select the checkbox,and let your style speak for you ")
    if st.checkbox("Show Table"):
        st.table(d)
    

    
    
    skin=d['skin_colour'].unique().tolist()
    skin_selection=st.multiselect('skin_colour:',skin,default=skin)
    mask=(d['skin_colour'].isin(skin_selection))

    st.subheader("Get customised dresses accorrding to your occassion !!")



    choice =st.selectbox("Choose your occassion",["","Freshers","Festive","Interview"])
    
       
    if choice =="Interview":
        st.image(img,caption='Recommendations for you ',use_column_width=True)
        st.table(data1)

        st.write("Who told you that Trendy dresses are costly ?")
        st.subheader("Now you can get YOUR PERFECT FIT at YOUR COST")
        temp_options =['Low','Medium','High']
        temp=st.select_slider("Choose your range",options=temp_options)
        if temp =='Low':
            st.dataframe(lul)
        if temp == 'High':
            st.dataframe(nul)
        



    if choice =="Festive":
        st.image(fes,caption='Recommendations for you',use_column_width=True)
        st.table(data2)
       

            
        
        


        
    if choice=="Freshers":
        st.image(imu,caption='Recommendations for you',use_column_width=True)
        st.table(data3) 
        temp_options =['Low','Medium','High']
        temp=st.select_slider("Choose your range",options=temp_options)
        if temp =='Low':
           st.dataframe(dul)
        if temp == 'High':
           st.dataframe(hul)      


if nav=="Profile":
    st.write("Profile")
    st.subheader("LOGIN INFO")
    username=st.text_input("USER NAME")
    # val=st.number_input("Enter your age")
    val=st.text_input("E-MAIL ID")
    val=st.text_input("PASSWORD",type='password')
    if st.button("LOGIN"):
        st.success("Logged in as {}".format(username))
        st.info("Go to Home")



if nav=="Trends":
    st.write("Trends")
    st.video(r'C:\Users\amala\Downloads\Untitled design (1).mp4')
    st.video(r'C:\Users\amala\Downloads\AI.mp4')

    
if nav=="Know your skin colour":
    
    st.write("𝓔𝓿𝓮𝓻 𝔀𝓸𝓷𝓭𝓮𝓻𝓮𝓭 𝔀𝓱𝓪𝓽'𝓼 𝔂𝓸𝓾𝓻 𝓼𝓴𝓲𝓷 𝓬𝓸𝓵𝓸𝓾𝓻? 𝓴𝓷𝓸𝔀 𝓲𝓽 & 𝓕𝓵𝓪𝓾𝓷𝓽 𝓲𝓽 ,𝓳𝓾𝓼𝓽 𝓫𝔂 𝓬𝓵𝓲𝓬𝓴𝓲𝓷𝓰 𝔂𝓮𝓼")

    photo=st.selectbox("Do you want to know your skin colour ",["","yes","no"])

    if photo == "yes":
        
        import cv2
        import numpy as np


        cam=cv2.VideoCapture(0)
        cv2.namedWindow(" Instant shots/ TrendwithAI")

        img_counter=0

        while True:
            ret,frame=cam.read()

            if not ret:
                print("failed to grab frame")
                break

            cv2.imshow("test",frame)


            k=cv2.waitKey(1)

            if k%256 ==27:
                print("Escape hit,closing the app")
                break

            elif k%256==32:
                img_name="fash{}.jpg".format(img_counter)
                cv2.imwrite(img_name,frame)
                print("screenshot taken")
                img_counter+=1


        img_path = r'fash1.jpg'
        img = cv2.imread(img_path)

# declaring global variables (are used later on)
        clicked = False
        r = g = b = x_pos = y_pos = 0

        # Reading csv file with pandas and giving names to each column
        index = ["color", "color_name", "hex", "R", "G", "B"]
        csv = pd.read_csv(r'C:\Users\amala\Downloads\colors.csv', names=index, header=None)


# function to calculate minimum distance from all colors and get the most matching color
        def get_color_name(R, G, B):
            minimum = 10000
            for i in range(len(csv)):
                d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
                if d <= minimum:
                    minimum = d
                    cname = csv.loc[i, "color_name"]
            return cname


# # function to get x,y coordinates of mouse double click
        def draw_function(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDBLCLK:
                global b, g, r, x_pos, y_pos, clicked
                clicked = True
                x_pos = x
                y_pos = y
                b, g, r = img[y, x]
                b = int(b)
                g = int(g)
                r = int(r)


        cv2.namedWindow('image')
        cv2.setMouseCallback('image', draw_function)

        while True:

            cv2.imshow("image", img)
            if clicked:

        # cv2.rectangle(image, start point, endpoint, color, thickness)-1 fills entire rectangle
                cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        #         # Creating text string to display( Color name and RGB values )
                text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        #         # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
                cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        #         # For very light colours we will display text in black colour
                if r + g + b >= 600:
                    cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

                clicked = False

        #     # Break the loop when user hits 'esc' key
            if cv2.waitKey(20) & 0xFF == 27:
                break



        cam.release()
        # cam.destroyAllWindows()
        cv2.destroyAllWindows()
    
    st.write("Find your sjin colour in the given table &   FLAUNT IT !")

    tone=pd.read_csv(r'C:\Users\amala\Downloads\tone.csv')

    if st.checkbox("Show Table"):
          st.table(tone)

if nav=="About Us":
    st.subheader("About us")
    st.write("People are not made for dresses,but Dresses are  made for the people. With that BetterBots is building webapps that give personalised clothing experience to the people .Valuating indian Skin tone is also our mission .  ")





        



       
 
