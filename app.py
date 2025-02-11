import streamlit as st
import pandas as pd
import pickle
final_df = pd.read_csv('final_df.csv')

teams = ['Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad', 'Delhi Capitals',
         'Chennai Super Kings', 'Gujarat Titans', 'Lucknow Super Giants', 'Kolkata Knight Riders',
         'Punjab Kings', 'Mumbai Indians']

city = ['Ahmedabad', 'Kolkata', 'Mumbai', 'Navi Mumbai', 'Pune', 'Dubai', 'Sharjah', 'Abu Dhabi', 'Delhi',
        'Chennai', 'Hyderabad', 'Visakhapatnam', 'Chandigarh', 'Bengaluru', 'Jaipur', 'Indore', 'Bangalore',
        'Kanpur', 'Rajkot', 'Raipur', 'Ranchi', 'Cuttack', 'Dharamsala', 'Nagpur', 'Johannesburg', 'Centurion',
        'Durban', 'Bloemfontein', 'Port Elizabeth', 'Kimberley', 'East London', 'Cape Town']

pipe = pickle.load(open('pipe.pkl', 'rb'))

batsman = final_df['batter'].unique().tolist()
bowler = final_df['bowler'].unique().tolist()

st.title("IPL WIN PREDICTOR 🏏")

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team ⚾', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team 🎳', sorted(teams))

col3, col4 = st.columns(2)

with col3:
    batsman = st.selectbox('Select the batsman 🏏', sorted(batsman))

with col4:
    bowler = st.selectbox('Select the bowler 🎯', sorted(bowler))

selected_city = st.selectbox('Select the city,venue 🌍', sorted(city))

target = st.number_input('Target 🎯')

col5, col6, col7 = st.columns(3)

with col5:
    current_score = st.number_input('Current Score 📊')

with col6:
    overs_done = st.number_input('Overs Done 🕒')

with col7:
    wickets_down = st.number_input('Wickets Down 🏏')

runs_left = 0
ball_left = 0
wickets = 0
crr = 0
rrr = 0

if st.button('Predict Probability 🔮'):
    runs_left = target - current_score
    ball_left = 120 - (overs_done * 6)
    wickets = 10 - wickets_down
    crr = current_score / overs_done
    rrr = (runs_left * 6) / ball_left

    # Output with Emojis and Messages
    st.subheader(f"Match Status 🏟️")
    st.text(f"🧮 **Target:** {target} | 🏏 **Batting Team:** {batting_team} | 🎳 **Bowling Team:** {bowling_team}")
    st.text(f"⚡ **Runs Left:** {runs_left} | ⏳ **Balls Left:** {ball_left} | 🏃‍♂️ **Wickets Left:** {wickets}")
    st.text(f"📈 **Current Run Rate (CRR):** {crr:.2f} | 📊 **Required Run Rate (RRR):** {rrr:.2f}")

    # Win/Loss Probability
    st.subheader(f"Predicted Win Probabilities 🎯")
    st.text(f"💥 **{batting_team} win probability:** {win * 100:.2f}%")
    st.text(f"🔥 **{bowling_team} win probability:** {loss * 100:.2f}%")

    if win > 0.5:
        st.success(f"🏆 **{batting_team} is likely to win!**")
    else:
        st.warning(f"⚠️ **{bowling_team} has a higher chance of winning!**")
