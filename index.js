import puppeteer from 'puppeteer';

let queryStart = 'https://au.finance.yahoo.com/quote/';
let queryEnd = '?.tsrc=fin-srch';

let csvToJson = (data, delimiter= ',') => {
    let titles = data.slice(0, data.indexOf('\n')).split(delimiter);
    return data
        .slice(data.indexOf('\n') + 1)
        .split('\n')
        .map(v => {
            let values = v.split(delimiter);
            return titles.reduce(
                (obj, title, index) => ((obj[title] = values[index]), obj), {});
        });
};


function mainQuery(tickerSymbols) {
    for (let i = 0; i < tickerSymbols.length; i++) {
        let queryURL = `${queryStart}+${tickerSymbols[i][1]}+${queryEnd}`;
        console.log(queryURL);
        //main();
    };
};


let main = async() => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(queryURL);

    let allArticles = await page.eveluate(() => {
        let articles = document.querySelectorAll('Cf');
        return Array.from(articles).slice(0,5).map((article) => {
            const title = article.querySelector('a').innerText();
            const hyperLink = article.querySelector('a').href();
            return {title, hyperLink};
        });
    });

    console.log(allArticles);
    // Closing browser
    await browser.close();
};

let tickerSymbols = csvToJson(window.open('Resources/ASX_Listed_Companies_25-03-2024_02-42-20_AEDT.csv'));
console.log(tickerSymbols);
mainQuery();
// News pages are found here:
    // <div class="Cf">
    // Check image in folder for reference

// TODO: Figure out how to implement node.js in project