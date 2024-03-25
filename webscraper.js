// Importing node.js packages
const fs = require('fs');
const csv = require('csv-parser');
// import puppeteer from 'puppeteer';
// import {createRequire} from 'puppeteer';
// const require = createRequire(import.meta.url)
// import WebContainer from'@webcontainer/api';

let queryStart = 'https://au.finance.yahoo.com/quote/';
let queryEnd = '?.tsrc=fin-srch';

// Converting the ASX list to JSON
let tickerSymbolPath = './Resources/ASX_Listed_Companies_25-03-2024_02-42-20_AEDT.csv';
let companyList = csvToJson(tickerSymbolPath);
console.log(companyList)
function csvToJson(tickerSymbolPath) {
    // const jsonArray = [];

    fs.createReadStream(tickerSymbolPath)
        .pipe(csv())
        .on('data', (row) => {
            companyList.push(row);
        })
        .on('end', () => {
            // console.log(companyList);
        })

};

let tickerSymbols = [];

for (let i = 0; i < companyList.length; i++) {
    console.log(companyList[i]['ASX code']);
    tickerSymbols.push(companyList[i]['ASX code']);
}


// Creating the searchable URL
function mainQuery(tickerSymbols) {
    for (let i = 0; i < tickerSymbols.length; i++) {
        let queryURL = `${queryStart}+${tickerSymbols[i][1]}+${queryEnd}`;
        console.log(queryURL);
        //main();
        return queryURL;
    };
};

// Main webscraping code
let main = async(queryURL) => {

    // const webcontainer = await WebContainer.boot();
    // await webcontainer.mount(projectFiles);
    // const install = await webcontainer.spawn('npm', ['i']);
    // await install.exit;
    // await webcontainer.spawn('npm', ['run','dev']);

    const response = await fetch()
    // Code from puppeteer was not importing
    // const browser = await puppeteer.launch();
    // const page = await browser.newPage();
    // await page.goto(queryURL);

    // let allArticles = await page.eveluate(() => {
    //     let articles = document.querySelectorAll('Cf');
    //     return Array.from(articles).slice(0,5).map((article) => {
    //         const title = article.querySelector('a').innerText();
    //         const hyperLink = article.querySelector('a').href();
    //         return {title, hyperLink};
    //     });
    // });

    // console.log(allArticles);
    // // Closing browser
    // await browser.close();
};

console.log(tickerSymbols);

// Calling all functions
csvToJson(tickerSymbolPath);
mainQuery(tickerSymbols);
// News pages are found here:
    // <div class="Cf">
    // Check image in folder for reference

// TODO: Figure out how to implement node.js in project