# Firebase Setup Guide

This guide will help you set up Firebase to store team data online so all users can access the same data.

## Step 1: Create a Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click "Add project" or "Create a project"
3. Enter project name: "Harbor Editorial Team" (or your preferred name)
4. Disable Google Analytics (optional) or enable it if you want
5. Click "Create project"

## Step 2: Enable Firestore Database

1. In your Firebase project, click "Firestore Database" in the left menu
2. Click "Create database"
3. Select "Start in test mode" (for now - you can add security rules later)
4. Choose a location (closest to your users)
5. Click "Enable"

## Step 3: Get Your Firebase Config

1. In Firebase Console, click the gear icon ⚙️ next to "Project Overview"
2. Click "Project settings"
3. Scroll down to "Your apps" section
4. Click the `</>` (Web) icon to add a web app
5. Register app with a nickname (e.g., "Harbor Team Management")
6. Copy the `firebaseConfig` object

## Step 4: Update firebase-config.js

1. Open `firebase-config.js` in this project
2. Replace the placeholder values with your actual Firebase config:

```javascript
const firebaseConfig = {
    apiKey: "YOUR_ACTUAL_API_KEY",
    authDomain: "your-project-id.firebaseapp.com",
    projectId: "your-project-id",
    storageBucket: "your-project-id.appspot.com",
    messagingSenderId: "123456789",
    appId: "1:123456789:web:abcdef"
};
```

## Step 5: Set Up Firestore Security Rules (Important!)

1. In Firebase Console, go to "Firestore Database" → "Rules"
2. Replace the rules with:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Allow read/write access to teamData for everyone
    // In production, you may want to add authentication
    match /teamData/{document=**} {
      allow read, write: if true;
    }
  }
}
```

3. Click "Publish"

**Note:** The rules above allow anyone to read/write. For production, consider:
- Adding authentication
- Restricting writes to authenticated users
- Using Firebase App Check for additional security

## Step 6: Deploy to GitHub Pages

1. Commit and push your changes:
   ```bash
   git add .
   git commit -m "Add Firebase integration for shared data storage"
   git push
   ```

2. Your site will automatically update on GitHub Pages

## How It Works

- **First user**: Data is initialized from `getInitialTeamMembers()` and saved to Firebase
- **All users**: Data is loaded from Firebase, so everyone sees the same data
- **Updates**: When anyone makes changes, they're saved to Firebase and visible to all users
- **Fallback**: If Firebase is unavailable, it falls back to localStorage

## Testing

1. Open the site on one computer and make a change
2. Open the site on another computer (or refresh)
3. You should see the same data on both

## Troubleshooting

- **"Firebase is not defined"**: Make sure `firebase-config.js` is loaded before `script.js`
- **Permission denied**: Check your Firestore security rules
- **Data not syncing**: Check browser console for errors
- **Still using localStorage**: Firebase config might be incorrect - check console

## Optional: Add Authentication

If you want to restrict who can edit data:

1. Enable Authentication in Firebase Console
2. Add authentication to your app
3. Update Firestore rules to require authentication:
   ```javascript
   allow read: if true;
   allow write: if request.auth != null;
   ```
