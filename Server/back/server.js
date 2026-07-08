const express = require('express');
const path = require('path');

const app = express();
const port = process.env.PORT || 3000;
const frontendDistPath = path.resolve(__dirname, '../front/dist');

// Middleware to parse JSON requests
app.use(express.json());

// Serve the built frontend assets.
app.use(express.static(frontendDistPath));

app.get('/api', (req, res) => {

    const clientInfo = {
        ip: req.ip,
        ips: req.ips,
        userAgent: req.get('User-Agent'),
        referer: req.get('Referer'),
        origin: req.get('Origin'),
        host: req.get('Host'),
        method: req.method,
        url: req.originalUrl,
        headers: req.headers,
        query: req.query,
        body: req.body
    };


    // res.send('hello backend')

    // setTimeout(() => {
    //     res.json({ message: 'water' });
    // }, 3000);

    res.json({ message: 'Click Button', data: clientInfo });
});

// Support client-side routing by returning the frontend entry point
// for GET requests that did not match a static file or API route.
app.use((req, res, next) => {
    if (req.method !== 'GET') {
        return next();
    }

    return res.sendFile(path.join(frontendDistPath, 'index.html'));
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
}); 
