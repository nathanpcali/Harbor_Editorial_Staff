# Harbor Editorial Team Management

A modern, interactive organizational chart and team management system for Harbor Editorial. This web application allows you to visualize your team hierarchy, manage team member information, and maintain organizational relationships.

## Features

- **Interactive Organizational Chart**: Visual hierarchical display of team structure with connecting lines
- **Team Member Management**: Add, edit, and remove team members
- **Rich Profiles**: Store profile photos, notes, and links for each team member
- **Color-Coded Teams**: Each Creative Director's team is visually distinguished with unique colors
- **Zoom & Pan**: Navigate large organizational charts with zoom and pan controls
- **Local Storage**: All data persists in your browser's local storage
- **Harbor Branding**: Custom dark theme matching Harbor Editorial's brand identity

## Getting Started

### Local Development

1. Clone or download this repository
2. Open `index.html` in your web browser
3. No build process or dependencies required - it's pure HTML, CSS, and JavaScript!

### GitHub Pages Deployment

1. Push this repository to GitHub
2. Go to your repository Settings → Pages
3. Select the branch (usually `main` or `master`)
4. Select the root folder (`/`)
5. Click Save
6. Your site will be available at `https://[your-username].github.io/[repository-name]`

## Usage

### Viewing the Organizational Chart

- The chart displays all team members in a hierarchical structure
- Use the zoom controls (+/-) or mouse wheel (with Ctrl/Cmd) to zoom in/out
- Click and drag to pan around the chart
- Click any team member card to view their details

### Managing Team Members

- **Add Member**: Click the "+ Add Team Member" button
- **Edit Member**: Click on a team member card, then click "Edit"
- **Delete Member**: Click on a team member card, then click "Delete"
- **Add Photos**: Upload an image file or paste a URL in the profile photo field
- **Add Links**: Click "+ Add Link" to add multiple links per team member

### Data Management

- All data is stored in your browser's local storage
- Click "Reset View" to restore the default organizational chart structure
- Data persists across browser sessions

## File Structure

```
team-management/
├── index.html          # Main HTML file
├── styles.css          # All styling and Harbor brand theme
├── script.js           # Application logic and team management
├── fetch-photos.html   # Helper tool for bulk photo uploads
├── harbor-logo.png    # Harbor logo image
└── README.md          # This file
```

## Customization

### Adding Team Members

Team members are defined in `script.js` in the `getInitialTeamMembers()` function. Each member has:
- `id`: Unique identifier
- `name`: Full name
- `title`: Job title
- `photo`: Profile photo URL
- `notes`: Additional notes
- `links`: Array of URLs
- `reportsTo`: ID of the person they report to (null for top level)

### Styling

The Harbor brand theme is defined in `styles.css`. Key color variables:
- Background: Dark navy (#0a1929)
- Text: Light gray (#B0BCC7, #e8eaed)
- Accent: Blue tones (#4a90e2, #1e3a5f)

### Team Colors

Each Creative Director's team has a unique color:
- Aaron Porzel: Blue
- Art Castle: Green
- Jesse Thompson: Red
- Jefferson Chaney: Orange
- Justin Sirizzotti: Purple
- Nate Cali: Yellow

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge

## License

This project is for internal use by Harbor Editorial.

## Support

For issues or questions, please contact the development team.


