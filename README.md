# Data Analysis Dashboard Suite

This comprehensive data analysis suite includes three interactive dashboards built with Python, Streamlit, and React:

## 1. 🚢 Titanic Dataset Analysis

An interactive dashboard analyzing the famous Titanic dataset with machine learning predictions.

### Features

- Dataset overview and statistics
- Survival analysis by various factors
- Interactive visualizations
- Machine learning prediction model
- Real-time survival probability calculator

## 2. ✅ Task Manager

A full-featured task management application for organizing and tracking tasks.

### Features

- Add and manage tasks
- Set due dates
- Mark tasks as complete
- Delete tasks
- Filter tasks by status
- Persistent storage

## 3. 📈 Stock Market Dashboard

Real-time stock market analysis and visualization tool.

### Features

- Live stock price tracking
- Interactive candlestick charts
- Trading volume analysis
- Key statistics display
- Company information

## Setup Instructions

1. Install Dependencies:

```bash
npm install        # Install Node.js dependencies
pip install -r requirements.txt  # Install Python dependencies
```

2. Environment Variables:
   Create a `.env` file with:

```
VITE_TRAIN_DATA_URL="your_train_data_url"
VITE_TEST_DATA_URL="your_test_data_url"
```

3. Running the Applications:

```bash
npm run dev:titanic  # Run Titanic Analysis
npm run dev:tasks    # Run Task Manager
npm run dev:stocks   # Run Stock Dashboard
npm run dev:all      # Run all applications
```

## Deployment

The applications are deployed using Netlify for the frontend and Streamlit Cloud for the Python backends.

### Frontend (React)

```bash
npm run build
```

The build output will be in the `dist` directory.

### Backend (Streamlit)

Deploy to Streamlit Cloud:

1. Push to GitHub
2. Connect to Streamlit Cloud
3. Select the appropriate Python file
4. Configure environment variables

## Usage

1. Access the dashboards through your browser
2. Navigate between different analysis sections
3. Interact with visualizations and controls
4. Use the prediction tools and filters

## Technologies Used

- Frontend:

  - React
  - TypeScript
  - Tailwind CSS
  - Vite
  - Lucide Icons

- Backend:
  - Python
  - Streamlit
  - Pandas
  - Scikit-learn
  - Plotly
  - Seaborn

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
