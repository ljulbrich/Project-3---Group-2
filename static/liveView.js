document.getElementById('stock').innerHTML = JSON.stringify(liveView)

function format_date(date) {
    const dtFormat = new Intl.DateTimeFormat('en-GB', {
        year: '2-digit',
        month: '2-digit',
        day: '2-digit'
    })
    return dtFormat.format(new Date(date))
}

var selectorOptions = {
    buttons: [{
        step: 'month',
        stepmode: 'backward',
        count: 1,
        label: '1m'
    }, {
        step: 'month',
        stepmode: 'backward',
        count: 6,
        label: '6m'
    }, {
        step: 'year',
        stepmode: 'todate',
        count: 1,
        label: 'YTD'
    }, {

        step: 'year',
        stepmode: 'backward',
        count: 1,
        label: '1y'
    }, {
        step: 'all',
    }],

};

let high = {
    x: [],
    y: [],
    type: 'scatter',
    name: 'High',
    marker: {
        color: 'rgb(0,255,0)',
        width: 2
    }
};

let low = {
    x: [],
    y: [],
    type: 'scatter',
    name: 'Low',
    marker: {
        color: 'rgb(255,0,0)',
        width: 2
    }
};

if (Object.keys(liveView).length > 0) {
    for (var row of Object.values(liveView)) {
        let date = String(format_date(row.Date));
        let highRow = row.High;
        let lowRow = row.Low;

        high.x.push(date);
        high.y.push(highRow);

        low.x.push(date);
        low.y.push(lowRow);
    }
};
let layout = {
    title: 'Long term stock view',
    x: {
        rangeselector: selectorOptions,
        rangeslider: {}
    },
    y: {fixedrange: true}
};

let data = [high, low];

Plotly.newPlot('liveView', data, layout);