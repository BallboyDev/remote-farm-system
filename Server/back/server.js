const express = require('express');
const path = require('path');

const app = express();
const port = process.env.PORT || 3000;
const frontendDistPath = path.resolve(__dirname, '../front/dist');

// Middleware to parse JSON requests
app.use(express.json());

// const gpioConnection = (command) => {
//     return new Promise((resolve, reject) => {
//         const client = net.createConnection(
//             {
//                 host: '127.0.0.1',
//                 port: 8888
//             },
//             () => {
//                 client.write(command)
//             }
//         )

//         client.on('data', (data) => {
//             console.log("python 응답 : ", data.toString())
//             client.end()
//         })

//         client.on("error", (error) => {
//             console.error('연결 실패', error.message)
//         })

//         client.setTimeout(3000, () => {
//             client.destroy();
//             reject(new Error("서버 응답 시간 초과"))
//         });
//     })
// }

// Serve the built frontend assets.
app.use(express.static(frontendDistPath));

app.get('/test', (req, res) => {
    res.send('Test route');
});

app.use('/api', require('./routes'));

// Support client-side routing by returning the frontend entry point
// for GET requests that did not match a static file or API route.
app.use((req, res, next) => {
    if (req.method !== 'GET') {
        return next();
    }

    return res.sendFile(path.join(frontendDistPath, 'index.html'));
});

// Start the server
app.listen(port, '::',  () => {
    console.log(`Server is running on http://localhost:${port}`);
}); 
