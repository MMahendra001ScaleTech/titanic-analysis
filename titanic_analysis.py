import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import os
from dotenv import load_dotenv
import requests
from io import StringIO

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(page_title="Titanic Data Analysis", layout="wide")
st.title("🚢 Titanic Dataset Analysis")

# Load data from environment variables
@st.cache_data
def load_data():
    train_url = os.getenv('VITE_TRAIN_DATA_URL')
    test_url = os.getenv('VITE_TEST_DATA_URL')
    
    try:
        # Download the files using requests
        train_response = requests.get(train_url)
        test_response = requests.get(test_url)
        
        # Check if the responses were successful
        train_response.raise_for_status()
        test_response.raise_for_status()
        
        # Read the CSV data from the response content
        train_data = pd.read_csv(StringIO(train_response.text))
        test_data = pd.read_csv(StringIO(test_response.text))
        
        return train_data, test_data
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None, None

# Load data
train_df, test_df = load_data()

if train_df is not None:
    # Sidebar
    st.sidebar.header("Analysis Options")
    analysis_type = st.sidebar.selectbox(
        "Choose Analysis",
        ["Overview", "Survival Analysis", "Age Distribution", "Passenger Class Analysis", "Survival Prediction"]
    )

    if analysis_type == "Overview":
        st.header("Dataset Overview")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("First Few Rows")
            st.dataframe(train_df.head())
        
        with col2:
            st.subheader("Dataset Info")
            buffer = st.empty()
            with buffer:
                st.write(f"Total Passengers: {len(train_df)}")
                st.write(f"Survival Rate: {(train_df['Survived'].mean()*100):.2f}%")
                st.write(f"Features Available: {', '.join(train_df.columns)}")

    elif analysis_type == "Survival Analysis":
        st.header("Survival Analysis")
        
        # Gender and Survival
        fig_gender = px.pie(train_df, 
                          names='Sex', 
                          title='Gender Distribution',
                          hole=0.3)
        st.plotly_chart(fig_gender)

        # Survival by Gender
        survival_by_gender = train_df.groupby(['Sex', 'Survived']).size().unstack()
        fig_survival = go.Figure(data=[
            go.Bar(name='Did Not Survive', x=survival_by_gender.index, y=survival_by_gender[0]),
            go.Bar(name='Survived', x=survival_by_gender.index, y=survival_by_gender[1])
        ])
        fig_survival.update_layout(title='Survival by Gender', barmode='group')
        st.plotly_chart(fig_survival)

    elif analysis_type == "Age Distribution":
        st.header("Age Distribution Analysis")
        
        # Age distribution
        fig_age = px.histogram(train_df, 
                             x='Age', 
                             nbins=30,
                             title='Age Distribution',
                             color='Survived',
                             labels={'Survived': 'Survival Status'})
        st.plotly_chart(fig_age)

        # Age statistics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Average Age", f"{train_df['Age'].mean():.1f}")
        with col2:
            st.metric("Youngest Passenger", f"{train_df['Age'].min():.0f}")
        with col3:
            st.metric("Oldest Passenger", f"{train_df['Age'].max():.0f}")

    elif analysis_type == "Passenger Class Analysis":
        st.header("Passenger Class Analysis")
        
        # Class distribution
        fig_class = px.pie(train_df, 
                          names='Pclass',
                          title='Passenger Class Distribution',
                          hole=0.3)
        st.plotly_chart(fig_class)

        # Survival rate by class
        survival_by_class = train_df.groupby('Pclass')['Survived'].mean() * 100
        fig_survival_class = px.bar(x=survival_by_class.index, 
                                  y=survival_by_class.values,
                                  title='Survival Rate by Passenger Class',
                                  labels={'x': 'Passenger Class', 'y': 'Survival Rate (%)'})
        st.plotly_chart(fig_survival_class)

    elif analysis_type == "Survival Prediction":
        st.header("Survival Prediction Model")
        
        # Prepare data for modeling
        def prepare_data(df):
            df = df.copy()
            df['Age'].fillna(df['Age'].median(), inplace=True)
            df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
            return df[['Pclass', 'Sex', 'Age', 'Fare']]

        X = prepare_data(train_df)
        y = train_df['Survived']
        
        # Train model
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Model performance
        val_pred = model.predict(X_val)
        accuracy = accuracy_score(y_val, val_pred)
        
        st.metric("Model Accuracy", f"{accuracy:.2%}")
        
        # Feature importance
        importance_df = pd.DataFrame({
            'Feature': X.columns,
            'Importance': model.feature_importances_
        }).sort_values('Importance', ascending=False)
        
        fig_importance = px.bar(importance_df, 
                              x='Feature', 
                              y='Importance',
                              title='Feature Importance')
        st.plotly_chart(fig_importance)
        
        # Interactive prediction
        st.subheader("Try Predicting Survival")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            p_class = st.selectbox("Passenger Class", [1, 2, 3])
        with col2:
            sex = st.selectbox("Gender", ["male", "female"])
        with col3:
            age = st.number_input("Age", 0, 100, 30)
        with col4:
            fare = st.number_input("Fare", 0.0, 600.0, 32.2)
            
        if st.button("Predict"):
            input_data = pd.DataFrame([[p_class, 1 if sex == "female" else 0, age, fare]],
                                    columns=['Pclass', 'Sex', 'Age', 'Fare'])
            prediction = model.predict_proba(input_data)[0]
            
            st.write(f"Survival Probability: {prediction[1]:.2%}")
            
            if prediction[1] > 0.5:
                st.success("This passenger would likely survive! ✨")
            else:
                st.error("This passenger would likely not survive 😢")
else:
    st.error("Failed to load the Titanic dataset. Please check your internet connection and try again.")