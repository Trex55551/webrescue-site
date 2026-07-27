const requiredFiles = [
  'index.html', 'styles.css', 'script.js', 'privacy.html', 'terms.html',
  'package.json', 'vercel.json', 'assets/example-domain-before.png'
];

const fs = await import('node:fs');
let failed = false;
for (const file of requiredFiles) {
  if (!fs.existsSync(file)) {
    console.error(`MISSING ${file}`);
    failed = true;
  } else {
    console.log(`OK ${file}`);
  }
}

const html = fs.readFileSync('index.html', 'utf8');
for (const marker of ['mailto:', 'Independent concept redesign', 'Evidence & sources', 'Starting at']) {
  if (!html.includes(marker)) {
    console.error(`MISSING CONTENT: ${marker}`);
    failed = true;
  } else {
    console.log(`OK content: ${marker}`);
  }
}
process.exit(failed ? 1 : 0);
