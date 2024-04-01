const searchBox = document.getElementById('search-main');
searchBox.addEventListener('keypress', (event) => 
{
    if (event.key === 'Enter') 
    {
    // Call a function to submit the form (using Javascript)
    submitSearch();
    }
});

//what actually happens after Enter is pressed
function submitSearch() 
{
  const searchQuery = document.getElementById('search-main').value;
  //better do validation check here to avoid bad input
  if (searchQuery)
  {
    window.location.href = `/${searchQuery}`;  
  }
}

function randNum(min, max) 
{
  // Math.random() generates a random number between 0 (inclusive) and 1 (exclusive)
  const randomDecimal = Math.random();

  // Multiply the random decimal by the range (max minus min) and add the minimum value
  // This scales the random decimal to be within the desired range
  const randomNumber = Math.floor(randomDecimal * (max - min + 1)) + min;

  return randomNumber;
}

function lineChart(x, y)
{
    var trace1 = {
    type: "scatter",
    mode: "lines",
    name: 'A Random Company',
    x: x,
    y: y,
    line: {color: '#17BECF'}
    }

    var data = [trace1];

    var layout = {
    title: 'A Random Company From NASDAQ',
    };

    Plotly.newPlot('line-chart', data, layout);
}

function initialChart(x,y)
{
  
}