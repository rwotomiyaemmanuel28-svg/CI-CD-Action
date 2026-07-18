# Flask CI/CD Demo

A minimal Flask app used to demonstrate a GitHub Actions CI/CD pipeline that
builds, tests, and deploys to Azure App Service.

## Endpoints
- `GET /` — hello message
- `GET /health` — health check
- `GET /add/<a>/<b>` — adds two integers

## Local run
```bash
pip install -r requirements.txt
python app.py
# visit http://localhost:8000
```

## Run tests locally
```bash
pytest -v
```

## Setup: GitHub repo
1. Create a new repo on GitHub (e.g. `flask-ci-demo`).
2. Push this folder's contents to it:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Flask app with CI/CD workflow"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo>.git
   git push -u origin main
   ```

## Setup: Azure Web App
1. In the [Azure Portal](https://portal.azure.com), create a new **Web App**:
   - Runtime stack: **Python 3.11**
   - Operating System: **Linux**
   - Pick the Free (F1) tier if available.
2. Once created, go to **Deployment Center** (or **Configuration**) and set the
   **Startup Command** to:
   ```
   gunicorn --bind=0.0.0.0 --timeout 600 app:app
   ```
3. Go to **Get publish profile** (top of the Web App's Overview page) and
   download the `.PublishSettings` file.
4. In your GitHub repo: **Settings → Secrets and variables → Actions → New
   repository secret**
   - Name: `AZURE_WEBAPP_PUBLISH_PROFILE`
   - Value: paste the full contents of the publish profile file
5. Edit `.github/workflows/main_azure.yml` and change
   `AZURE_WEBAPP_NAME` at the top to the exact name of the Web App you
   created.
6. Push a commit (or re-run the workflow from the **Actions** tab). The
   workflow will:
   - Install dependencies and run `pytest`
   - If tests pass, deploy the app to Azure Web App
7. Visit `https://<your-webapp-name>.azurewebsites.net/` to confirm it's live.

## What to submit
1. **CI tool**: GitHub Actions
2. **URL to web app**: `https://<your-webapp-name>.azurewebsites.net/`
3. **Tutorial(s) followed**: https://github.com/skills/deploy-to-azure
   (plus https://github.com/skills/hello-github-actions and
   https://github.com/skills/test-with-actions if you did those first)
4. **Repo URL**: your GitHub repo containing `.github/workflows/main_azure.yml`
