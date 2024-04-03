anychart.onDocumentReady(function() {
    let data = fetch('./Resources/newsArticles.json').then(response => response.json());
    let chart = anychart.tagCloud(data);

    // set a chart title
    chart.title('Sentiment analysis of summarised news articles');
    // set an array of angles at which the words will be laid out
    chart.angles([0, 90]);
    // setting scale to logarithmic (comment if not needed)
    // chart.scale(anychart.scales.log());

    // Setting url
    chart.listen("pointClick", function(e){
        var url = "//en.wiktionary.org/wiki/" + e.point.get("x");
        window.open(url, "_blank");
      });

    // enable a color range
    let colourRange = chart.colorRange(true);
    colourRange.enabled(true);

    colourRange.palette(['#40cf45', '#d13936']);

    // set marker type (optional)
    let marker = colorRange.marker();
    marker.type('diamond');

    // display the word cloud chart
    chart.container("container");
    chart.draw();
});