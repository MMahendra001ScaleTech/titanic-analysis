# Deployment Guide

## Deploying to Netlify

### Method 1: Deploy via Netlify UI (Recommended for first deployment)

1. **Prepare Your Repository**

   - Push your code to a GitHub repository
   - Make sure all environment variables are properly set in `.env`
   - Ensure `netlify.toml` is present in your repository

2. **Deploy on Netlify**

   - Go to [Netlify](https://app.netlify.com/)
   - Click "Add new site" → "Import an existing project"
   - Connect to your GitHub repository
   - Configure build settings:
     - Build command: `npm run build`
     - Publish directory: `dist`

3. **Configure Environment Variables**

   - Go to Site settings → Environment variables
   - Add your environment variables:
     ```
     VITE_TRAIN_DATA_URL="your_train_data_url"
     VITE_TEST_DATA_URL="your_test_data_url"
     ```

4. **Deploy**
   - Netlify will automatically build and deploy your site
   - You'll get a unique URL for your deployment

### Method 2: Deploy via Netlify CLI

1. **Install Netlify CLI**

   ```bash
   npm install netlify-cli -g
   ```

2. **Login to Netlify**

   ```bash
   netlify login
   ```

3. **Initialize Netlify**

   ```bash
   netlify init
   ```

4. **Deploy**
   ```bash
   netlify deploy --prod
   ```

### Continuous Deployment

Netlify automatically sets up continuous deployment:

- Every push to main branch triggers a new deployment
- Preview deployments for pull requests
- Branch deployments for feature branches

### Environment Variables

1. **Local Development**

   - Use `.env` file locally
   - Never commit `.env` to Git

2. **Production**
   - Set variables in Netlify UI
   - Or use `netlify env:set VARIABLE_NAME "value"`

### Troubleshooting

1. **Build Failures**

   - Check build logs in Netlify UI
   - Verify all dependencies are installed
   - Ensure environment variables are set

2. **Runtime Errors**

   - Check browser console
   - Verify API endpoints
   - Check environment variables

3. **404 Errors**
   - Verify `netlify.toml` redirects
   - Check build output in `dist`

### Monitoring

1. **Analytics**

   - Enable Netlify Analytics
   - Monitor site performance
   - Track user behavior

2. **Notifications**
   - Set up deploy notifications
   - Configure build alerts
   - Monitor site status

### Security

1. **Environment Variables**

   - Use Netlify UI for sensitive data
   - Never expose secrets in code
   - Use appropriate access controls

2. **Headers**
   - Configure security headers
   - Enable HTTPS
   - Set up CSP if needed
