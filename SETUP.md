# Project Setup and Deployment Guide

## 1. Task Manager Application

### Local Setup

1. Create a new directory and navigate to it:

```bash
mkdir task-manager
cd task-manager
```

2. Create required files:

- `requirements.txt` for Python dependencies
- `web_task_manager.py` for the Streamlit app
- `.gitignore` for version control

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run locally:

```bash
streamlit run web_task_manager.py
```

### Deployment to Streamlit Cloud

1. Create a GitHub repository and push your code
2. Visit [Streamlit Cloud](https://streamlit.io/cloud)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository
6. Choose `web_task_manager.py` as the main file
7. Click "Deploy"

## 2. Titanic Analysis Dashboard

### Local Setup

1. Create project structure:

```bash
mkdir titanic-analysis
cd titanic-analysis
```

2. Download Titanic dataset from Kaggle:

- Visit: https://www.kaggle.com/c/titanic/data
- Download: `train.csv`, `test.csv`
- Place in project root

3. Create required files:

- `requirements.txt` for dependencies
- `titanic_analysis.py` for the main app
- `.gitignore` for version control

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run locally:

```bash
streamlit run titanic_analysis.py
```

### Deployment to Streamlit Cloud

1. Create GitHub repository
2. Add your dataset files to `.gitignore`:

```
*.csv
__pycache__/
.env
```

3. Create a `data` folder in your repository and add the Titanic dataset
4. Push code to GitHub
5. Deploy on Streamlit Cloud:
   - Visit [Streamlit Cloud](https://streamlit.io/cloud)
   - Connect your GitHub account
   - Select repository
   - Choose `titanic_analysis.py` as main file
   - Deploy

## 3. Stock Market Dashboard

### Local Setup

1. Create project structure:

```bash
mkdir stock-dashboard
cd stock-dashboard
```

2. Create required files:

- `requirements.txt` for dependencies
- `stock_dashboard.py` for the main app
- `.gitignore` for version control

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run locally:

```bash
streamlit run stock_dashboard.py
```

### Deployment to Streamlit Cloud

1. Create GitHub repository
2. Push code to GitHub
3. Deploy on Streamlit Cloud:
   - Visit [Streamlit Cloud](https://streamlit.io/cloud)
   - Connect GitHub account
   - Select repository
   - Choose `stock_dashboard.py` as main file
   - Deploy

## Common Deployment Steps

1. **Version Control Setup**:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

2. **Environment Variables**:

- Create `.env` file for sensitive data
- Add to `.gitignore`
- Configure in deployment platform

3. **Requirements File**:

- Keep `requirements.txt` updated
- Use specific versions
- Test dependencies locally

4. **Deployment Checklist**:

- All dependencies listed in `requirements.txt`
- Data files accessible
- Environment variables configured
- Main file specified correctly
- Repository permissions set

## Troubleshooting

1. **Common Issues**:

- Missing dependencies
- File path errors
- Environment variable configuration
- Memory limits
- Timeout errors

2. **Solutions**:

- Check logs in deployment platform
- Verify all requirements are installed
- Test locally before deployment
- Monitor resource usage
- Use caching when possible

## Maintenance

1. **Regular Updates**:

- Keep dependencies updated
- Monitor application performance
- Check for security updates
- Backup data regularly

2. **Monitoring**:

- Set up alerts for errors
- Monitor resource usage
- Track user activity
- Check application logs
