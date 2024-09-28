const { exec } = require('child_process');

// Start the Flask backend server
const flaskProcess = exec('python app.py', { cwd: __dirname });

flaskProcess.stdout.on('data', (data) => {
  console.log(`Flask: ${data}`);
});

flaskProcess.stderr.on('data', (data) => {
  console.error(`Flask Error: ${data}`);
});

flaskProcess.on('close', (code) => {
  console.log(`Flask process exited with code ${code}`);
});

// Start the React frontend (Vite dev server)
const viteProcess = exec('npm run dev', { cwd: __dirname });

viteProcess.stdout.on('data', (data) => {
  console.log(`Vite: ${data}`);
});

viteProcess.stderr.on('data', (data) => {
  console.error(`Vite Error: ${data}`);
});

viteProcess.on('close', (code) => {
  console.log(`Vite process exited with code ${code}`);
});
