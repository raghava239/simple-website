const express = require('express');
const path = require('path');
const app = express();
const PORT = 80; // Standard HTTP port for LB access

// Middleware to parse form data
app.use(express.urlencoded({ extended: true }));

// 1. Serve the Login Page at the root IP
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'login.html'));
});

// 2. Accept any username/password and redirect
app.post('/auth', (req, res) => {
    const { username } = req.body;
    console.log(`User ${username} logged in.`);
    // Redirecting to the /login path as requested
    res.redirect('/login');
});

// 3. The Landing path after login
app.get('/login', (req, res) => {
    res.send('<h1>Success</h1><p>You have reached the /login path.</p>');
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
