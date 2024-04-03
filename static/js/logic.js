//listener for Enter key
const searchBox = document.getElementById('search');
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
  const searchQuery = document.getElementById('search').value;
  //better do validation check here to avoid bad input
  if (searchQuery)
  {
    window.location.href = `/${searchQuery}`;  
  }
}
