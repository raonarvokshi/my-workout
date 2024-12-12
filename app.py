import streamlit as st
import pandas as pd

st.set_page_config(page_title="GYM WORKOUT PLAN")

st.title("Welcome to Raonar's GYM Workout Plan")
st.markdown("---")
st.header("Please select the day you want for your workout: ")
day = st.selectbox("Workout Day", options=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

if day == "Monday":
  st.subheader("Monday Workout Plan")
  pd_df = pd.read_csv("data/days/day_1.csv", index_col=False)
  pd_df = pd_df.drop(columns=["Unnamed: 0"])
  if pd_df["Sets/Reps"].isna().any():
    pd_df["Sets/Reps"] = pd_df["Sets/Reps"].fillna("Just Warmup")
  st.dataframe(pd_df, use_container_width=True, hide_index=True)

elif day == "Tuesday":
  st.subheader("Tuesday Workout Wlan")
  pd_df = pd.read_csv("data/days/day_2.csv", index_col=False)
  pd_df = pd_df.drop(columns=["Unnamed: 0"])
  if pd_df["Sets/Reps"].isna().any():
    pd_df["Sets/Reps"] = pd_df["Sets/Reps"].fillna("Just Warmup")
  st.dataframe(pd_df, use_container_width=True, hide_index=True)

elif day == "Wednesday":
  st.subheader("Wednesday Workout Plan")
  pd_df = pd.read_csv("data/days/day_3.csv", index_col=False)
  pd_df = pd_df.drop(columns=["Unnamed: 0"])
  if pd_df["Sets/Reps"].isna().any():
    pd_df["Sets/Reps"] = pd_df["Sets/Reps"].fillna("Just Warmup")
  st.dataframe(pd_df, use_container_width=True, hide_index=True)

elif day == "Thursday":
  st.subheader("Thursday Workout Plan")
  pd_df = pd.read_csv("data/days/day_4.csv", index_col=False)
  pd_df = pd_df.drop(columns=["Unnamed: 0"])
  if pd_df["Sets/Reps"].isna().any():
    pd_df["Sets/Reps"] = pd_df["Sets/Reps"].fillna("Just Warmup")
  st.dataframe(pd_df, use_container_width=True, hide_index=True)

elif day == "Friday":
  st.subheader("Friday Workout Plan")
  pd_df = pd.read_csv("data/days/day_5.csv", index_col=False)
  pd_df = pd_df.drop(columns=["Unnamed: 0"])
  if pd_df["Sets/Reps"].isna().any():
    pd_df["Sets/Reps"] = pd_df["Sets/Reps"].fillna("Just Warmup")
  st.dataframe(pd_df, use_container_width=True, hide_index=True)


elif day == "Saturday":
  st.subheader("Saturday Workout Plan")
  pd_df = pd.read_csv("data/days/day_6.csv", index_col=False)
  pd_df = pd_df.drop(columns=["Unnamed: 0"])
  if pd_df["Sets/Reps"].isna().any():
    pd_df["Sets/Reps"] = pd_df["Sets/Reps"].fillna("Just Warmup")
  st.dataframe(pd_df, use_container_width=True, hide_index=True)

elif day == "Sunday":
  st.subheader("Sunday Workout Plan")
  pd_df = pd.read_csv("data/days/day_7.csv", index_col=False)
  pd_df = pd_df.drop(columns=["Unnamed: 0"])
  if pd_df["Sets/Reps"].isna().any():
    pd_df["Sets/Reps"] = pd_df["Sets/Reps"].fillna("Just Warmup")
  st.dataframe(pd_df, use_container_width=True, hide_index=True)


st.markdown("---")
st.header("Your Workout Plan Per Week")

workout_plan = pd.read_csv("data/plan/workout_plan.csv", index_col=False)

workout_plan.loc[workout_plan["Workout"] == "Rest or Active Recovery", "Sets/Reps"] = "Just Rest"
workout_plan["Sets/Reps"] = workout_plan["Sets/Reps"].fillna("Just Warmup")

st.dataframe(workout_plan, hide_index=True, use_container_width=True)