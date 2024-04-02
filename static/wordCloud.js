anychart.onDocumentReady(function() {
    let dataList = [];
    let text = '';
    document.getElementById('news').innerHTML = JSON.stringify(scrapedData);
    for (var article of Object.values(scrapedData)) {
        let title = article.title;
        let score = article.score;
        let label = article.label;
        let link = article.link;

        dataList.push({
            x:`${title}`,
            value:score,
            category:`${label}`,
            custom_field: `${link}`
        });
    };
        
    console.table(dataList);

    // Create wordCloud
    let chart = anychart.tagCloud(dataList);

    // set a chart title
    chart.title('Sentiment analysis of summarised news articles')
    // set an array of angles at which the words will be laid out
    chart.angles([0, 45])

    chart.mode('spiral')

    chart.listen('pointClick', function(e) {
        let url = `https://au.yahoo.com${e.point.get('custom_field')}`;
        console.log(url);
        window.open(url);
    });

    // enable a color range
    let colorRange = chart.colorRange(true);
    colorRange.enabled(true);

    colorRange.palette(['#40cf45', '#d13936']);

    // display the word cloud chart
    chart.container("container");
    chart.draw();
});
