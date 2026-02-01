# GitHub Setup Instructions

## Step 1: Create a New Repository on GitHub

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Name it: `harbor-team-management` (or any name you prefer)
5. Choose **Public** or **Private** (your choice)
6. **DO NOT** initialize with README, .gitignore, or license (we already have these)
7. Click "Create repository"

## Step 2: Connect Your Local Repository to GitHub

After creating the repository on GitHub, you'll see instructions. Run these commands in your terminal:

```bash
cd /Users/natecali/Documents/Cursor/team-management

# Add the remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/harbor-team-management.git

# Push your code
git branch -M main
git push -u origin main
```

## Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click on **Settings** (top menu)
3. Scroll down to **Pages** (left sidebar)
4. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **Save**
6. Your site will be live at: `https://YOUR_USERNAME.github.io/harbor-team-management/`

## Step 4: Update the Repository (Future Changes)

Whenever you make changes to your website:

```bash
cd /Users/natecali/Documents/Cursor/team-management

# Check what changed
git status

# Add all changes
git add .

# Commit with a message
git commit -m "Description of your changes"

# Push to GitHub
git push
```

GitHub Pages will automatically update within a few minutes!

## Tips

- The site will be available at: `https://YOUR_USERNAME.github.io/harbor-team-management/`
- Changes may take 1-2 minutes to appear after pushing
- You can customize the repository name, but remember to update the URL accordingly
- All data is stored in browser localStorage, so each visitor has their own data


