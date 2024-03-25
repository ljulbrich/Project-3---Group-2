// libraries to use:
    // Cheerio for webscraping
    // Nightmare for webpage automation
import * as cheerio from 'cheerio';
import puppeteer from 'puppeteer';

let queryStart = 'https://au.finance.yahoo.com/quote/';
let queryEnd = '?.tsrc=fin-srch';

let tickerSymbols = {
    'Google' : 'GOOG',
    'Apple' : 'APPL',
    'Microsoft' : 'MSFT',
    'NVIDIA' : 'NVDA',
    'Amazon' : 'AMZN',
    'META' : 'META' 
};

function queryURL {
    
};


let main = async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(queryURL);

    let allArticles = await page.eveluate(() => {
        let articles = document.querySelectorAll('article');
        return Array.from(articles).slice(0,3).map((article) => {
            const title = article.querySelector()
        })
    })

    // Closing browser
    await browser.close();
}

// News pages are found here:
    // <div class="Cf">
    // Check image in folder for reference

// TODO: Figure out how to implement node.js in project