//listener for Enter key
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

function newsPage(news)
{
  const dropdown = document.getElementById("pages");

  //we only display 3 news per page
  for (let i=1; i<Math.ceil(news.length/3)+1; i++)
    {
      //create an option for each id
      let option = document.createElement("option");
      option.value = i;
      option.text = "page " + i;
      //populate the dropdown with options
      dropdown.appendChild(option);
    };
    let defaultPage = 1;
    createNews(defaultPage, news);
}

function createNews(page, news)
{
  //using math to decide the starting item based on page value
  let start = 3*(page-1);
  let end = start+3;
  let thisPage = news.slice(start, end);
  //console.log(thisPage[0][0].url);

  for (let i=0; i<3; i++) 
  {
    // Clear existing content
    document.getElementById(`row${i+1}`).innerHTML = ""; 

    // Create image element
    const image = document.createElement('img');
    image.src = thisPage[i][0].url; // Replace with your image source paths
    image.alt = `News Image ${i}`;
    image.width = 215;
    image.height = 120;
    image.style.marginBottom = "5px";

    // Create text element as a hyperlink
    const text = document.createElement('a');
    text.href = thisPage[i][2].link; 
    text.textContent = thisPage[i][1].title;
    text.target = "_blank"; // Open link in a new tab
    text.style.marginLeft = "15px";

    // Create a container div for each image-text pair
    const rowItem = document.createElement('div');
    // Add a CSS class for styling 
    rowItem.classList.add('row-item'); 
    rowItem.style.display = "flex";
    rowItem.style.alignItems = "center";

    // Append image and text to the row item div
    rowItem.appendChild(image);
    rowItem.appendChild(text);

    // Append the row item to the corresponding row div, and row id start from 1
    document.getElementById(`row${i+1}`).appendChild(rowItem);
  }
}

function optionChanged(value, news)
{
  page = value;
  createNews(page, news);
}

function createTable(data_list) {
    // Reference to the container element
    let demoCard = document.getElementById("company");
    demoCard.innerHTML = ""; // Clear existing content
  
    // Create the table element
    let table = document.createElement("table");
    table.style.width = "100%";
    table.style.height = demoCard.clientHeight + "px";
  
    // Create table rows for data
    for (data of data_list)
    {
      for (const key in data) {
        let row = document.createElement("tr");
        let keyCell = document.createElement("td");
        keyCell.textContent = key;
        let valueCell = document.createElement("td");
        valueCell.textContent = data[key];
        // Right-align value cell
        valueCell.style.textAlign = "right"; 

        row.appendChild(keyCell);
        row.appendChild(valueCell);
        table.appendChild(row);
      }
    }
  
    // Append the table to the container
    demoCard.appendChild(table);
  }

  
function mainChart(x, high, low, name)
{
    var trace1 = {
    type: "scatter",
    mode: "lines",
    name: 'high',
    x: x,
    y: high,
    line: {color: '#17BECF'}
    }

    var trace2 = {
      type: "scatter",
      mode: "lines",
      name: 'low',
      x: x,
      y: low,
      line: {color: '#AD0B00'}
    }

    var data = [trace1, trace2];

    var layout = {
    title: `${name}`,
    xaxis: {
      autorange: true,
      range: [x[0], x[x.length-1]],
      rangeselector: {buttons: [
          {
            count: 1,
            label: '1m',
            step: 'month',
            stepmode: 'backward'
          },
          {
            count: 6,
            label: '6m',
            step: 'month',
            stepmode: 'backward'
          },
          {step: 'all'}
        ]},
      rangeslider: {range: [x[0], x[x.length-1]]},
      type: 'date'
    },
    yaxis: {
      autorange: true,
      range: [Math.min(low), Math.max(high)],
      type: 'linear'
    }
    };

    Plotly.newPlot('main-chart', data, layout);
}
