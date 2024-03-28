anychart.onDocumentReady(function() {
    let data = [
        {"x":'not been profitable', "value":0.9997759461402893, 'catagory':'NEGATIVE'},
        {"x":"We Wouldn't Be Too Quick", "value":0.9955692887306213, 'catagory':'NEGATIVE'},
        {"x":"potential dividends", "value":0.8955692887306213, 'catagory':'POSITIVE'},
        {"x":"Bad eggs, good profits", "value":0.999992887306229, 'catagory':'POSITIVE'}
        ];
    let chart = anychart.tagCloud(data);

    // set a chart title
    chart.title('Sentiment analysis of summarised news articles')
    // set an array of angles at which the words will be laid out
    chart.angles([0, 90])

    // enable a color range
    let colorRange = chart.colorRange(true);
    colorRange.enabled(true);

    colorRange.palette(['#40cf45', '#d13936']);

    // set marker type (optional)
    // let marker = colorRange.marker();
    // marker.type('diamond');


    // format tooltips
    var formatter = "{%value}{scale:(1)(1000)(1000)(1000)|()( thousand)( million)( billion)}";
    var tooltip = chart.tooltip();
    tooltip.format(formatter);

    // display the word cloud chart
    chart.container("container");
    chart.draw();
});